use crc::{
    Crc, CRC_16_ARC, CRC_16_CDMA2000, CRC_16_CMS, CRC_16_DDS_110, CRC_16_DECT_R, CRC_16_DECT_X,
    CRC_16_DNP, CRC_16_EN_13757, CRC_16_GENIBUS, CRC_16_GSM, CRC_16_IBM_3740, CRC_16_IBM_SDLC,
    CRC_16_ISO_IEC_14443_3_A, CRC_16_KERMIT, CRC_16_LJ1200, CRC_16_MAXIM_DOW, CRC_16_MCRF4XX,
    CRC_16_MODBUS, CRC_16_NRSC_5, CRC_16_OPENSAFETY_A, CRC_16_OPENSAFETY_B, CRC_16_PROFIBUS,
    CRC_16_RIELLO, CRC_16_SPI_FUJITSU, CRC_16_T10_DIF, CRC_16_TELEDISK, CRC_16_TMS37157,
    CRC_16_UMTS, CRC_16_USB, CRC_16_XMODEM, CRC_32_AIXM, CRC_32_AUTOSAR, CRC_32_BASE91_D,
    CRC_32_BZIP2, CRC_32_CD_ROM_EDC, CRC_32_CKSUM, CRC_32_ISCSI, CRC_32_ISO_HDLC, CRC_32_JAMCRC,
    CRC_32_MPEG_2, CRC_32_XFER, CRC_64_ECMA_182, CRC_64_GO_ISO, CRC_64_WE, CRC_64_XZ,
};
use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

#[pyfunction]
fn crc_16_arc(data: &[u8]) -> PyResult<u16> {
    const CRC: Crc<u16> = Crc::<u16>::new(&CRC_16_ARC);
    Ok(CRC.checksum(&data))
}

#[pyfunction]
fn crc_16_cdma2000(data: &[u8]) -> PyResult<u16> {
    const CRC: Crc<u16> = Crc::<u16>::new(&CRC_16_CDMA2000);
    Ok(CRC.checksum(&data))
}

#[pyfunction]
fn crc_16_cms(data: &[u8]) -> PyResult<u16> {
    const CRC: Crc<u16> = Crc::<u16>::new(&CRC_16_CMS);
    Ok(CRC.checksum(&data))
}

#[pyfunction]
fn crc_16_dds_110(data: &[u8]) -> PyResult<u16> {
    const CRC: Crc<u16> = Crc::<u16>::new(&CRC_16_DDS_110);
    Ok(CRC.checksum(&data))
}

#[pyfunction]
fn crc_16_dect_r(data: &[u8]) -> PyResult<u16> {
    const CRC: Crc<u16> = Crc::<u16>::new(&CRC_16_DECT_R);
    Ok(CRC.checksum(&data))
}

#[pyfunction]
fn crc_16_dect_x(data: &[u8]) -> PyResult<u16> {
    const CRC: Crc<u16> = Crc::<u16>::new(&CRC_16_DECT_X);
    Ok(CRC.checksum(&data))
}

#[pyfunction]
fn crc_16_dnp(data: &[u8]) -> PyResult<u16> {
    const CRC: Crc<u16> = Crc::<u16>::new(&CRC_16_DNP);
    Ok(CRC.checksum(&data))
}

#[pyfunction]
fn crc_16_en_13757(data: &[u8]) -> PyResult<u16> {
    const CRC: Crc<u16> = Crc::<u16>::new(&CRC_16_EN_13757);
    Ok(CRC.checksum(&data))
}

#[pyfunction]
fn crc_16_genibus(data: &[u8]) -> PyResult<u16> {
    const CRC: Crc<u16> = Crc::<u16>::new(&CRC_16_GENIBUS);
    Ok(CRC.checksum(&data))
}

#[pyfunction]
fn crc_16_gsm(data: &[u8]) -> PyResult<u16> {
    const CRC: Crc<u16> = Crc::<u16>::new(&CRC_16_GSM);
    Ok(CRC.checksum(&data))
}

#[pyfunction]
fn crc_16_ibm_3740(data: &[u8]) -> PyResult<u16> {
    const CRC: Crc<u16> = Crc::<u16>::new(&CRC_16_IBM_3740);
    Ok(CRC.checksum(&data))
}

