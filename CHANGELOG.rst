==========
Change Log
==========

This document records all notable changes to `fastcrc <https://github.com/overcat/fastcrc/>`_.

Unreleased
----------
* chore: upgrade PyO3 from 0.26 to 0.29.2 and refresh the Rust dependency lock file.
* feat: wheels are now also built for Windows on ARM64.
* breaking: Python 3.7, Python 3.8 and PyPy 3.9/3.10 are no longer supported: PyO3 0.29 requires CPython 3.8+ and PyPy 3.11+, the manylinux build images no longer ship Python 3.8, and the 3.7 drop was announced in 0.4.0; ``requires-python`` is now ``>=3.9`` and no wheels are built for those interpreters.
* note: the ``TypeError`` raised for an invalid ``initial`` no longer carries the ``argument 'initial':`` prefix, following PyO3's new error reporting; the exception type is unchanged.

0.4.1 (September 15, 2026)
--------------------------
* feat: add ``fastcrc.crc16.autosar``, the CRC16 routine of the AUTOSAR CRC library (CRC-16/CCITT-FALSE); it is an alias of ``crc16.ibm_3740``. (`#9 <https://github.com/overcat/fastcrc/issues/9>`_)

0.4.0 (September 15, 2026)
--------------------------
* perf: CRC-16, CRC-32 and CRC-64 checksums are computed with SIMD carry-less multiplication (PCLMULQDQ/VPCLMULQDQ on x86, PMULL on aarch64, table-based fallback elsewhere) via the `crc-fast <https://crates.io/crates/crc-fast>`_ crate, and CRC-8 uses slice-by-16 tables; large inputs are over 100x faster on CPUs with VPCLMULQDQ, results are unchanged.
* perf: the GIL is released while computing checksums of inputs of 16 KiB or more.
* perf: release builds use fat LTO, reducing per-call overhead for small inputs.
* perf: the functions in ``fastcrc.crc8``/``crc16``/``crc32``/``crc64`` are now the extension functions themselves instead of Python wrappers around them, saving about 15 ns per call; names, positional and keyword calling and results are unchanged, type hints moved to ``.pyi`` stubs, and the note below lists what changes about the function objects.
* perf: inputs shorter than 8 bytes are computed with a lookup table, avoiding the SIMD setup cost.
* feat: every function accepts any bytes-like object (``bytearray``, ``memoryview``, ``array``, ``mmap``, NumPy arrays, ...) through the buffer protocol, treated as raw bytes like ``zlib.crc32`` does; ``bytes`` keeps its zero-copy fast path, and as with ``hashlib`` a mutable buffer must not be modified by another thread while its checksum is computed. Unsupported objects raise the standard ``a bytes-like object is required`` TypeError and non-contiguous buffers raise BufferError.
* chore: the ``crc`` crate is no longer a dependency; building from source requires Rust 1.89 or newer.
* note: the public functions are now built-in functions rather than Python functions: ``inspect.isfunction`` is false, they have no ``__annotations__``, ``__code__`` or ``__dict__`` (attributes cannot be set on them), they do not bind as methods when stored on a class, and they do not appear as frames in tracebacks or ``sys.settrace``; the private, undocumented ``fastcrc.fastcrc.crc_32_iscsi``-style names and ``fastcrc.crc32._crc_32_iscsi``-style aliases no longer exist.
* deprecation: this is the last release series to support Python 3.7; fastcrc 0.5.0 will drop it.

0.3.6 (May 06, 2026)
--------------------
* feat: add `fastcrc.crc64.tms570_iso` for the TI Hercules TMS570 CRC-64-ISO algorithm. (`#30 <https://github.com/overcat/fastcrc/pull/30>`_)

0.3.5 (January 01, 2026)
------------------------
* feat: add `riscv64gc-unknown-linux-gnu` build target. (`#27 <https://github.com/overcat/fastcrc/pull/27>`_)

0.3.4 (October 26, 2025)
------------------------
* chore: mark module as gil-free. (`#17 <https://github.com/overcat/fastcrc/pull/17>`_)

0.3.3 (October 09, 2025)
------------------------
* chore: bump third-party dependencies.

0.3.1 (October 23, 2024)
------------------------
* chore: add wheels for Python 3.13, pypy 3.8, pypy 3.9 and pypy 3.10.

0.3.0 (January 2, 2024)
-----------------------
* feat: add support for 8 bit CRCs. (`#5 <https://github.com/overcat/fastcrc/pull/5>`_)
* chore: drop support for Python 3.6. (`#6 <https://github.com/overcat/fastcrc/pull/6>`_)

0.2.1 (September 15, 2022)
--------------------------
* feat: add `fastcrc.crc16.ibm_refin` and `fastcrc.crc32.reversed_reciprocal_refin`, these are two experimental functions that may be removed in the future.
* chore: build wheels for more platforms.
* docs: improve documentation.

0.2.0 (June 19, 2022)
---------------------
* Add initial value optional parameter to all CRC functions. (`#1 <https://github.com/overcat/fastcrc/pull/1>`_)

0.1.1 (May 23, 2021)
---------------------
* Correct the project information.

0.1.0 (May 23, 2021)
---------------------
* First release.
