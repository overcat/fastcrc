"""
Cross-check every algorithm against a bit-by-bit pure-Python reference implementation
of the Rocksoft model, on inputs large enough to exercise the SIMD and table code
paths (the check value "123456789" only covers the short-input path).
"""
import random
import unittest

import fastcrc

# (module, function, width, poly, init, refin, refout, xorout)
PARAMS = [
    ("crc8", "autosar", 8, 0x2f, 0xff, False, False, 0xff),
    ("crc8", "bluetooth", 8, 0xa7, 0x00, True, True, 0x00),
    ("crc8", "cdma2000", 8, 0x9b, 0xff, False, False, 0x00),
    ("crc8", "darc", 8, 0x39, 0x00, True, True, 0x00),
    ("crc8", "dvb_s2", 8, 0xd5, 0x00, False, False, 0x00),
    ("crc8", "gsm_a", 8, 0x1d, 0x00, False, False, 0x00),
    ("crc8", "gsm_b", 8, 0x49, 0x00, False, False, 0xff),
    ("crc8", "i_432_1", 8, 0x07, 0x00, False, False, 0x55),
    ("crc8", "i_code", 8, 0x1d, 0xfd, False, False, 0x00),
    ("crc8", "lte", 8, 0x9b, 0x00, False, False, 0x00),
    ("crc8", "maxim_dow", 8, 0x31, 0x00, True, True, 0x00),
    ("crc8", "mifare_mad", 8, 0x1d, 0xc7, False, False, 0x00),
    ("crc8", "nrsc_5", 8, 0x31, 0xff, False, False, 0x00),
    ("crc8", "opensafety", 8, 0x2f, 0x00, False, False, 0x00),
    ("crc8", "rohc", 8, 0x07, 0xff, True, True, 0x00),
    ("crc8", "sae_j1850", 8, 0x1d, 0xff, False, False, 0xff),
    ("crc8", "smbus", 8, 0x07, 0x00, False, False, 0x00),
    ("crc8", "tech_3250", 8, 0x1d, 0xff, True, True, 0x00),
    ("crc8", "wcdma", 8, 0x9b, 0x00, True, True, 0x00),
    ("crc16", "arc", 16, 0x8005, 0x0000, True, True, 0x0000),
    ("crc16", "autosar", 16, 0x1021, 0xffff, False, False, 0x0000),
    ("crc16", "cdma2000", 16, 0xc867, 0xffff, False, False, 0x0000),
    ("crc16", "cms", 16, 0x8005, 0xffff, False, False, 0x0000),
    ("crc16", "dds_110", 16, 0x8005, 0x800d, False, False, 0x0000),
    ("crc16", "dect_r", 16, 0x0589, 0x0000, False, False, 0x0001),
    ("crc16", "dect_x", 16, 0x0589, 0x0000, False, False, 0x0000),
    ("crc16", "dnp", 16, 0x3d65, 0x0000, True, True, 0xffff),
    ("crc16", "en_13757", 16, 0x3d65, 0x0000, False, False, 0xffff),
    ("crc16", "genibus", 16, 0x1021, 0xffff, False, False, 0xffff),
    ("crc16", "gsm", 16, 0x1021, 0x0000, False, False, 0xffff),
    ("crc16", "ibm_3740", 16, 0x1021, 0xffff, False, False, 0x0000),
    ("crc16", "ibm_sdlc", 16, 0x1021, 0xffff, True, True, 0xffff),
    ("crc16", "iso_iec_14443_3_a", 16, 0x1021, 0xc6c6, True, True, 0x0000),
    ("crc16", "kermit", 16, 0x1021, 0x0000, True, True, 0x0000),
    ("crc16", "lj1200", 16, 0x6f63, 0x0000, False, False, 0x0000),
    ("crc16", "maxim_dow", 16, 0x8005, 0x0000, True, True, 0xffff),
    ("crc16", "mcrf4xx", 16, 0x1021, 0xffff, True, True, 0x0000),
    ("crc16", "modbus", 16, 0x8005, 0xffff, True, True, 0x0000),
    ("crc16", "nrsc_5", 16, 0x080b, 0xffff, True, True, 0x0000),
    ("crc16", "opensafety_a", 16, 0x5935, 0x0000, False, False, 0x0000),
    ("crc16", "opensafety_b", 16, 0x755b, 0x0000, False, False, 0x0000),
    ("crc16", "profibus", 16, 0x1dcf, 0xffff, False, False, 0xffff),
    ("crc16", "riello", 16, 0x1021, 0xb2aa, True, True, 0x0000),
    ("crc16", "spi_fujitsu", 16, 0x1021, 0x1d0f, False, False, 0x0000),
    ("crc16", "t10_dif", 16, 0x8bb7, 0x0000, False, False, 0x0000),
    ("crc16", "teledisk", 16, 0xa097, 0x0000, False, False, 0x0000),
    ("crc16", "tms37157", 16, 0x1021, 0x89ec, True, True, 0x0000),
    ("crc16", "umts", 16, 0x8005, 0x0000, False, False, 0x0000),
    ("crc16", "usb", 16, 0x8005, 0xffff, True, True, 0xffff),
    ("crc16", "xmodem", 16, 0x1021, 0x0000, False, False, 0x0000),
    ("crc32", "aixm", 32, 0x814141ab, 0x00000000, False, False, 0x00000000),
    ("crc32", "autosar", 32, 0xf4acfb13, 0xffffffff, True, True, 0xffffffff),
    ("crc32", "base91_d", 32, 0xa833982b, 0xffffffff, True, True, 0xffffffff),
    ("crc32", "bzip2", 32, 0x04c11db7, 0xffffffff, False, False, 0xffffffff),
    ("crc32", "cd_rom_edc", 32, 0x8001801b, 0x00000000, True, True, 0x00000000),
    ("crc32", "cksum", 32, 0x04c11db7, 0x00000000, False, False, 0xffffffff),
    ("crc32", "iscsi", 32, 0x1edc6f41, 0xffffffff, True, True, 0xffffffff),
    ("crc32", "iso_hdlc", 32, 0x04c11db7, 0xffffffff, True, True, 0xffffffff),
    ("crc32", "jamcrc", 32, 0x04c11db7, 0xffffffff, True, True, 0x00000000),
    ("crc32", "mpeg_2", 32, 0x04c11db7, 0xffffffff, False, False, 0x00000000),
    ("crc32", "xfer", 32, 0x000000af, 0x00000000, False, False, 0x00000000),
    ("crc64", "ecma_182", 64, 0x42f0e1eba9ea3693, 0x0000000000000000, False, False, 0x0000000000000000),
    ("crc64", "go_iso", 64, 0x000000000000001b, 0xffffffffffffffff, True, True, 0xffffffffffffffff),
    ("crc64", "we", 64, 0x42f0e1eba9ea3693, 0xffffffffffffffff, False, False, 0xffffffffffffffff),
    ("crc64", "xz", 64, 0x42f0e1eba9ea3693, 0xffffffffffffffff, True, True, 0xffffffffffffffff),
    ("crc16", "ibm_refin", 16, 0x8005, 0x0000, True, False, 0x0000),
    ("crc32", "k_reversed_reciprocal_refin", 32, 0xba0dc66b, 0x00000000, True, False, 0x00000000),
    ("crc64", "tms570_iso", 64, 0x000000000000001b, 0x0000000000000000, False, False, 0x0000000000000000),
]

