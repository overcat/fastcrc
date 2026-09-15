from typing import Optional, Set

algorithms_guaranteed: Set[str]
algorithms_available: Set[str]

def ecma_182(data: bytes, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-64 checksum of data with the `ecma 182` algorithm.

    Algorithm parameters:
        - poly: 0x42f0e1eba9ea3693
        - init: 0x0000000000000000
        - xorout: 0x0000000000000000
        - refin: False
        - refout: False

    :param bytes data: The data to be computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def go_iso(data: bytes, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-64 checksum of data with the `go iso` algorithm.

    Algorithm parameters:
        - poly: 0x000000000000001b
        - init: 0xffffffffffffffff
        - xorout: 0xffffffffffffffff
        - refin: True
        - refout: True

    :param bytes data: The data to be computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def we(data: bytes, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-64 checksum of data with the `we` algorithm.

    Algorithm parameters:
        - poly: 0x42f0e1eba9ea3693
        - init: 0xffffffffffffffff
        - xorout: 0xffffffffffffffff
        - refin: False
        - refout: False

    :param bytes data: The data to be computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def xz(data: bytes, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-64 checksum of data with the `xz` algorithm.

    Algorithm parameters:
        - poly: 0x42f0e1eba9ea3693
        - init: 0xffffffffffffffff
        - xorout: 0xffffffffffffffff
        - refin: True
        - refout: True

    :param bytes data: The data to be computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def tms570_iso(data: bytes, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-64 checksum of data with the `tms570_iso` algorithm.

    Algorithm parameters:
        - poly: 0x000000000000001b
        - init: 0x0000000000000000
        - xorout: 0x0000000000000000
        - refin: False
        - refout: False

    :param bytes data: The data to be computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """
