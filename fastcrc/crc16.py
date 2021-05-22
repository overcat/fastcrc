"""
Compute a CRC-16 checksum of data.
"""
from .fastcrc import crc_16_arc as _crc_16_arc
from .fastcrc import crc_16_cdma2000 as _crc_16_cdma2000
from .fastcrc import crc_16_cms as _crc_16_cms
from .fastcrc import crc_16_dds_110 as _crc_16_dds_110
from .fastcrc import crc_16_dect_r as _crc_16_dect_r
from .fastcrc import crc_16_dect_x as _crc_16_dect_x
from .fastcrc import crc_16_dnp as _crc_16_dnp
from .fastcrc import crc_16_en_13757 as _crc_16_en_13757
from .fastcrc import crc_16_genibus as _crc_16_genibus
from .fastcrc import crc_16_gsm as _crc_16_gsm
from .fastcrc import crc_16_ibm_3740 as _crc_16_ibm_3740
from .fastcrc import crc_16_ibm_sdlc as _crc_16_ibm_sdlc
from .fastcrc import crc_16_iso_iec_14443_3_a as _crc_16_iso_iec_14443_3_a
from .fastcrc import crc_16_kermit as _crc_16_kermit
from .fastcrc import crc_16_lj1200 as _crc_16_lj1200
from .fastcrc import crc_16_maxim_dow as _crc_16_maxim_dow
from .fastcrc import crc_16_mcrf4xx as _crc_16_mcrf4xx
from .fastcrc import crc_16_modbus as _crc_16_modbus
from .fastcrc import crc_16_nrsc_5 as _crc_16_nrsc_5
from .fastcrc import crc_16_opensafety_a as _crc_16_opensafety_a
from .fastcrc import crc_16_opensafety_b as _crc_16_opensafety_b
from .fastcrc import crc_16_profibus as _crc_16_profibus
from .fastcrc import crc_16_riello as _crc_16_riello
from .fastcrc import crc_16_spi_fujitsu as _crc_16_spi_fujitsu
from .fastcrc import crc_16_t10_dif as _crc_16_t10_dif
from .fastcrc import crc_16_teledisk as _crc_16_teledisk
from .fastcrc import crc_16_tms37157 as _crc_16_tms37157
from .fastcrc import crc_16_umts as _crc_16_umts
from .fastcrc import crc_16_usb as _crc_16_usb
from .fastcrc import crc_16_xmodem as _crc_16_xmodem
from .utils import _ensure_bytes