SIZES = [0, 1, 7, 8, 9, 15, 16, 17, 63, 64, 65, 127, 128, 255, 256, 1023, 1024, 4096, 20000]


def reference_crc(data, width, poly, init, refin, refout, xorout):
    mask = (1 << width) - 1
    top = 1 << (width - 1)
    crc = init
    for byte in data:
        if refin:
            byte = int(f"{byte:08b}"[::-1], 2)
        crc ^= byte << (width - 8)
        for _ in range(8):
            crc = ((crc << 1) ^ poly) if crc & top else (crc << 1)
            crc &= mask
    if refout:
        crc = int(f"{crc:0{width}b}"[::-1], 2)
    return crc ^ xorout


class TestAgainstReference(unittest.TestCase):
    def test_all_algorithms(self):
        rng = random.Random(0x5EED)
        inputs = [bytes(rng.getrandbits(8) for _ in range(n)) for n in SIZES]
        for module, name, width, poly, init, refin, refout, xorout in PARAMS:
            fn = getattr(getattr(fastcrc, module), name)
            for data in inputs:
                with self.subTest(algorithm=f"{module}.{name}", size=len(data)):
                    expected = reference_crc(data, width, poly, init, refin, refout, xorout)
                    self.assertEqual(expected, fn(data))
                    # Feeding the checksum of a prefix as `initial` must continue it.
                    split = rng.randint(0, len(data))
                    self.assertEqual(expected, fn(data[split:], fn(data[:split])))


if __name__ == "__main__":
    unittest.main()
