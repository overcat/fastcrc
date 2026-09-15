#!/usr/bin/env python3
"""
fastcrc benchmark harness.

    python benchmarks/run.py run [--json PATH|auto] [--quick]
    python benchmarks/run.py report RESULT.json [RESULT.json ...]

`run` measures the installed fastcrc and prints a Markdown report; `--json` also stores the raw
measurements. `report` renders one or more stored result files into a single
Markdown document, e.g. to put two fastcrc versions side by side.

Methodology
-----------
Every measurement is a timed loop of `iterations` calls on the same
`os.urandom` payload, so per-call figures include the Python call overhead.
The iteration count is chosen so that one sample lasts at least
`SAMPLE_SECONDS`; `REPEATS` samples are taken after one warm-up sample and the
fastest one is reported (the usual choice for microbenchmarks, since noise
only ever makes a sample slower). The garbage collector is disabled while
timing. Throughput is bytes / best time, using 1 GB = 10**9 bytes.
"""

import argparse
import datetime as dt
import gc
import inspect
import json
import os
import platform
import re
import statistics
import subprocess
import sys
import threading
import time

SAMPLE_SECONDS = 0.05
REPEATS = 7
KIB, MIB = 1024, 1024 * 1024

# Algorithms profiled across all input sizes: one per width plus the three
# CRC-32 code paths (hardware-assisted ISCSI, reflected and forward generic).
PROFILE = ["crc8.smbus", "crc16.xmodem", "crc32.iscsi", "crc32.iso_hdlc", "crc32.bzip2", "crc64.xz"]
PROFILE_SIZES = [1, 8, 64, 256, KIB, 4 * KIB, 16 * KIB, 64 * KIB, 256 * KIB, MIB, 16 * MIB, 128 * MIB]
# Every algorithm is measured at these two sizes.
SMALL, LARGE = 64, MIB
THREAD_COUNTS = [1, 2, 4, 8]


# --------------------------------------------------------------------------- timing

def time_call(fn, data, repeats=REPEATS, sample_seconds=SAMPLE_SECONDS):
    """Best and median time per call in nanoseconds."""
    iterations = 1
    fn(data)
    while True:  # warm up and calibrate the iteration count
        start = time.perf_counter_ns()
        for _ in range(iterations):
            fn(data)
        elapsed = time.perf_counter_ns() - start
        if elapsed >= sample_seconds * 1e9 / 4:
            break
        iterations *= 4
    iterations = max(1, int(iterations * sample_seconds * 1e9 / max(elapsed, 1)))
    samples = []
    gc_enabled = gc.isenabled()
    gc.disable()
    try:
        for _ in range(repeats):
            start = time.perf_counter_ns()
            for _ in range(iterations):
                fn(data)
            samples.append((time.perf_counter_ns() - start) / iterations)
    finally:
        if gc_enabled:
            gc.enable()
    return min(samples), statistics.median(samples)


def payloads(sizes):
    return {size: os.urandom(size) for size in sorted(set(sizes))}


# --------------------------------------------------------------------------- environment

def cpu_info():
    info = {"model": platform.processor() or platform.machine(), "flags": []}
    try:
        if sys.platform.startswith("linux"):
            text = open("/proc/cpuinfo").read()
            model = re.search(r"^model name\s*:\s*(.+)$", text, re.M)
            flags = re.search(r"^(?:flags|Features)\s*:\s*(.+)$", text, re.M)
            if model:
                info["model"] = model.group(1).strip()
            if flags:
                info["flags"] = flags.group(1).split()
            try:
                info["governor"] = open("/sys/devices/system/cpu/cpu0/cpufreq/scaling_governor").read().strip()
            except OSError:
                pass
        elif sys.platform == "darwin":
            out = subprocess.run(["sysctl", "-n", "machdep.cpu.brand_string"], capture_output=True, text=True)
            if out.returncode == 0:
                info["model"] = out.stdout.strip()
    except OSError:
        pass
    interesting = ["sse4_2", "pclmulqdq", "avx2", "avx512f", "avx512vl", "vpclmulqdq", "aes", "pmull", "sha3", "crc32"]
    info["simd"] = [f for f in interesting if f in info["flags"]]
    del info["flags"]
    info["logical_cpus"] = os.cpu_count()
    return info


def environment():
    import fastcrc

    gil = getattr(sys, "_is_gil_enabled", lambda: True)()
    return {
        "timestamp": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "cpu": cpu_info(),
        "os": f"{platform.system()} {platform.release()}",
        "python": f"{platform.python_implementation()} {platform.python_version()}" + ("" if gil else " (free-threaded)"),
        "fastcrc": fastcrc.__version__,
    }


# --------------------------------------------------------------------------- what to measure

