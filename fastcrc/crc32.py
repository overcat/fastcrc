"""
Compute a CRC-32 checksum of data.
"""
from typing import Optional

from .fastcrc import crc_32_aixm as _crc_32_aixm
from .fastcrc import crc_32_autosar as _crc_32_autosar
from .fastcrc import crc_32_base91_d as _crc_32_base91_d
from .fastcrc import crc_32_bzip2 as _crc_32_bzip2
from .fastcrc import crc_32_cd_rom_edc as _crc_32_cd_rom_edc
from .fastcrc import crc_32_cksum as _crc_32_cksum
from .fastcrc import crc_32_iscsi as _crc_32_iscsi
from .fastcrc import crc_32_iso_hdlc as _crc_32_iso_hdlc
from .fastcrc import crc_32_jamcrc as _crc_32_jamcrc
from .fastcrc import crc_32_mpeg_2 as _crc_32_mpeg_2
from .fastcrc import crc_32_xfer as _crc_32_xfer
from .fastcrc import (
    crc_32_reversed_reciprocal_refin as _crc_32_reversed_reciprocal_refin,
)
from .utils import _ensure_bytes

__always_supported = (
    "aixm",
    "autosar",
    "base91_d",
    "bzip2",
    "cd_rom_edc",
    "cksum",
    "iscsi",
    "iso_hdlc",
    "jamcrc",
    "mpeg_2",
    "xfer",
)

algorithms_guaranteed = set(__always_supported)
algorithms_available = set(__always_supported)


def aixm(data: bytes, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-32 checksum of data with the aixm algorithm.

    :param bytes data: The data to be computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """
    _ensure_bytes(data)
    return _crc_32_aixm(data, initial)


def autosar(data: bytes, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-32 checksum of data with the autosar algorithm.

    :param bytes data: The data to be computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """
    _ensure_bytes(data)
    return _crc_32_autosar(data, initial)


def base91_d(data: bytes, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-32 checksum of data with the base91_d algorithm.

    :param bytes data: The data to be computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """
    _ensure_bytes(data)
    return _crc_32_base91_d(data, initial)


def bzip2(data: bytes, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-32 checksum of data with the bzip2 algorithm.

    :param bytes data: The data to be computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """
    _ensure_bytes(data)
    return _crc_32_bzip2(data, initial)


def cd_rom_edc(data: bytes, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-32 checksum of data with the cd_rom_edc algorithm.

    :param bytes data: The data to be computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """
    _ensure_bytes(data)
    return _crc_32_cd_rom_edc(data, initial)


def cksum(data: bytes, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-32 checksum of data with the cksum algorithm.

    :param bytes data: The data to be computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """
    _ensure_bytes(data)
    return _crc_32_cksum(data, initial)


def iscsi(data: bytes, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-32 checksum of data with the iscsi algorithm.

    :param bytes data: The data to be computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """
    _ensure_bytes(data)
    return _crc_32_iscsi(data, initial)


def iso_hdlc(data: bytes, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-32 checksum of data with the iso_hdlc algorithm.

    :param bytes data: The data to be computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """
    _ensure_bytes(data)
    return _crc_32_iso_hdlc(data, initial)


def jamcrc(data: bytes, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-32 checksum of data with the jamcrc algorithm.

    :param bytes data: The data to be computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """
    _ensure_bytes(data)
    return _crc_32_jamcrc(data, initial)


def mpeg_2(data: bytes, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-32 checksum of data with the mpeg_2 algorithm.

    :param bytes data: The data to be computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """
    _ensure_bytes(data)
    return _crc_32_mpeg_2(data, initial)


def xfer(data: bytes, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-32 checksum of data with the xfer algorithm.

    :param bytes data: The data to be computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """
    _ensure_bytes(data)
    return _crc_32_xfer(data, initial)


def reversed_reciprocal_refin(data: bytes, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-32 checksum of data with the reversed reciprocal refin algorithm.

    **This method may be removed in the future.**

    :param bytes data: The data to be computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """
    _ensure_bytes(data)
    return _crc_32_reversed_reciprocal_refin(data, initial)
