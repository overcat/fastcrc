import sys
from typing import Optional, Set

if sys.version_info >= (3, 12):
    from collections.abc import Buffer
else:
    from typing_extensions import Buffer

algorithms_guaranteed: Set[str]
algorithms_available: Set[str]

def ecma_182(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-64 checksum of data with the `ecma 182` algorithm.

    Algorithm parameters:
        - poly: 0x42f0e1eba9ea3693
        - init: 0x0000000000000000
        - xorout: 0x0000000000000000
        - refin: False
        - refout: False

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def go_iso(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-64 checksum of data with the `go iso` algorithm.

    Algorithm parameters:
        - poly: 0x000000000000001b
        - init: 0xffffffffffffffff
        - xorout: 0xffffffffffffffff
        - refin: True
        - refout: True

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def we(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-64 checksum of data with the `we` algorithm.

    Algorithm parameters:
        - poly: 0x42f0e1eba9ea3693
        - init: 0xffffffffffffffff
        - xorout: 0xffffffffffffffff
        - refin: False
        - refout: False

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def xz(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-64 checksum of data with the `xz` algorithm.

    Algorithm parameters:
        - poly: 0x42f0e1eba9ea3693
        - init: 0xffffffffffffffff
        - xorout: 0xffffffffffffffff
        - refin: True
        - refout: True

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def tms570_iso(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-64 checksum of data with the `tms570_iso` algorithm.

    Algorithm parameters:
        - poly: 0x000000000000001b
        - init: 0x0000000000000000
        - xorout: 0x0000000000000000
        - refin: False
        - refout: False

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """
