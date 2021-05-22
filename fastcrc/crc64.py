"""
Compute a CRC-64 checksum of data.
"""
from .fastcrc import crc_64_ecma_182 as _crc_64_ecma_182
from .fastcrc import crc_64_go_iso as _crc_64_go_iso
from .fastcrc import crc_64_we as _crc_64_we
from .fastcrc import crc_64_xz as _crc_64_xz
from .utils import _ensure_bytes

__always_supported = ("ecma_182", "go_iso", "we", "xz")

algorithms_guaranteed = set(__always_supported)
algorithms_available = set(__always_supported)


def ecma_182(data: bytes) -> int:
    """
    Compute a CRC-64 checksum of data with the ecma_182 algorithm.

    :param bytes data: The data to be computed
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """
    _ensure_bytes(data)
    return _crc_64_ecma_182(data)


def go_iso(data: bytes) -> int:
    """
    Compute a CRC-64 checksum of data with the go_iso algorithm.

    :param bytes data: The data to be computed
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """
    _ensure_bytes(data)
    return _crc_64_go_iso(data)


def we(data: bytes) -> int:
    """
    Compute a CRC-64 checksum of data with the we algorithm.

    :param bytes data: The data to be computed
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """
    _ensure_bytes(data)
    return _crc_64_we(data)


def xz(data: bytes) -> int:
    """
    Compute a CRC-64 checksum of data with the xz algorithm.

    :param bytes data: The data to be computed
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """
    _ensure_bytes(data)
    return _crc_64_xz(data)