#[pyfunction]
fn crc_16_ibm_sdlc(data: &[u8]) -> PyResult<u16> {
    const CRC: Crc<u16> = Crc::<u16>::new(&CRC_16_IBM_SDLC);
    Ok(CRC.checksum(&data))
}

#[pyfunction]
fn crc_16_iso_iec_14443_3_a(data: &[u8]) -> PyResult<u16> {
    const CRC: Crc<u16> = Crc::<u16>::new(&CRC_16_ISO_IEC_14443_3_A);
    Ok(CRC.checksum(&data))
}

#[pyfunction]
fn crc_16_kermit(data: &[u8]) -> PyResult<u16> {
    const CRC: Crc<u16> = Crc::<u16>::new(&CRC_16_KERMIT);
    Ok(CRC.checksum(&data))
}

#[pyfunction]
fn crc_16_lj1200(data: &[u8]) -> PyResult<u16> {
    const CRC: Crc<u16> = Crc::<u16>::new(&CRC_16_LJ1200);
    Ok(CRC.checksum(&data))
}

#[pyfunction]
fn crc_16_maxim_dow(data: &[u8]) -> PyResult<u16> {
    const CRC: Crc<u16> = Crc::<u16>::new(&CRC_16_MAXIM_DOW);
    Ok(CRC.checksum(&data))
}

#[pyfunction]
fn crc_16_mcrf4xx(data: &[u8]) -> PyResult<u16> {
    const CRC: Crc<u16> = Crc::<u16>::new(&CRC_16_MCRF4XX);
    Ok(CRC.checksum(&data))
}

#[pyfunction]
fn crc_16_modbus(data: &[u8]) -> PyResult<u16> {
    const CRC: Crc<u16> = Crc::<u16>::new(&CRC_16_MODBUS);
    Ok(CRC.checksum(&data))
}

#[pyfunction]
fn crc_16_nrsc_5(data: &[u8]) -> PyResult<u16> {
    const CRC: Crc<u16> = Crc::<u16>::new(&CRC_16_NRSC_5);
    Ok(CRC.checksum(&data))
}

#[pyfunction]
fn crc_16_opensafety_a(data: &[u8]) -> PyResult<u16> {
    const CRC: Crc<u16> = Crc::<u16>::new(&CRC_16_OPENSAFETY_A);
    Ok(CRC.checksum(&data))
}

#[pyfunction]
fn crc_16_opensafety_b(data: &[u8]) -> PyResult<u16> {
    const CRC: Crc<u16> = Crc::<u16>::new(&CRC_16_OPENSAFETY_B);
    Ok(CRC.checksum(&data))
}

#[pyfunction]
fn crc_16_profibus(data: &[u8]) -> PyResult<u16> {
    const CRC: Crc<u16> = Crc::<u16>::new(&CRC_16_PROFIBUS);
    Ok(CRC.checksum(&data))
}

#[pyfunction]
fn crc_16_riello(data: &[u8]) -> PyResult<u16> {
    const CRC: Crc<u16> = Crc::<u16>::new(&CRC_16_RIELLO);
    Ok(CRC.checksum(&data))
}

#[pyfunction]
fn crc_16_spi_fujitsu(data: &[u8]) -> PyResult<u16> {
    const CRC: Crc<u16> = Crc::<u16>::new(&CRC_16_SPI_FUJITSU);
    Ok(CRC.checksum(&data))
}

#[pyfunction]
fn crc_16_t10_dif(data: &[u8]) -> PyResult<u16> {
    const CRC: Crc<u16> = Crc::<u16>::new(&CRC_16_T10_DIF);
    Ok(CRC.checksum(&data))
}

#[pyfunction]
fn crc_16_teledisk(data: &[u8]) -> PyResult<u16> {
    const CRC: Crc<u16> = Crc::<u16>::new(&CRC_16_TELEDISK);
    Ok(CRC.checksum(&data))
}

#[pyfunction]
fn crc_16_tms37157(data: &[u8]) -> PyResult<u16> {
    const CRC: Crc<u16> = Crc::<u16>::new(&CRC_16_TMS37157);
    Ok(CRC.checksum(&data))
}