__always_supported = (
    "arc",
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


def arc(data: bytes) -> int:
    """
    Compute a CRC-16 checksum of data with the arc algorithm.

    :param bytes data: The data to be computed
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """
    _ensure_bytes(data)
    return _crc_16_arc(data)


def cdma2000(data: bytes) -> int:
    """
    Compute a CRC-16 checksum of data with the cdma2000 algorithm.

    :param bytes data: The data to be computed
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """
    _ensure_bytes(data)
    return _crc_16_cdma2000(data)


def cms(data: bytes) -> int:
    """
    Compute a CRC-16 checksum of data with the cms algorithm.

    :param bytes data: The data to be computed
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """
    _ensure_bytes(data)
    return _crc_16_cms(data)


def dds_110(data: bytes) -> int:
    """
    Compute a CRC-16 checksum of data with the dds_110 algorithm.

    :param bytes data: The data to be computed
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """
    _ensure_bytes(data)
    return _crc_16_dds_110(data)


def dect_r(data: bytes) -> int:
    """
    Compute a CRC-16 checksum of data with the dect_r algorithm.

    :param bytes data: The data to be computed
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """
    _ensure_bytes(data)
    return _crc_16_dect_r(data)


def dect_x(data: bytes) -> int:
    """
    Compute a CRC-16 checksum of data with the dect_x algorithm.

    :param bytes data: The data to be computed
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """
    _ensure_bytes(data)
    return _crc_16_dect_x(data)


def dnp(data: bytes) -> int:
    """
    Compute a CRC-16 checksum of data with the dnp algorithm.

    :param bytes data: The data to be computed
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """
    _ensure_bytes(data)
    return _crc_16_dnp(data)


def en_13757(data: bytes) -> int:
    """
    Compute a CRC-16 checksum of data with the en_13757 algorithm.

    :param bytes data: The data to be computed
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """
    _ensure_bytes(data)
    return _crc_16_en_13757(data)


def genibus(data: bytes) -> int:
    """
    Compute a CRC-16 checksum of data with the genibus algorithm.

    :param bytes data: The data to be computed
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """
    _ensure_bytes(data)
    return _crc_16_genibus(data)


def gsm(data: bytes) -> int:
    """
    Compute a CRC-16 checksum of data with the gsm algorithm.

    :param bytes data: The data to be computed
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """
    _ensure_bytes(data)
    return _crc_16_gsm(data)


def ibm_3740(data: bytes) -> int:
    """
    Compute a CRC-16 checksum of data with the ibm_3740 algorithm.

    :param bytes data: The data to be computed
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """
    _ensure_bytes(data)
    return _crc_16_ibm_3740(data)


def ibm_sdlc(data: bytes) -> int:
    """
    Compute a CRC-16 checksum of data with the ibm_sdlc algorithm.

    :param bytes data: The data to be computed
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """
    _ensure_bytes(data)
    return _crc_16_ibm_sdlc(data)


def iso_iec_14443_3_a(data: bytes) -> int:
    """
    Compute a CRC-16 checksum of data with the iso_iec_14443_3_a algorithm.

    :param bytes data: The data to be computed
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """
    _ensure_bytes(data)
    return _crc_16_iso_iec_14443_3_a(data)


def kermit(data: bytes) -> int:
    """
    Compute a CRC-16 checksum of data with the kermit algorithm.

    :param bytes data: The data to be computed
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """
    _ensure_bytes(data)
    return _crc_16_kermit(data)


def lj1200(data: bytes) -> int:
    """
    Compute a CRC-16 checksum of data with the lj1200 algorithm.

    :param bytes data: The data to be computed
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """
    _ensure_bytes(data)
    return _crc_16_lj1200(data)


def maxim_dow(data: bytes) -> int:
    """
    Compute a CRC-16 checksum of data with the maxim_dow algorithm.

    :param bytes data: The data to be computed
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """
    _ensure_bytes(data)
    return _crc_16_maxim_dow(data)


def mcrf4xx(data: bytes) -> int:
    """
    Compute a CRC-16 checksum of data with the mcrf4xx algorithm.

    :param bytes data: The data to be computed
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """
    _ensure_bytes(data)
    return _crc_16_mcrf4xx(data)


def modbus(data: bytes) -> int:
    """
    Compute a CRC-16 checksum of data with the modbus algorithm.

    :param bytes data: The data to be computed
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """
    _ensure_bytes(data)
    return _crc_16_modbus(data)


def nrsc_5(data: bytes) -> int:
    """
    Compute a CRC-16 checksum of data with the nrsc_5 algorithm.

    :param bytes data: The data to be computed
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """
    _ensure_bytes(data)
    return _crc_16_nrsc_5(data)


def opensafety_a(data: bytes) -> int:
    """
    Compute a CRC-16 checksum of data with the opensafety_a algorithm.

    :param bytes data: The data to be computed
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """
    _ensure_bytes(data)
    return _crc_16_opensafety_a(data)


def opensafety_b(data: bytes) -> int:
    """
    Compute a CRC-16 checksum of data with the opensafety_b algorithm.

    :param bytes data: The data to be computed
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """
    _ensure_bytes(data)
    return _crc_16_opensafety_b(data)


def profibus(data: bytes) -> int:
    """
    Compute a CRC-16 checksum of data with the profibus algorithm.

    :param bytes data: The data to be computed
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """
    _ensure_bytes(data)
    return _crc_16_profibus(data)


def riello(data: bytes) -> int:
    """
    Compute a CRC-16 checksum of data with the riello algorithm.

    :param bytes data: The data to be computed
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """
    _ensure_bytes(data)
    return _crc_16_riello(data)


def spi_fujitsu(data: bytes) -> int:
    """
    Compute a CRC-16 checksum of data with the spi_fujitsu algorithm.

    :param bytes data: The data to be computed
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """
    _ensure_bytes(data)
    return _crc_16_spi_fujitsu(data)


def t10_dif(data: bytes) -> int:
    """
    Compute a CRC-16 checksum of data with the t10_dif algorithm.

    :param bytes data: The data to be computed
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """
    _ensure_bytes(data)
    return _crc_16_t10_dif(data)


def teledisk(data: bytes) -> int:
    """
    Compute a CRC-16 checksum of data with the teledisk algorithm.

    :param bytes data: The data to be computed
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """
    _ensure_bytes(data)
    return _crc_16_teledisk(data)


def tms37157(data: bytes) -> int:
    """
    Compute a CRC-16 checksum of data with the tms37157 algorithm.

    :param bytes data: The data to be computed
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """
    _ensure_bytes(data)
    return _crc_16_tms37157(data)


def umts(data: bytes) -> int:
    """
    Compute a CRC-16 checksum of data with the umts algorithm.

    :param bytes data: The data to be computed
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """
    _ensure_bytes(data)
    return _crc_16_umts(data)


def usb(data: bytes) -> int:
    """
    Compute a CRC-16 checksum of data with the usb algorithm.

    :param bytes data: The data to be computed
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """
    _ensure_bytes(data)
    return _crc_16_usb(data)


def xmodem(data: bytes) -> int:
    """
    Compute a CRC-16 checksum of data with the xmodem algorithm.

    :param bytes data: The data to be computed
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """
    _ensure_bytes(data)
    return _crc_16_xmodem(data)
