import unittest

from fastcrc import crc16, crc32, crc64

data = b"123456789"


class TestCrc16(unittest.TestCase):
    def test_arc(self):
        self.assertEqual(47933, crc16.arc(data))

    def test_cdma2000(self):
        self.assertEqual(19462, crc16.cdma2000(data))

    def test_cms(self):
        self.assertEqual(44775, crc16.cms(data))

    def test_dds_110(self):
        self.assertEqual(40655, crc16.dds_110(data))

    def test_dect_r(self):
        self.assertEqual(126, crc16.dect_r(data))

    def test_dect_x(self):
        self.assertEqual(127, crc16.dect_x(data))

    def test_dnp(self):
        self.assertEqual(60034, crc16.dnp(data))

    def test_en_13757(self):
        self.assertEqual(49847, crc16.en_13757(data))

    def test_genibus(self):
        self.assertEqual(54862, crc16.genibus(data))

    def test_gsm(self):
        self.assertEqual(52796, crc16.gsm(data))

    def test_ibm_3740(self):
        self.assertEqual(10673, crc16.ibm_3740(data))

    def test_ibm_sdlc(self):
        self.assertEqual(36974, crc16.ibm_sdlc(data))

    def test_iso_iec_14443_3_a(self):
        self.assertEqual(48901, crc16.iso_iec_14443_3_a(data))

    def test_kermit(self):
        self.assertEqual(8585, crc16.kermit(data))

    def test_lj1200(self):
        self.assertEqual(48628, crc16.lj1200(data))

    def test_maxim_dow(self):
        self.assertEqual(17602, crc16.maxim_dow(data))

    def test_mcrf4xx(self):
        self.assertEqual(28561, crc16.mcrf4xx(data))

    def test_modbus(self):
        self.assertEqual(19255, crc16.modbus(data))

    def test_nrsc_5(self):
        self.assertEqual(41062, crc16.nrsc_5(data))

    def test_opensafety_a(self):
        self.assertEqual(23864, crc16.opensafety_a(data))

    def test_opensafety_b(self):
        self.assertEqual(8446, crc16.opensafety_b(data))

    def test_profibus(self):
        self.assertEqual(43033, crc16.profibus(data))

    def test_riello(self):
        self.assertEqual(25552, crc16.riello(data))

    def test_spi_fujitsu(self):
        self.assertEqual(58828, crc16.spi_fujitsu(data))

    def test_t10_dif(self):
        self.assertEqual(53467, crc16.t10_dif(data))

    def test_teledisk(self):
        self.assertEqual(4019, crc16.teledisk(data))

    def test_tms37157(self):
        self.assertEqual(9905, crc16.tms37157(data))

    def test_umts(self):
        self.assertEqual(65256, crc16.umts(data))

    def test_usb(self):
        self.assertEqual(46280, crc16.usb(data))

    def test_xmodem(self):
        self.assertEqual(12739, crc16.xmodem(data))


class TestCrc32(unittest.TestCase):
    def test_aixm(self):
        self.assertEqual(806403967, crc32.aixm(data))

    def test_autosar(self):
        self.assertEqual(379048042, crc32.autosar(data))

    def test_base91_d(self):
        self.assertEqual(2268157302, crc32.base91_d(data))

    def test_bzip2(self):
        self.assertEqual(4236843288, crc32.bzip2(data))

    def test_cd_rom_edc(self):
        self.assertEqual(1858268612, crc32.cd_rom_edc(data))

    def test_cksum(self):
        self.assertEqual(1985902208, crc32.cksum(data))

    def test_iscsi(self):
        self.assertEqual(3808858755, crc32.iscsi(data))

    def test_iso_hdlc(self):
        self.assertEqual(3421780262, crc32.iso_hdlc(data))

    def test_jamcrc(self):
        self.assertEqual(873187033, crc32.jamcrc(data))

    def test_mpeg_2(self):
        self.assertEqual(58124007, crc32.mpeg_2(data))

    def test_xfer(self):
        self.assertEqual(3171672888, crc32.xfer(data))


class TestCrc64(unittest.TestCase):
    def test_ecma_182(self):
        self.assertEqual(7800480153909949255, crc64.ecma_182(data))

    def test_go_iso(self):
        self.assertEqual(13333283586479230977, crc64.go_iso(data))

    def test_we(self):
        self.assertEqual(7128171145767219210, crc64.we(data))

    def test_xz(self):
        self.assertEqual(11051210869376104954, crc64.xz(data))


if __name__ == "__main__":
    unittest.main()
