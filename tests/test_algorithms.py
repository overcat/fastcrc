"""
Every algorithm computes the right checksum: the catalogue check value for ``b"123456789"``,
the same result as the bit-by-bit reference implementation on inputs of every size class the
extension treats differently, the same as the standard library where it has the algorithm,
the published test vectors of the AUTOSAR CRC library for the routines it defines, and the
same as the vendor's reference function for the TMS570 CRC module. Continuing a checksum
through ``initial`` must give the checksum of the whole input.
"""
import binascii
import random
import unittest
import zlib

from fastcrc import crc8, crc16, crc32, crc64

from tests.catalogue import CATALOGUE, CHECK_INPUT, public_functions, reference_crc

# Sizes that reach every code path: the byte-wise table for inputs under 8 bytes, the SIMD
# kernels' block sizes and their remainders, and the 16 KiB threshold from which the GIL is
# released.
SIZES = [
    0, 1, 7, 8, 9, 15, 16, 17, 63, 64, 65, 127, 128, 255, 256, 1023, 1024, 4096,
    16383, 16384, 16385,
]


def random_bytes(rng, size):
    return rng.getrandbits(8 * size).to_bytes(size, "little") if size else b""


class TestCatalogue(unittest.TestCase):
    """The catalogue is complete, and the reference implementation agrees with it."""

    def test_lists_every_function_once(self):
        listed = [str(algorithm) for algorithm in CATALOGUE]
        self.assertEqual(len(listed), len(set(listed)))
        self.assertEqual(set(public_functions()), set(listed))

    def test_reference_reproduces_check_values(self):
        for algorithm in CATALOGUE:
            with self.subTest(algorithm=str(algorithm)):
                self.assertEqual(algorithm.check, reference_crc(algorithm, CHECK_INPUT))


class TestCheckValues(unittest.TestCase):
    def test_check_value(self):
        for algorithm in CATALOGUE:
            with self.subTest(algorithm=str(algorithm)):
                self.assertEqual(algorithm.check, algorithm.function(CHECK_INPUT))

    def test_initial_continues_a_checksum(self):
        for algorithm in CATALOGUE:
            fn = algorithm.function
            with self.subTest(algorithm=str(algorithm)):
                self.assertEqual(algorithm.check, fn(b"56789", fn(b"1234")))
                checksum = fn(b"")
                for i in range(len(CHECK_INPUT)):
                    checksum = fn(CHECK_INPUT[i : i + 1], checksum)
                self.assertEqual(algorithm.check, checksum)


class TestAgainstReference(unittest.TestCase):
    def test_all_sizes(self):
        rng = random.Random(0x5EED)
        inputs = [random_bytes(rng, size) for size in SIZES]
        for algorithm in CATALOGUE:
            fn = algorithm.function
            for data in inputs:
                with self.subTest(algorithm=str(algorithm), size=len(data)):
                    expected = reference_crc(algorithm, data)
                    self.assertEqual(expected, fn(data))
                    for split in (0, rng.randint(0, len(data)), len(data)):
                        self.assertEqual(expected, fn(data[split:], fn(data[:split])))


class TestAgainstStandardLibrary(unittest.TestCase):
    """
    ``zlib.crc32`` is CRC-32/ISO-HDLC and ``binascii.crc_hqx`` is CRC-16/XMODEM, and both
    take a previous checksum to continue from. They are fast, so the inputs can be far larger
    than the reference implementation handles, and ``initial`` must interoperate with them.
    """

    SIZES = [0, 1, 4095, 65536, 65537, 1 << 20, (1 << 20) + 13]

    def compare(self, fn, stdlib):
        rng = random.Random(0xC0FFEE)
        for size in self.SIZES:
            data = random_bytes(rng, size)
            split = rng.randint(0, size)
            with self.subTest(size=size):
                expected = stdlib(data, 0)
                self.assertEqual(expected, fn(data))
                self.assertEqual(expected, fn(data[split:], stdlib(data[:split], 0)))
                self.assertEqual(expected, stdlib(data[split:], fn(data[:split])))

    def test_iso_hdlc_is_zlib_crc32(self):
        self.compare(crc32.iso_hdlc, zlib.crc32)

    def test_xmodem_is_binascii_crc_hqx(self):
        self.compare(crc16.xmodem, binascii.crc_hqx)


