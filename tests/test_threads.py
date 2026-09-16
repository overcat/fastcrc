"""
Checksums can be computed from several threads at once, and on free-threaded builds importing
fastcrc leaves the GIL disabled.
"""
import os
import sys
import sysconfig
import threading
import unittest

from fastcrc import crc32, crc64


class TestThreads(unittest.TestCase):
    def test_concurrent_calls_agree(self):
        # Inputs above 16 KiB are computed with the GIL released; bytes and memoryview take the
        # two input paths.
        data = os.urandom(1 << 20)
        expected = (crc32.iscsi(data), crc64.xz(memoryview(data)))
        results = []

        def work():
            for _ in range(20):
                results.append((crc32.iscsi(data), crc64.xz(memoryview(data))))

        threads = [threading.Thread(target=work) for _ in range(8)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        self.assertEqual([expected] * 160, results)

    # `sys.flags.gil` is 1 when the GIL was forced on with `-X gil=1` or `PYTHON_GIL=1`.
    @unittest.skipUnless(
        sysconfig.get_config_var("Py_GIL_DISABLED") and getattr(sys.flags, "gil", None) != 1,
        "needs a free-threaded build started with the GIL disabled",
    )
    def test_import_leaves_the_gil_disabled(self):
        # fastcrc declares itself safe for free threading; had it not, CPython would have
        # re-enabled the GIL when the extension was imported.
        self.assertFalse(sys._is_gil_enabled())
