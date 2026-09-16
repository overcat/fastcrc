"""
Every function accepts any bytes-like object through the buffer protocol and treats it as raw
bytes, the way ``zlib.crc32`` does.
"""
import array
import mmap
import os
import unittest
import zlib

from fastcrc import crc16, crc32, crc64

from tests.catalogue import public_functions


class TestBufferProtocol(unittest.TestCase):
    # Above the 16 KiB threshold, so the buffer is borrowed while the GIL is released.
    data = bytes(range(256)) * 80

    def test_all_functions_accept_bytearray_and_memoryview(self):
        for name, fn in public_functions().items():
            with self.subTest(function=name):
                expected = fn(self.data)
                self.assertEqual(expected, fn(bytearray(self.data)))
                self.assertEqual(expected, fn(memoryview(self.data)))
                view = memoryview(self.data)
                self.assertEqual(expected, fn(view[5000:], fn(view[:5000])))

    def test_buffer_types(self):
        iscsi = crc32.iscsi
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
        self.assertEqual(zlib.crc32(bytearray(self.data)), crc32.iso_hdlc(bytearray(self.data)))

    def test_rejected_inputs(self):
        for value in ("text", None, 5, [1, 2], 1.5):
            with self.subTest(value=value), self.assertRaises(TypeError):
                crc16.xmodem(value)
        with self.assertRaises(BufferError):
            crc16.xmodem(memoryview(self.data)[::2])

    def test_export_released_and_mutation_visible(self):
        # The buffer export only lasts for the call: the bytearray can be modified and resized
        # again afterwards, and changes are picked up.
        buffer = bytearray(os.urandom(1 << 20))
        before = crc64.xz(buffer)
        buffer[12345] ^= 0xFF
        self.assertNotEqual(before, crc64.xz(buffer))
        buffer.extend(b"resizable again once the buffer export is released")
        self.assertEqual(crc64.xz(bytes(buffer)), crc64.xz(buffer))