class TestAutosarVectors(unittest.TestCase):
    """
    The routines of the AUTOSAR CRC library (AUTOSAR_SWS_CRCLibrary) map onto existing
    algorithms. The specification lists the same seven test inputs with the expected result
    for every routine; check them all.
    """

    INPUTS = [
        bytes.fromhex(h)
        for h in (
            "00000000",
            "F20183",
            "0FAA0055",
            "00FF5511",
            "332255AABBCCDDEEFF",
            "926B55",
            "FFFFFFFF",
        )
    ]

    # AUTOSAR routine -> (fastcrc function, expected results for INPUTS)
    ROUTINES = {
        "Crc_CalculateCRC8 (SAE J1850)": (
            crc8.sae_j1850,
            [0x59, 0x37, 0x79, 0xB8, 0xCB, 0x8C, 0x74],
        ),
        "Crc_CalculateCRC8H2F": (
            crc8.autosar,
            [0x12, 0xC2, 0xC6, 0x77, 0x11, 0x33, 0x6C],
        ),
        "Crc_CalculateCRC16 (CCITT-FALSE)": (
            crc16.autosar,
            [0x84C0, 0xD374, 0x2023, 0xB8F9, 0xF53F, 0x0745, 0x1D0F],
        ),
        "Crc_CalculateCRC16ARC": (
            crc16.arc,
            [0x0000, 0xC2E1, 0x0BE3, 0x6CCF, 0xAE98, 0xE24E, 0x9401],
        ),
        "Crc_CalculateCRC32 (IEEE 802.3)": (
            crc32.iso_hdlc,
            [0x2144DF1C, 0x24AB9D77, 0xB6C9B287, 0x32A06212, 0xB0AE863D, 0x9CDEA29B, 0xFFFFFFFF],
        ),
        "Crc_CalculateCRC32P4": (
            crc32.autosar,
            [0x6FB32240, 0x4F721A25, 0x20662DF8, 0x9BD7996E, 0xA65A343D, 0xEE688A78, 0xFFFFFFFF],
        ),
        "Crc_CalculateCRC64": (
            crc64.xz,
            [
                0xF4A586351E1B9F4B,
                0x319C27668164F1C6,
                0x54C5D0F7667C1575,
                0xA63822BE7E0704E6,
                0x701ECEB219A8E5D5,
                0x5FAA96A9B59F3E4E,
                0xFFFFFFFF00000000,
            ],
        ),
    }

    def test_specification_vectors(self):
        for routine, (fn, expected) in self.ROUTINES.items():
            for data, value in zip(self.INPUTS, expected):
                with self.subTest(routine=routine, data=data.hex()):
                    self.assertEqual(value, fn(data))

    def test_crc16_autosar_is_ibm_3740(self):
        for data in self.INPUTS + [CHECK_INPUT, bytes(range(256))]:
            self.assertEqual(crc16.ibm_3740(data), crc16.autosar(data))


class TestTms570Reference(unittest.TestCase):
    """
    ``crc64.tms570_iso`` is the algorithm of the CRC module of TI's Hercules microcontrollers,
    defined by the vendor's C function ``crc_update_word`` in section 3.3 of "Using the CRC
    Module on Hercules-Based Microcontrollers" (SPNA235,
    https://www.ti.com/lit/an/spna235/spna235.pdf), transcribed below as is. It consumes 64-bit
    words most significant bit first, so a byte string corresponds to its words in big-endian
    order, and the previous output or seed it takes is fastcrc's ``initial``.
    """

    @staticmethod
    def crc_update_word(crc64, data):
        for i in range(63, -1, -1):
            next_crc = ((crc64 >> 63) ^ (data >> i)) & 1
            for j in range(1, 64):
                if j in (1, 3, 4):
                    bit = ((crc64 >> (j - 1)) ^ (crc64 >> 63) ^ (data >> i)) & 1
                else:
                    bit = (crc64 >> (j - 1)) & 1
                next_crc |= bit << j
            crc64 = next_crc
        return crc64

    def test_whole_words(self):
        rng = random.Random(0x7E5570)
        for words in (1, 2, 3, 8, 32):
            data = random_bytes(rng, 8 * words)
            seed = rng.getrandbits(64)
            for initial in (None, seed):
                with self.subTest(words=words, initial=initial):
                    crc = 0 if initial is None else initial
                    for offset in range(0, len(data), 8):
                        word = int.from_bytes(data[offset : offset + 8], "big")
                        crc = self.crc_update_word(crc, word)
                    self.assertEqual(crc, crc64.tms570_iso(data, initial))