#[pyfunction]
fn crc_16_umts(data: &[u8]) -> PyResult<u16> {
    const CRC: Crc<u16> = Crc::<u16>::new(&CRC_16_UMTS);
    Ok(CRC.checksum(&data))
}

#[pyfunction]
fn crc_16_usb(data: &[u8]) -> PyResult<u16> {
    const CRC: Crc<u16> = Crc::<u16>::new(&CRC_16_USB);
    Ok(CRC.checksum(&data))
}

#[pyfunction]
fn crc_16_xmodem(data: &[u8]) -> PyResult<u16> {
    const CRC: Crc<u16> = Crc::<u16>::new(&CRC_16_XMODEM);
    Ok(CRC.checksum(&data))
}

#[pyfunction]
fn crc_32_aixm(data: &[u8]) -> PyResult<u32> {
    const CRC: Crc<u32> = Crc::<u32>::new(&CRC_32_AIXM);
    Ok(CRC.checksum(&data))
}

#[pyfunction]
fn crc_32_autosar(data: &[u8]) -> PyResult<u32> {
    const CRC: Crc<u32> = Crc::<u32>::new(&CRC_32_AUTOSAR);
    Ok(CRC.checksum(&data))
}

#[pyfunction]
fn crc_32_base91_d(data: &[u8]) -> PyResult<u32> {
    const CRC: Crc<u32> = Crc::<u32>::new(&CRC_32_BASE91_D);
    Ok(CRC.checksum(&data))
}

#[pyfunction]
fn crc_32_bzip2(data: &[u8]) -> PyResult<u32> {
    const CRC: Crc<u32> = Crc::<u32>::new(&CRC_32_BZIP2);
    Ok(CRC.checksum(&data))
}

#[pyfunction]
fn crc_32_cd_rom_edc(data: &[u8]) -> PyResult<u32> {
    const CRC: Crc<u32> = Crc::<u32>::new(&CRC_32_CD_ROM_EDC);
    Ok(CRC.checksum(&data))
}

#[pyfunction]
fn crc_32_cksum(data: &[u8]) -> PyResult<u32> {
    const CRC: Crc<u32> = Crc::<u32>::new(&CRC_32_CKSUM);
    Ok(CRC.checksum(&data))
}

#[pyfunction]
fn crc_32_iscsi(data: &[u8]) -> PyResult<u32> {
    const CRC: Crc<u32> = Crc::<u32>::new(&CRC_32_ISCSI);
    Ok(CRC.checksum(&data))
}

#[pyfunction]
fn crc_32_iso_hdlc(data: &[u8]) -> PyResult<u32> {
    const CRC: Crc<u32> = Crc::<u32>::new(&CRC_32_ISO_HDLC);
    Ok(CRC.checksum(&data))
}

#[pyfunction]
fn crc_32_jamcrc(data: &[u8]) -> PyResult<u32> {
    const CRC: Crc<u32> = Crc::<u32>::new(&CRC_32_JAMCRC);
    Ok(CRC.checksum(&data))
}

#[pyfunction]
fn crc_32_mpeg_2(data: &[u8]) -> PyResult<u32> {
    const CRC: Crc<u32> = Crc::<u32>::new(&CRC_32_MPEG_2);
    Ok(CRC.checksum(&data))
}

#[pyfunction]
fn crc_32_xfer(data: &[u8]) -> PyResult<u32> {
    const CRC: Crc<u32> = Crc::<u32>::new(&CRC_32_XFER);
    Ok(CRC.checksum(&data))
}

#[pyfunction]
fn crc_64_ecma_182(data: &[u8]) -> PyResult<u64> {
    const CRC: Crc<u64> = Crc::<u64>::new(&CRC_64_ECMA_182);
    Ok(CRC.checksum(&data))
}

#[pyfunction]
fn crc_64_go_iso(data: &[u8]) -> PyResult<u64> {
    const CRC: Crc<u64> = Crc::<u64>::new(&CRC_64_GO_ISO);
    Ok(CRC.checksum(&data))
}

#[pyfunction]
fn crc_64_we(data: &[u8]) -> PyResult<u64> {
    const CRC: Crc<u64> = Crc::<u64>::new(&CRC_64_WE);
    Ok(CRC.checksum(&data))
}

