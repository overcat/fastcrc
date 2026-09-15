import sys
from typing import Optional, Set

if sys.version_info >= (3, 12):
    from collections.abc import Buffer
else:
    from typing_extensions import Buffer

algorithms_guaranteed: Set[str]
algorithms_available: Set[str]

def aixm(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-32 checksum of data with the `aixm` algorithm.

    Algorithm parameters:
        - poly: 0x814141ab
        - init: 0x00000000
        - xorout: 0x00000000
        - refin: False
        - refout: False

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def autosar(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-32 checksum of data with the `autosar` algorithm.

    Algorithm parameters:
        - poly: 0xf4acfb13
        - init: 0xffffffff
        - xorout: 0xffffffff
        - refin: True
        - refout: True

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def base91_d(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-32 checksum of data with the `base91 d` algorithm.

    Algorithm parameters:
        - poly: 0xa833982b
        - init: 0xffffffff
        - xorout: 0xffffffff
        - refin: True
        - refout: True

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def bzip2(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-32 checksum of data with the `bzip2` algorithm.

    Algorithm parameters:
        - poly: 0x04c11db7
        - init: 0xffffffff
        - xorout: 0xffffffff
        - refin: False
        - refout: False

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def cd_rom_edc(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-32 checksum of data with the `cd rom edc` algorithm.

    Algorithm parameters:
        - poly: 0x8001801b
        - init: 0x00000000
        - xorout: 0x00000000
        - refin: True
        - refout: True

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def cksum(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-32 checksum of data with the `cksum` algorithm.

    Algorithm parameters:
        - poly: 0x04c11db7
        - init: 0x00000000
        - xorout: 0xffffffff
        - refin: False
        - refout: False

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def iscsi(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-32 checksum of data with the `iscsi` algorithm.

    Algorithm parameters:
        - poly: 0x1edc6f41
        - init: 0xffffffff
        - xorout: 0xffffffff
        - refin: True
        - refout: True

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def iso_hdlc(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-32 checksum of data with the `iso hdlc` algorithm.

    Algorithm parameters:
        - poly: 0x04c11db7
        - init: 0xffffffff
        - xorout: 0xffffffff
        - refin: True
        - refout: True

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def jamcrc(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-32 checksum of data with the `jamcrc` algorithm.

    Algorithm parameters:
        - poly: 0x04c11db7
        - init: 0xffffffff
        - xorout: 0x00000000
        - refin: True
        - refout: True

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def mpeg_2(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-32 checksum of data with the `mpeg 2` algorithm.

    Algorithm parameters:
        - poly: 0x04c11db7
        - init: 0xffffffff
        - xorout: 0x00000000
        - refin: False
        - refout: False

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def xfer(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-32 checksum of data with the `xfer` algorithm.

    Algorithm parameters:
        - poly: 0x000000af
        - init: 0x00000000
        - xorout: 0x00000000
        - refin: False
        - refout: False

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def k_reversed_reciprocal_refin(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-32 checksum of data with the `k reversed reciprocal refin` algorithm.

    **This method may be removed in the future.**

    Algorithm parameters:
        - poly: 0xba0dc66b
        - init: 0x00000000
        - xorout: 0x00000000
        - refin: True
        - refout: False

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """
