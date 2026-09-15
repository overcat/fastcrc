"""
Every function accepts any bytes-like object through the buffer protocol and
treats it as raw bytes, the way ``zlib.crc32`` does.
"""
import array
import mmap
import os
import unittest
import zlib

import fastcrc

MODULES = ("crc8", "crc16", "crc32", "crc64")


def functions():
    for name in MODULES:
        module = getattr(fastcrc, name)
        for attr in module.__all__:
            if not attr.startswith("algorithms_"):
                yield f"{name}.{attr}", getattr(module, attr)


class TestBufferProtocol(unittest.TestCase):
    data = bytes(range(256)) * 40  # 10240 bytes

    def test_all_functions_accept_bytearray_and_memoryview(self):
        for name, fn in functions():
            with self.subTest(function=name):
                expected = fn(self.data)
                self.assertEqual(expected, fn(bytearray(self.data)))
                self.assertEqual(expected, fn(memoryview(self.data)))
                self.assertEqual(expected, fn(memoryview(self.data)[5000:], fn(memoryview(self.data)[:5000])))

    def test_buffer_types(self):
        iscsi = fastcrc.crc32.iscsi
        expected = iscsi(self.data)
        self.assertEqual(expected, iscsi(memoryview(b"xx" + self.data + b"yy")[2:-2]))
        self.assertEqual(expected, iscsi(array.array("B", self.data)))
        self.assertEqual(expected, iscsi(memoryview(self.data).cast("I")))
        ints = array.array("i", range(1000))
        self.assertEqual(iscsi(ints.tobytes()), iscsi(ints))
        with mmap.mmap(-1, len(self.data)) as mapped:
            mapped.write(self.data)
            self.assertEqual(expected, iscsi(mapped))
        self.assertEqual(iscsi(b""), iscsi(bytearray()))
        self.assertEqual(iscsi(b""), iscsi(memoryview(b"")))
        self.assertEqual(zlib.crc32(bytearray(self.data)), fastcrc.crc32.iso_hdlc(bytearray(self.data)))

    def test_rejected_inputs(self):
        for value in ("text", None, 5, [1, 2], 1.5):
            with self.subTest(value=value), self.assertRaises(TypeError):
                fastcrc.crc16.xmodem(value)
        with self.assertRaises(BufferError):
            fastcrc.crc16.xmodem(memoryview(self.data)[::2])

    def test_export_released_and_mutation_visible(self):
        # The buffer export only lasts for the call: the bytearray can be
        # modified and resized again afterwards, and changes are picked up.
        buffer = bytearray(os.urandom(1 << 20))
        before = fastcrc.crc64.xz(buffer)
        buffer[12345] ^= 0xFF
        self.assertNotEqual(before, fastcrc.crc64.xz(buffer))
        buffer.extend(b"resizable again once the buffer export is released")
        self.assertEqual(fastcrc.crc64.xz(bytes(buffer)), fastcrc.crc64.xz(buffer))


if __name__ == "__main__":
    unittest.main()
