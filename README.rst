=======
fastcrc
=======

.. image:: https://img.shields.io/readthedocs/fastcrc.svg?style=flat&maxAge=1800
    :alt: Read the Docs
    :target: https://fastcrc.readthedocs.io/

.. image:: https://img.shields.io/pypi/v/fastcrc.svg?style=flat&maxAge=1800
    :alt: PyPI
    :target: https://pypi.python.org/pypi/fastcrc

.. image:: https://img.shields.io/badge/python-%3E%3D3.7-blue?style=flat
    :alt: Python - Version
    :target: https://pypi.python.org/pypi/fastcrc

A hyper-fast Python module for computing CRC(8, 16, 32, 64) checksum.


Installation
============

.. code-block:: text

   pip install fastcrc

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
  ``memoryview``, ``array``, ``mmap``, NumPy arrays, ...); it is read as raw bytes without copying.
  As with ``hashlib``, a mutable buffer must not be modified by another thread while its checksum
  is being computed.
* Pass a previously returned checksum as ``initial`` to continue it over more data.
* The GIL is released while inputs of 16 KiB or more are processed, and the free-threaded
  build of CPython is supported.
* The package ships type stubs (``py.typed``).

Performance
===========

CRC-16, CRC-32 and CRC-64 use SIMD carry-less multiplication (PCLMULQDQ/VPCLMULQDQ on x86,
PMULL on aarch64) with a table-based fallback elsewhere; CRC-8 uses slice-by-16 tables. The
best method for the CPU is picked at run time, so the wheels run everywhere.

Single-threaded throughput on an AMD Ryzen 7 9700X (Zen 5) with CPython 3.14, in GB/s:

===========  ============  ==============  ============  ==========  ==========
Input        crc32.iscsi   crc32.iso_hdlc  crc16.xmodem  crc64.xz    crc8.smbus
===========  ============  ==============  ============  ==========  ==========
64 B         2.4           1.6             1.6           1.3         2.6
1 KiB        21.9          24.0            23.6          21.9        8.3
1 MiB        86.9          86.8            86.6          86.3        9.2
===========  ============  ==============  ============  ==========  ==========

For CRC-32/ISO-HDLC that is about ten times ``zlib.crc32``; fastcrc 0.3.x topped out at
about 0.7 GB/s. Full tables for every algorithm, per-call latencies, comparisons with
``crc32c``, ``google-crc32c``, ``crc32c-rs`` and ``crcmod``, and the harness to reproduce
them are in `benchmarks/README.md`_.

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