def fastcrc_functions():
    import fastcrc

    for module in ("crc8", "crc16", "crc32", "crc64"):
        mod = getattr(fastcrc, module)
        public = [n for n in dir(mod) if not n.startswith("_") and inspect.isroutine(getattr(mod, n))]
        for name in sorted(mod.algorithms_available) + sorted(set(public) - set(mod.algorithms_available)):
            yield f"{module}.{name}", getattr(mod, name)


def thread_scaling(fn, data, counts):
    """Aggregate throughput in GB/s when `n` threads each hash `data` repeatedly."""
    rows = []
    for n in counts:
        calls = max(20, int(2e9 / len(data) / n))  # ~2 GB of work per thread

        def work():
            for _ in range(calls):
                fn(data)

        threads = [threading.Thread(target=work) for _ in range(n)]
        start = time.perf_counter_ns()
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        elapsed = (time.perf_counter_ns() - start) / 1e9
        rows.append({"threads": n, "gbps": n * calls * len(data) / elapsed / 1e9})
    return rows


# --------------------------------------------------------------------------- run

def run(args):
    env = environment()
    label = f"fastcrc {env['fastcrc']}"
    print(f"# {label} on {env['cpu']['model']} ({env['python']})", file=sys.stderr)
    quick = args.quick
    repeats = 3 if quick else REPEATS
    profile_sizes = [s for s in PROFILE_SIZES if s <= (MIB if quick else 128 * MIB)]
    data = payloads(profile_sizes + [SMALL, LARGE])
    measurements = []

    def record(library, algorithm, size, fn):
        best, median = time_call(fn, data[size], repeats=repeats)
        measurements.append({"library": library, "algorithm": algorithm, "size": size,
                             "ns": best, "ns_median": median, "gbps": size / best})

    functions = dict(fastcrc_functions())
    for name in PROFILE:
        print(f"profile {name}", file=sys.stderr)
        for size in profile_sizes:
            record(label, name, size, functions[name])
    for name, fn in functions.items():
        print(f"all {name}", file=sys.stderr)
        for size in (SMALL, LARGE):
            record(label, name, size, fn)
    threads = thread_scaling(functions["crc32.iscsi"], data[MIB], THREAD_COUNTS[:2] if quick else THREAD_COUNTS)

    result = {"environment": env, "label": label, "measurements": measurements,
              "threads": {"algorithm": "crc32.iscsi", "size": MIB, "rows": threads}}
    if args.json:
        path = args.json
        if path == "auto":
            slug = re.sub(r"[^a-z0-9]+", "-", env["cpu"]["model"].lower()).strip("-")
            path = os.path.join(os.path.dirname(__file__), "results", f"{slug}-{env['python'].split()[0].lower()}{env['python'].split()[1]}-fastcrc-{env['fastcrc']}.json")
        with open(path, "w") as f:
            json.dump(result, f, indent=1)
        print(f"wrote {path}", file=sys.stderr)
    print(render([result]))


# --------------------------------------------------------------------------- report

def fmt_size(n):
    for unit, div in (("MiB", MIB), ("KiB", KIB)):
        if n >= div and n % div == 0:
            return f"{n // div} {unit}"
    return f"{n} B"


def fmt_ns(ns):
    return f"{ns:,.0f} ns" if ns < 10_000 else f"{ns / 1000:,.1f} µs" if ns < 1e7 else f"{ns / 1e6:,.2f} ms"


def fmt_gbps(g):
    return f"{g:.2f}" if g < 10 else f"{g:.1f}"


def table(header, rows, align=None):
    align = align or ["---"] + ["---:"] * (len(header) - 1)
    out = ["| " + " | ".join(header) + " |", "| " + " | ".join(align) + " |"]
    out += ["| " + " | ".join(str(c) for c in row) + " |" for row in rows]
    return "\n".join(out)


