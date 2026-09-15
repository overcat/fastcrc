"""
The routines of the AUTOSAR CRC library (AUTOSAR_SWS_CRCLibrary) map onto
existing algorithms. The specification lists the same seven test inputs with
the expected result for every routine; check them all.
"""
import unittest

from fastcrc import crc8, crc16, crc32, crc64

INPUTS = [
    bytes.fromhex(h)
    for h in ("00000000", "F20183", "0FAA0055", "00FF5511", "332255AABBCCDDEEFF", "926B55", "FFFFFFFF")
]

# AUTOSAR routine -> (fastcrc function, expected results for INPUTS)
ROUTINES = {
    "Crc_CalculateCRC8 (SAE J1850)": (crc8.sae_j1850, [0x59, 0x37, 0x79, 0xB8, 0xCB, 0x8C, 0x74]),
    "Crc_CalculateCRC8H2F": (crc8.autosar, [0x12, 0xC2, 0xC6, 0x77, 0x11, 0x33, 0x6C]),
    "Crc_CalculateCRC16 (CCITT-FALSE)": (crc16.autosar, [0x84C0, 0xD374, 0x2023, 0xB8F9, 0xF53F, 0x0745, 0x1D0F]),
    "Crc_CalculateCRC16ARC": (crc16.arc, [0x0000, 0xC2E1, 0x0BE3, 0x6CCF, 0xAE98, 0xE24E, 0x9401]),
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


class TestAutosarVectors(unittest.TestCase):
    def test_specification_vectors(self):
        for routine, (fn, expected) in ROUTINES.items():
            for data, value in zip(INPUTS, expected):
                with self.subTest(routine=routine, data=data.hex()):
                    self.assertEqual(value, fn(data))

    def test_crc16_autosar_is_ibm_3740(self):
        for data in INPUTS + [b"123456789", bytes(range(256))]:
            self.assertEqual(crc16.ibm_3740(data), crc16.autosar(data))
        self.assertEqual(0x29B1, crc16.autosar(b"123456789"))


if __name__ == "__main__":
    unittest.main()