#[pyfunction]
fn crc_64_xz(data: &[u8]) -> PyResult<u64> {
    const CRC: Crc<u64> = Crc::<u64>::new(&CRC_64_XZ);
    Ok(CRC.checksum(&data))
}

#[pymodule]
fn fastcrc(_: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(crc_16_arc, m)?)?;
    m.add_function(wrap_pyfunction!(crc_16_cdma2000, m)?)?;
    m.add_function(wrap_pyfunction!(crc_16_cms, m)?)?;
    m.add_function(wrap_pyfunction!(crc_16_dds_110, m)?)?;
    m.add_function(wrap_pyfunction!(crc_16_dect_r, m)?)?;
    m.add_function(wrap_pyfunction!(crc_16_dect_x, m)?)?;
    m.add_function(wrap_pyfunction!(crc_16_dnp, m)?)?;
    m.add_function(wrap_pyfunction!(crc_16_en_13757, m)?)?;
    m.add_function(wrap_pyfunction!(crc_16_genibus, m)?)?;
    m.add_function(wrap_pyfunction!(crc_16_gsm, m)?)?;
    m.add_function(wrap_pyfunction!(crc_16_ibm_3740, m)?)?;
    m.add_function(wrap_pyfunction!(crc_16_ibm_sdlc, m)?)?;
    m.add_function(wrap_pyfunction!(crc_16_iso_iec_14443_3_a, m)?)?;
    m.add_function(wrap_pyfunction!(crc_16_kermit, m)?)?;
    m.add_function(wrap_pyfunction!(crc_16_lj1200, m)?)?;
    m.add_function(wrap_pyfunction!(crc_16_maxim_dow, m)?)?;
    m.add_function(wrap_pyfunction!(crc_16_mcrf4xx, m)?)?;
    m.add_function(wrap_pyfunction!(crc_16_modbus, m)?)?;
    m.add_function(wrap_pyfunction!(crc_16_nrsc_5, m)?)?;
    m.add_function(wrap_pyfunction!(crc_16_opensafety_a, m)?)?;
    m.add_function(wrap_pyfunction!(crc_16_opensafety_b, m)?)?;
    m.add_function(wrap_pyfunction!(crc_16_profibus, m)?)?;
    m.add_function(wrap_pyfunction!(crc_16_riello, m)?)?;
    m.add_function(wrap_pyfunction!(crc_16_spi_fujitsu, m)?)?;
    m.add_function(wrap_pyfunction!(crc_16_t10_dif, m)?)?;
    m.add_function(wrap_pyfunction!(crc_16_teledisk, m)?)?;
    m.add_function(wrap_pyfunction!(crc_16_tms37157, m)?)?;
    m.add_function(wrap_pyfunction!(crc_16_umts, m)?)?;
    m.add_function(wrap_pyfunction!(crc_16_usb, m)?)?;
    m.add_function(wrap_pyfunction!(crc_16_xmodem, m)?)?;
    m.add_function(wrap_pyfunction!(crc_32_aixm, m)?)?;
    m.add_function(wrap_pyfunction!(crc_32_autosar, m)?)?;
    m.add_function(wrap_pyfunction!(crc_32_base91_d, m)?)?;
    m.add_function(wrap_pyfunction!(crc_32_bzip2, m)?)?;
    m.add_function(wrap_pyfunction!(crc_32_cd_rom_edc, m)?)?;
    m.add_function(wrap_pyfunction!(crc_32_cksum, m)?)?;
    m.add_function(wrap_pyfunction!(crc_32_iscsi, m)?)?;
    m.add_function(wrap_pyfunction!(crc_32_iso_hdlc, m)?)?;
    m.add_function(wrap_pyfunction!(crc_32_jamcrc, m)?)?;
    m.add_function(wrap_pyfunction!(crc_32_mpeg_2, m)?)?;
    m.add_function(wrap_pyfunction!(crc_32_xfer, m)?)?;
    m.add_function(wrap_pyfunction!(crc_64_ecma_182, m)?)?;
    m.add_function(wrap_pyfunction!(crc_64_go_iso, m)?)?;
    m.add_function(wrap_pyfunction!(crc_64_we, m)?)?;
    m.add_function(wrap_pyfunction!(crc_64_xz, m)?)?;
    Ok(())
}