def render(results):
    results = sorted(results, key=lambda r: r["environment"]["timestamp"])
    latest = results[-1]
    env = latest["environment"]
    def version_key(label):
        return tuple(int(p) if p.isdigit() else p for p in re.split(r"[.\-]", label.split()[1]))

    labels = sorted({r["label"] for r in results}, key=version_key)  # oldest fastcrc first
    by_key = {}
    for r in results:
        for m in r["measurements"]:
            by_key[(m["library"], m["algorithm"], m["size"])] = m
    def get(lib, alg, size):
        return by_key.get((lib, alg, size))

    out = ["# fastcrc benchmarks", ""]
    out += ["Generated by `benchmarks/run.py`; raw measurements are in `benchmarks/results/`.", ""]
    out += ["## Environment", ""]
    cpu = env["cpu"]
    rows = [("CPU", cpu["model"]), ("SIMD extensions used by fastcrc", ", ".join(cpu["simd"]) or "none detected"),
            ("Logical CPUs", cpu["logical_cpus"]), ("OS", env["os"]), ("Python", env["python"])]
    if "governor" in cpu:
        rows.append(("CPU frequency governor", cpu["governor"]))
    rows.append(("fastcrc", ", ".join(l.split()[1] for l in labels)))
    rows.append(("Date", env["timestamp"][:10]))
    out += [table(["Property", "Value"], rows, ["---", "---"]), ""]
    out += ["## Methodology", "",
            f"Each figure is the fastest of {REPEATS} samples, each sample a loop of enough calls to last at least "
            f"{SAMPLE_SECONDS * 1000:.0f} ms, after one warm-up sample; the garbage collector is disabled while timing. "
            "Per-call latency includes the Python call overhead, so it is the time an application actually pays. "
            "Throughput is bytes / time with 1 GB = 10^9 bytes. Payloads come from `os.urandom`; CRC speed does "
            "not depend on the data. Single-threaded unless stated otherwise, with other cores idle.", ""]

    # --- profile tables
    new = labels[-1]
    sizes = sorted({m["size"] for r in results for m in r["measurements"] if m["library"] == new and m["algorithm"] in PROFILE})
    out += [f"## {new}: latency and throughput by input size", ""]
    hdr = ["Input"] + PROFILE
    out += ["Per-call latency:", "", table(hdr, [[fmt_size(s)] + [fmt_ns(get(new, a, s)["ns"]) if get(new, a, s) else "" for a in PROFILE] for s in sizes]), ""]
    out += ["Throughput (GB/s):", "", table(hdr, [[fmt_size(s)] + [fmt_gbps(get(new, a, s)["gbps"]) if get(new, a, s) else "" for a in PROFILE] for s in sizes]), ""]
    if len(labels) > 1:
        old = labels[0]
        out += [f"Speed-up of {new} over {old} (ratio of per-call times):", "",
                table(hdr, [[fmt_size(s)] + [f"{get(old, a, s)['ns'] / get(new, a, s)['ns']:.1f}×" if get(old, a, s) and get(new, a, s) else "" for a in PROFILE] for s in sizes]), ""]

    # --- every algorithm
    out += [f"## Every algorithm at {fmt_size(SMALL)} and {fmt_size(LARGE)}", ""]
    if len(labels) > 1:
        hdr = ["Function"] + [f"{fmt_size(SMALL)}, {l.split()[1]}" for l in labels] + [f"{fmt_size(LARGE)} GB/s, {l.split()[1]}" for l in labels]
    else:
        hdr = ["Function", f"{fmt_size(SMALL)}", f"{fmt_size(LARGE)} GB/s"]
    for module in ("crc8", "crc16", "crc32", "crc64"):
        algs = sorted({m["algorithm"] for r in results for m in r["measurements"] if m["algorithm"].startswith(module + ".") and m["library"] == new})
        rows = []
        for a in algs:
            row = [f"`{a}`"]
            row += [fmt_ns(get(l, a, SMALL)["ns"]) if get(l, a, SMALL) else "" for l in labels]
            row += [fmt_gbps(get(l, a, LARGE)["gbps"]) if get(l, a, LARGE) else "" for l in labels]
            rows.append(row)
        out += [f"### {module}", "", table(hdr, rows), ""]

    # --- threads
    th = latest.get("threads")
    if th:
        out += ["## Multi-threaded scaling", "",
                f"Aggregate throughput of `{th['algorithm']}` on {fmt_size(th['size'])} inputs with N Python threads. "
                "fastcrc releases the GIL for inputs of 16 KiB and more, so threads scale until memory bandwidth "
                "or the number of physical cores limits them.", "",
                table(["Threads", "GB/s", "Scaling"], [[r["threads"], fmt_gbps(r["gbps"]), f"{r['gbps'] / th['rows'][0]['gbps']:.1f}×"] for r in th["rows"]]), ""]
    return "\n".join(out)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command")
    p_run = sub.add_parser("run", help="measure the installed fastcrc")
    p_run.add_argument("--json", help="write raw results to PATH, or 'auto' for benchmarks/results/<machine>-fastcrc-<version>.json")
    p_run.add_argument("--quick", action="store_true", help="fewer sizes and repeats, for a smoke test")
    p_report = sub.add_parser("report", help="render stored results as Markdown")
    p_report.add_argument("files", nargs="+")
    args = parser.parse_args()
    if args.command == "report":
        print(render([json.load(open(f)) for f in args.files]))
    else:
        if args.command is None:
            args.json, args.quick = None, False
        run(args)


if __name__ == "__main__":
    main()
