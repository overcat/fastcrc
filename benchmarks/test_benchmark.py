import pytest
from fastcrc import crc16, crc32, crc64

test_data = b"123456789"


@pytest.mark.benchmark(group="crc_16_arc")
def test_crc_16_arc(benchmark):
    benchmark(crc16.arc, test_data)


@pytest.mark.benchmark(group="crc_16_cdma2000")
def test_crc_16_cdma2000(benchmark):
    benchmark(crc16.cdma2000, test_data)


@pytest.mark.benchmark(group="crc_16_cms")
def test_crc_16_cms(benchmark):
    benchmark(crc16.cms, test_data)


@pytest.mark.benchmark(group="crc_16_dds_110")
def test_crc_16_dds_110(benchmark):
    benchmark(crc16.dds_110, test_data)


@pytest.mark.benchmark(group="crc_16_dect_r")
def test_crc_16_dect_r(benchmark):
    benchmark(crc16.dect_r, test_data)


@pytest.mark.benchmark(group="crc_16_dect_x")
def test_crc_16_dect_x(benchmark):
    benchmark(crc16.dect_x, test_data)


@pytest.mark.benchmark(group="crc_16_dnp")
def test_crc_16_dnp(benchmark):
    benchmark(crc16.dnp, test_data)


@pytest.mark.benchmark(group="crc_16_en_13757")
def test_crc_16_en_13757(benchmark):
    benchmark(crc16.en_13757, test_data)


@pytest.mark.benchmark(group="crc_16_genibus")
def test_crc_16_genibus(benchmark):
    benchmark(crc16.genibus, test_data)


@pytest.mark.benchmark(group="crc_16_gsm")
def test_crc_16_gsm(benchmark):
    benchmark(crc16.gsm, test_data)


@pytest.mark.benchmark(group="crc_16_ibm_3740")
def test_crc_16_ibm_3740(benchmark):
    benchmark(crc16.ibm_3740, test_data)


@pytest.mark.benchmark(group="crc_16_ibm_sdlc")
def test_crc_16_ibm_sdlc(benchmark):
    benchmark(crc16.ibm_sdlc, test_data)


@pytest.mark.benchmark(group="crc_16_iso_iec_14443_3_a")
def test_crc_16_iso_iec_14443_3_a(benchmark):
    benchmark(crc16.iso_iec_14443_3_a, test_data)


@pytest.mark.benchmark(group="crc_16_kermit")
def test_crc_16_kermit(benchmark):
    benchmark(crc16.kermit, test_data)


@pytest.mark.benchmark(group="crc_16_lj1200")
def test_crc_16_lj1200(benchmark):
    benchmark(crc16.lj1200, test_data)


@pytest.mark.benchmark(group="crc_16_maxim_dow")
def test_crc_16_maxim_dow(benchmark):
    benchmark(crc16.maxim_dow, test_data)


@pytest.mark.benchmark(group="crc_16_mcrf4xx")
def test_crc_16_mcrf4xx(benchmark):
    benchmark(crc16.mcrf4xx, test_data)


@pytest.mark.benchmark(group="crc_16_modbus")
def test_crc_16_modbus(benchmark):
    benchmark(crc16.modbus, test_data)


@pytest.mark.benchmark(group="crc_16_nrsc_5")
def test_crc_16_nrsc_5(benchmark):
    benchmark(crc16.nrsc_5, test_data)


@pytest.mark.benchmark(group="crc_16_opensafety_a")
def test_crc_16_opensafety_a(benchmark):
    benchmark(crc16.opensafety_a, test_data)


@pytest.mark.benchmark(group="crc_16_opensafety_b")
def test_crc_16_opensafety_b(benchmark):
    benchmark(crc16.opensafety_b, test_data)


@pytest.mark.benchmark(group="crc_16_profibus")
def test_crc_16_profibus(benchmark):
    benchmark(crc16.profibus, test_data)


@pytest.mark.benchmark(group="crc_16_riello")
def test_crc_16_riello(benchmark):
    benchmark(crc16.riello, test_data)


@pytest.mark.benchmark(group="crc_16_spi_fujitsu")
def test_crc_16_spi_fujitsu(benchmark):
    benchmark(crc16.spi_fujitsu, test_data)


@pytest.mark.benchmark(group="crc_16_t10_dif")
def test_crc_16_t10_dif(benchmark):
    benchmark(crc16.t10_dif, test_data)


@pytest.mark.benchmark(group="crc_16_teledisk")
def test_crc_16_teledisk(benchmark):
    benchmark(crc16.teledisk, test_data)


@pytest.mark.benchmark(group="crc_16_tms37157")
def test_crc_16_tms37157(benchmark):
    benchmark(crc16.tms37157, test_data)


@pytest.mark.benchmark(group="crc_16_umts")
def test_crc_16_umts(benchmark):
    benchmark(crc16.umts, test_data)


@pytest.mark.benchmark(group="crc_16_usb")
def test_crc_16_usb(benchmark):
    benchmark(crc16.usb, test_data)


@pytest.mark.benchmark(group="crc_16_xmodem")
def test_crc_16_xmodem(benchmark):
    benchmark(crc16.xmodem, test_data)


@pytest.mark.benchmark(group="crc_32_aixm")
def test_crc_32_aixm(benchmark):
    benchmark(crc32.aixm, test_data)


@pytest.mark.benchmark(group="crc_32_autosar")
def test_crc_32_autosar(benchmark):
    benchmark(crc32.autosar, test_data)


@pytest.mark.benchmark(group="crc_32_base91_d")
def test_crc_32_base91_d(benchmark):
    benchmark(crc32.base91_d, test_data)


@pytest.mark.benchmark(group="crc_32_bzip2")
def test_crc_32_bzip2(benchmark):
    benchmark(crc32.bzip2, test_data)


@pytest.mark.benchmark(group="crc_32_cd_rom_edc")
def test_crc_32_cd_rom_edc(benchmark):
    benchmark(crc32.cd_rom_edc, test_data)


@pytest.mark.benchmark(group="crc_32_cksum")
def test_crc_32_cksum(benchmark):
    benchmark(crc32.cksum, test_data)


@pytest.mark.benchmark(group="crc_32_iscsi")
def test_crc_32_iscsi(benchmark):
    benchmark(crc32.iscsi, test_data)


@pytest.mark.benchmark(group="crc_32_iso_hdlc")
def test_crc_32_iso_hdlc(benchmark):
    benchmark(crc32.iso_hdlc, test_data)


@pytest.mark.benchmark(group="crc_32_jamcrc")
def test_crc_32_jamcrc(benchmark):
    benchmark(crc32.jamcrc, test_data)


@pytest.mark.benchmark(group="crc_32_mpeg_2")
def test_crc_32_mpeg_2(benchmark):
    benchmark(crc32.mpeg_2, test_data)


@pytest.mark.benchmark(group="crc_32_xfer")
def test_crc_32_xfer(benchmark):
    benchmark(crc32.xfer, test_data)


@pytest.mark.benchmark(group="crc_64_ecma_182")
def test_crc_64_ecma_182(benchmark):
    benchmark(crc64.ecma_182, test_data)


@pytest.mark.benchmark(group="crc_64_go_iso")
def test_crc_64_go_iso(benchmark):
    benchmark(crc64.go_iso, test_data)


@pytest.mark.benchmark(group="crc_64_we")
def test_crc_64_we(benchmark):
    benchmark(crc64.we, test_data)


@pytest.mark.benchmark(group="crc_64_xz")
def test_crc_64_xz(benchmark):
    benchmark(crc64.xz, test_data)
