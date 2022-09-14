import unittest

from fastcrc import crc16, crc32, crc64

data = b"123456789"
data_part1 = b"1234"
data_part2 = b"56789"


class TestCrc16(unittest.TestCase):
    def test_arc(self):
        self.assertEqual(47933, crc16.arc(data))

    def test_arc_init(self):
        self.assertEqual(47933, crc16.arc(data_part2, crc16.arc(data_part1)))

    def test_cdma2000(self):
        self.assertEqual(19462, crc16.cdma2000(data))

    def test_cdma2000_init(self):
        self.assertEqual(19462, crc16.cdma2000(data_part2, crc16.cdma2000(data_part1)))

    def test_cms(self):
        self.assertEqual(44775, crc16.cms(data))

    def test_cms_init(self):
        self.assertEqual(44775, crc16.cms(data_part2, crc16.cms(data_part1)))

    def test_dds_110(self):
        self.assertEqual(40655, crc16.dds_110(data))

    def test_dds_110_init(self):
        self.assertEqual(40655, crc16.dds_110(data_part2, crc16.dds_110(data_part1)))

    def test_dect_r(self):
        self.assertEqual(126, crc16.dect_r(data))

    def test_dect_r_init(self):
        self.assertEqual(126, crc16.dect_r(data_part2, crc16.dect_r(data_part1)))

    def test_dect_x(self):
        self.assertEqual(127, crc16.dect_x(data))

    def test_dect_x_init(self):
        self.assertEqual(127, crc16.dect_x(data_part2, crc16.dect_x(data_part1)))

    def test_dnp(self):
        self.assertEqual(60034, crc16.dnp(data))

    def test_dnp_init(self):
        self.assertEqual(60034, crc16.dnp(data_part2, crc16.dnp(data_part1)))

    def test_en_13757(self):
        self.assertEqual(49847, crc16.en_13757(data))

    def test_en_13757_init(self):
        self.assertEqual(49847, crc16.en_13757(data_part2, crc16.en_13757(data_part1)))

    def test_genibus(self):
        self.assertEqual(54862, crc16.genibus(data))

    def test_genibus_init(self):
        self.assertEqual(54862, crc16.genibus(data_part2, crc16.genibus(data_part1)))

    def test_gsm(self):
        self.assertEqual(52796, crc16.gsm(data))

    def test_gsm_init(self):
        self.assertEqual(52796, crc16.gsm(data_part2, crc16.gsm(data_part1)))

    def test_ibm_3740(self):
        self.assertEqual(10673, crc16.ibm_3740(data))

    def test_ibm_3740_init(self):
        self.assertEqual(10673, crc16.ibm_3740(data_part2, crc16.ibm_3740(data_part1)))

    def test_ibm_sdlc(self):
        self.assertEqual(36974, crc16.ibm_sdlc(data))

    def test_ibm_sdlc_init(self):
        self.assertEqual(36974, crc16.ibm_sdlc(data_part2, crc16.ibm_sdlc(data_part1)))

    def test_iso_iec_14443_3_a(self):
        self.assertEqual(48901, crc16.iso_iec_14443_3_a(data))

    def test_iso_iec_14443_3_a_init(self):
        self.assertEqual(
            48901,
            crc16.iso_iec_14443_3_a(data_part2, crc16.iso_iec_14443_3_a(data_part1)),
        )

    def test_kermit(self):
        self.assertEqual(8585, crc16.kermit(data))

    def test_kermit_init(self):
        self.assertEqual(8585, crc16.kermit(data_part2, crc16.kermit(data_part1)))

    def test_lj1200(self):
        self.assertEqual(48628, crc16.lj1200(data))

    def test_lj1200_init(self):
        self.assertEqual(48628, crc16.lj1200(data_part2, crc16.lj1200(data_part1)))

    def test_maxim_dow(self):
        self.assertEqual(17602, crc16.maxim_dow(data))

    def test_maxim_dow_init(self):
        self.assertEqual(
            17602, crc16.maxim_dow(data_part2, crc16.maxim_dow(data_part1))
        )

    def test_mcrf4xx(self):
        self.assertEqual(28561, crc16.mcrf4xx(data))

    def test_mcrf4xx_init(self):
        self.assertEqual(28561, crc16.mcrf4xx(data_part2, crc16.mcrf4xx(data_part1)))

    def test_modbus(self):
        self.assertEqual(19255, crc16.modbus(data))

    def test_modbus_init(self):
        self.assertEqual(19255, crc16.modbus(data_part2, crc16.modbus(data_part1)))

    def test_nrsc_5(self):
        self.assertEqual(41062, crc16.nrsc_5(data))

    def test_nrsc_5_init(self):
        self.assertEqual(41062, crc16.nrsc_5(data_part2, crc16.nrsc_5(data_part1)))

    def test_opensafety_a(self):
        self.assertEqual(23864, crc16.opensafety_a(data))

    def test_opensafety_a_init(self):
        self.assertEqual(
            23864, crc16.opensafety_a(data_part2, crc16.opensafety_a(data_part1))
        )

    def test_opensafety_b(self):
        self.assertEqual(8446, crc16.opensafety_b(data))

    def test_opensafety_b_init(self):
        self.assertEqual(
            8446, crc16.opensafety_b(data_part2, crc16.opensafety_b(data_part1))
        )

    def test_profibus(self):
        self.assertEqual(43033, crc16.profibus(data))

    def test_profibus_init(self):
        self.assertEqual(43033, crc16.profibus(data_part2, crc16.profibus(data_part1)))

    def test_riello(self):
        self.assertEqual(25552, crc16.riello(data))

    def test_riello_init(self):
        self.assertEqual(25552, crc16.riello(data_part2, crc16.riello(data_part1)))

    def test_spi_fujitsu(self):
        self.assertEqual(58828, crc16.spi_fujitsu(data))

    def test_spi_fujitsu_init(self):
        self.assertEqual(
            58828, crc16.spi_fujitsu(data_part2, crc16.spi_fujitsu(data_part1))
        )

    def test_t10_dif(self):
        self.assertEqual(53467, crc16.t10_dif(data))

    def test_t10_dif_init(self):
        self.assertEqual(53467, crc16.t10_dif(data_part2, crc16.t10_dif(data_part1)))

    def test_teledisk(self):
        self.assertEqual(4019, crc16.teledisk(data))

    def test_teledisk_init(self):
        self.assertEqual(4019, crc16.teledisk(data_part2, crc16.teledisk(data_part1)))

    def test_tms37157(self):
        self.assertEqual(9905, crc16.tms37157(data))

    def test_tms37157_init(self):
        self.assertEqual(9905, crc16.tms37157(data_part2, crc16.tms37157(data_part1)))

    def test_umts(self):
        self.assertEqual(65256, crc16.umts(data))

    def test_umts_init(self):
        self.assertEqual(65256, crc16.umts(data_part2, crc16.umts(data_part1)))

    def test_usb(self):
        self.assertEqual(46280, crc16.usb(data))

    def test_usb_init(self):
        self.assertEqual(46280, crc16.usb(data_part2, crc16.usb(data_part1)))

    def test_xmodem(self):
        self.assertEqual(12739, crc16.xmodem(data))

    def test_xmodem_init(self):
        self.assertEqual(12739, crc16.xmodem(data_part2, crc16.xmodem(data_part1)))

    def test_ibm_refin(self):
        self.assertEqual(15568, crc16.ibm_refin(data))

    def test_ibm_refin_init(self):
        self.assertEqual(
            15568, crc16.ibm_refin(data_part2, crc16.ibm_refin(data_part1))
        )


