=======
fastcrc
=======

.. image:: https://img.shields.io/github/actions/workflow/status/overcat/fastcrc/ci.yml?branch=main
    :alt: GitHub Workflow Status
    :target: https://github.com/overcat/fastcrc/actions

.. image:: https://img.shields.io/readthedocs/fastcrc.svg?style=flat&maxAge=1800
    :alt: Read the Docs
    :target: https://fastcrc.readthedocs.io/

.. image:: https://static.pepy.tech/personalized-badge/fastcrc?period=total&units=abbreviation&left_color=grey&right_color=brightgreen&left_text=Downloads
    :alt: PyPI - Downloads
    :target: https://pypi.python.org/pypi/fastcrc

.. image:: https://img.shields.io/pypi/v/fastcrc.svg?style=flat&maxAge=1800
    :alt: PyPI
    :target: https://pypi.python.org/pypi/fastcrc

A hyper-fast Python module for computing CRC(8, 16, 32, 64) checksum.


Installation
============

fastcrc needs Python 3.8 or newer. Prebuilt wheels are available for recent CPython versions on
Linux, macOS and Windows, so on most machines this is all it takes:

.. code-block:: text

   pip install fastcrc

If pip can't find a wheel for your interpreter it falls back to building from source, which
needs a Rust toolchain (1.89 or newer).

Usage
=====

.. code:: python

   from fastcrc import crc8, crc16, crc32, crc64

   data = b"123456789"
   print(f"crc8 checksum with cdma2000 algorithm: {crc8.cdma2000(data)}")
   print(f"crc16 checksum with xmodem algorithm: {crc16.xmodem(data)}")
   print(f"crc32 checksum with aixm algorithm: {crc32.aixm(data)}")
   print(f"crc64 checksum with ecma_182 algorithm: {crc64.ecma_182(data)}")
   print(f"crc16 checksum with xmodem algorithm (with initial data): {crc16.xmodem(b'56789', crc16.xmodem(b'1234'))}")

   # Any bytes-like object works without copying, e.g. a slice of a larger buffer.
   buffer = bytearray(b"header:123456789")
   print(f"crc32 checksum of a memoryview slice: {crc32.iscsi(memoryview(buffer)[7:])}")

Notes
=====

* ``data`` may be any object that supports the buffer protocol (``bytes``, ``bytearray``,
  ``memoryview``, ``array``, ``mmap``, NumPy arrays, ...). It is read in place without copying,
  so do not modify it from another thread while its checksum is being computed.
* Inputs of 16 KiB and more are processed with the GIL released, so threads can compute
  checksums in parallel. The free-threaded build of CPython is supported.

Performance
===========

CRC-16, CRC-32 and CRC-64 use SIMD carry-less multiplication (PCLMULQDQ/VPCLMULQDQ on x86,
PMULL on aarch64) with a table-based fallback elsewhere; CRC-8 uses slice-by-16 tables. The
best method for the CPU is picked at run time, so the wheels run everywhere.

Single-threaded throughput on an AMD Ryzen 7 9700X (Zen 5) with CPython 3.14, in GB/s:

===========  ============  ==============  ============  ==========  ==========
Input        crc32.iscsi   crc32.iso_hdlc  crc16.xmodem  crc64.xz    crc8.smbus
===========  ============  ==============  ============  ==========  ==========
64 B         2.3           1.5             1.5           1.3         2.4
1 KiB        21.5          21.5            22.8          20.9        8.2
1 MiB        86.8          87.0            86.4          86.6        9.4
===========  ============  ==============  ============  ==========  ==========

Full tables for every algorithm, per-call latencies, multi-threaded scaling and the harness
to reproduce them are in `benchmarks/README.md`_.

Documentation
=============
fastcrc's documentation can be found at https://fastcrc.readthedocs.io

License
=======

fastcrc is licensed under `MIT License`_.

Thanks
======

fastcrc is made possible by `crc-fast`_.

.. _MIT License: ./LICENSE
.. _crc-fast: https://github.com/awesomized/crc-fast-rust
.. _benchmarks/README.md: https://github.com/overcat/fastcrc/blob/main/benchmarks/README.md
