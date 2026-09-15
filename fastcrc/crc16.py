"""
Compute a CRC-16 checksum of data.
"""
from .fastcrc import crc16 as _crc16

__all__ = [
    "algorithms_available",
    "algorithms_guaranteed",
    "arc",
    "autosar",
    "cdma2000",
    "cms",
    "dds_110",
    "dect_r",
    "dect_x",
    "dnp",
    "en_13757",
    "genibus",
    "gsm",
    "ibm_3740",
    "ibm_sdlc",
    "iso_iec_14443_3_a",
    "kermit",
    "lj1200",
    "maxim_dow",
    "mcrf4xx",
    "modbus",
    "nrsc_5",
    "opensafety_a",
    "opensafety_b",
    "profibus",
    "riello",
    "spi_fujitsu",
    "t10_dif",
    "teledisk",
    "tms37157",
    "umts",
    "usb",
    "xmodem",
    "ibm_refin",
]

__always_supported = (
    "arc",
    "autosar",
    "cdma2000",
    "cms",
    "dds_110",
    "dect_r",
    "dect_x",
    "dnp",
    "en_13757",
    "genibus",
    "gsm",
    "ibm_3740",
    "ibm_sdlc",
    "iso_iec_14443_3_a",
    "kermit",
    "lj1200",
    "maxim_dow",
    "mcrf4xx",
    "modbus",
    "nrsc_5",
    "opensafety_a",
    "opensafety_b",
    "profibus",
    "riello",
    "spi_fujitsu",
    "t10_dif",
    "teledisk",
    "tms37157",
    "umts",
    "usb",
    "xmodem",
)

algorithms_guaranteed = set(__always_supported)
algorithms_available = set(__always_supported)

arc = _crc16.arc
autosar = _crc16.autosar
cdma2000 = _crc16.cdma2000
cms = _crc16.cms
dds_110 = _crc16.dds_110
dect_r = _crc16.dect_r
dect_x = _crc16.dect_x
dnp = _crc16.dnp
en_13757 = _crc16.en_13757
genibus = _crc16.genibus
gsm = _crc16.gsm
ibm_3740 = _crc16.ibm_3740
ibm_sdlc = _crc16.ibm_sdlc
iso_iec_14443_3_a = _crc16.iso_iec_14443_3_a
kermit = _crc16.kermit
lj1200 = _crc16.lj1200
maxim_dow = _crc16.maxim_dow
mcrf4xx = _crc16.mcrf4xx
modbus = _crc16.modbus
nrsc_5 = _crc16.nrsc_5
opensafety_a = _crc16.opensafety_a
opensafety_b = _crc16.opensafety_b
profibus = _crc16.profibus
riello = _crc16.riello
spi_fujitsu = _crc16.spi_fujitsu
t10_dif = _crc16.t10_dif
teledisk = _crc16.teledisk
tms37157 = _crc16.tms37157
umts = _crc16.umts
usb = _crc16.usb
xmodem = _crc16.xmodem
ibm_refin = _crc16.ibm_refin
