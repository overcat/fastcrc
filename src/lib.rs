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

extern crate paste;

// Macro to define a CRC function
macro_rules! define_crc_fn {
    ($name:ident, $word_type:ty, $crc_type:ty) => {
        ::paste::paste! {
            #[pyfunction]
            fn $name(data: &[u8], initial: Option<$word_type>) -> PyResult<$word_type> {
                const CRC: Crc<$word_type> = Crc::<$word_type>::new(&$crc_type);
                let mut digest = match initial {
                    None => CRC.digest(),
                    Some(mut value) => {
                        value ^= $crc_type.xorout;
                        if $crc_type.refin {
                            value = value.reverse_bits()
                        }
                        CRC.digest_with_initial(value)
                    }
                };
                digest.update(&data);
                Ok(digest.finalize())
            }
        }
    }
}

define_crc_fn!(crc_16_arc, u16, CRC_16_ARC);
define_crc_fn!(crc_16_cdma2000, u16, CRC_16_CDMA2000);
define_crc_fn!(crc_16_cms, u16, CRC_16_CMS);
define_crc_fn!(crc_16_dds_110, u16, CRC_16_DDS_110);
define_crc_fn!(crc_16_dect_r, u16, CRC_16_DECT_R);
define_crc_fn!(crc_16_dect_x, u16, CRC_16_DECT_X);
define_crc_fn!(crc_16_dnp, u16, CRC_16_DNP);
define_crc_fn!(crc_16_en_13757, u16, CRC_16_EN_13757);
define_crc_fn!(crc_16_genibus, u16, CRC_16_GENIBUS);
define_crc_fn!(crc_16_gsm, u16, CRC_16_GSM);
define_crc_fn!(crc_16_ibm_3740, u16, CRC_16_IBM_3740);
define_crc_fn!(crc_16_ibm_sdlc, u16, CRC_16_IBM_SDLC);
define_crc_fn!(crc_16_iso_iec_14443_3_a, u16, CRC_16_ISO_IEC_14443_3_A);
define_crc_fn!(crc_16_kermit, u16, CRC_16_KERMIT);
define_crc_fn!(crc_16_lj1200, u16, CRC_16_LJ1200);
define_crc_fn!(crc_16_maxim_dow, u16, CRC_16_MAXIM_DOW);
define_crc_fn!(crc_16_mcrf4xx, u16, CRC_16_MCRF4XX);
define_crc_fn!(crc_16_modbus, u16, CRC_16_MODBUS);
define_crc_fn!(crc_16_nrsc_5, u16, CRC_16_NRSC_5);
define_crc_fn!(crc_16_opensafety_a, u16, CRC_16_OPENSAFETY_A);
define_crc_fn!(crc_16_opensafety_b, u16, CRC_16_OPENSAFETY_B);
define_crc_fn!(crc_16_profibus, u16, CRC_16_PROFIBUS);
define_crc_fn!(crc_16_riello, u16, CRC_16_RIELLO);
define_crc_fn!(crc_16_spi_fujitsu, u16, CRC_16_SPI_FUJITSU);
define_crc_fn!(crc_16_t10_dif, u16, CRC_16_T10_DIF);
define_crc_fn!(crc_16_teledisk, u16, CRC_16_TELEDISK);
define_crc_fn!(crc_16_tms37157, u16, CRC_16_TMS37157);
define_crc_fn!(crc_16_umts, u16, CRC_16_UMTS);
define_crc_fn!(crc_16_usb, u16, CRC_16_USB);
define_crc_fn!(crc_16_xmodem, u16, CRC_16_XMODEM);
define_crc_fn!(crc_32_aixm, u32, CRC_32_AIXM);
define_crc_fn!(crc_32_autosar, u32, CRC_32_AUTOSAR);
define_crc_fn!(crc_32_base91_d, u32, CRC_32_BASE91_D);
define_crc_fn!(crc_32_bzip2, u32, CRC_32_BZIP2);
define_crc_fn!(crc_32_cd_rom_edc, u32, CRC_32_CD_ROM_EDC);
define_crc_fn!(crc_32_cksum, u32, CRC_32_CKSUM);
define_crc_fn!(crc_32_iscsi, u32, CRC_32_ISCSI);
define_crc_fn!(crc_32_iso_hdlc, u32, CRC_32_ISO_HDLC);
define_crc_fn!(crc_32_jamcrc, u32, CRC_32_JAMCRC);
define_crc_fn!(crc_32_mpeg_2, u32, CRC_32_MPEG_2);
define_crc_fn!(crc_32_xfer, u32, CRC_32_XFER);
define_crc_fn!(crc_64_ecma_182, u64, CRC_64_ECMA_182);
define_crc_fn!(crc_64_go_iso, u64, CRC_64_GO_ISO);
define_crc_fn!(crc_64_we, u64, CRC_64_WE);
define_crc_fn!(crc_64_xz, u64, CRC_64_XZ);

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