class TestCrc32(unittest.TestCase):
    def test_aixm(self):
        self.assertEqual(806403967, crc32.aixm(data))

    def test_aixm_init(self):
        self.assertEqual(806403967, crc32.aixm(data_part2, crc32.aixm(data_part1)))

    def test_autosar(self):
        self.assertEqual(379048042, crc32.autosar(data))

    def test_autosar_init(self):
        self.assertEqual(
            379048042, crc32.autosar(data_part2, crc32.autosar(data_part1))
        )

    def test_base91_d(self):
        self.assertEqual(2268157302, crc32.base91_d(data))

    def test_base91_d_init(self):
        self.assertEqual(
            2268157302, crc32.base91_d(data_part2, crc32.base91_d(data_part1))
        )

    def test_bzip2(self):
        self.assertEqual(4236843288, crc32.bzip2(data))

    def test_bzip2_init(self):
        self.assertEqual(4236843288, crc32.bzip2(data_part2, crc32.bzip2(data_part1)))

    def test_cd_rom_edc(self):
        self.assertEqual(1858268612, crc32.cd_rom_edc(data))

    def test_cd_rom_edc_init(self):
        self.assertEqual(
            1858268612, crc32.cd_rom_edc(data_part2, crc32.cd_rom_edc(data_part1))
        )

    def test_cksum(self):
        self.assertEqual(1985902208, crc32.cksum(data))

    def test_cksum_init(self):
        self.assertEqual(1985902208, crc32.cksum(data_part2, crc32.cksum(data_part1)))

    def test_iscsi(self):
        self.assertEqual(3808858755, crc32.iscsi(data))

    def test_iscsi_init(self):
        self.assertEqual(3808858755, crc32.iscsi(data_part2, crc32.iscsi(data_part1)))

    def test_iso_hdlc(self):
        self.assertEqual(3421780262, crc32.iso_hdlc(data))

    def test_iso_hdlc_init(self):
        self.assertEqual(
            3421780262, crc32.iso_hdlc(data_part2, crc32.iso_hdlc(data_part1))
        )

    def test_jamcrc(self):
        self.assertEqual(873187033, crc32.jamcrc(data))

    def test_jamcrc_init(self):
        self.assertEqual(873187033, crc32.jamcrc(data_part2, crc32.jamcrc(data_part1)))

    def test_mpeg_2(self):
        self.assertEqual(58124007, crc32.mpeg_2(data))

    def test_mpeg_2_init(self):
        self.assertEqual(58124007, crc32.mpeg_2(data_part2, crc32.mpeg_2(data_part1)))

    def test_xfer(self):
        self.assertEqual(3171672888, crc32.xfer(data))

    def test_xfer_init(self):
        self.assertEqual(3171672888, crc32.xfer(data_part2, crc32.xfer(data_part1)))

    def test_reversed_reciprocal_refin(self):
        self.assertEqual(
            1239285113,
            crc32.reversed_reciprocal_refin(data),
        )

    def test_reversed_reciprocal_refin_init(self):
        self.assertEqual(
            1239285113,
            crc32.reversed_reciprocal_refin(
                data_part2, crc32.reversed_reciprocal_refin(data_part1)
            ),
        )


class TestCrc64(unittest.TestCase):
    def test_ecma_182(self):
        self.assertEqual(7800480153909949255, crc64.ecma_182(data))

    def test_ecma_182_init(self):
        self.assertEqual(
            7800480153909949255, crc64.ecma_182(data_part2, crc64.ecma_182(data_part1))
        )

    def test_go_iso(self):
        self.assertEqual(13333283586479230977, crc64.go_iso(data))

    def test_go_iso_init(self):
        self.assertEqual(
            13333283586479230977, crc64.go_iso(data_part2, crc64.go_iso(data_part1))
        )

    def test_we(self):
        self.assertEqual(7128171145767219210, crc64.we(data))

    def test_we_init(self):
        self.assertEqual(
            7128171145767219210, crc64.we(data_part2, crc64.we(data_part1))
        )

    def test_xz(self):
        self.assertEqual(11051210869376104954, crc64.xz(data))

    def test_xz_init(self):
        self.assertEqual(
            11051210869376104954, crc64.xz(data_part2, crc64.xz(data_part1))
        )


if __name__ == "__main__":
    unittest.main()
