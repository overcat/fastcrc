import sys
from typing import Optional, Set

if sys.version_info >= (3, 12):
    from collections.abc import Buffer
else:
    from typing_extensions import Buffer

algorithms_guaranteed: Set[str]
algorithms_available: Set[str]

def autosar(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-8 checksum of data with the `autosar` algorithm.

    Algorithm parameters:
        - poly: 0x2f
        - init: 0xff
        - xorout: 0xff
        - refin: False
        - refout: False

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def bluetooth(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-8 checksum of data with the `bluetooth` algorithm.

    Algorithm parameters:
        - poly: 0xa7
        - init: 0x00
        - xorout: 0x00
        - refin: True
        - refout: True

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def cdma2000(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-8 checksum of data with the `cdma2000` algorithm.

    Algorithm parameters:
        - poly: 0x9b
        - init: 0xff
        - xorout: 0x00
        - refin: False
        - refout: False

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def darc(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-8 checksum of data with the `darc` algorithm.

    Algorithm parameters:
        - poly: 0x39
        - init: 0x00
        - xorout: 0x00
        - refin: True
        - refout: True

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def dvb_s2(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-8 checksum of data with the `dvb_s2` algorithm.

    Algorithm parameters:
        - poly: 0xd5
        - init: 0x00
        - xorout: 0x00
        - refin: False
        - refout: False

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def gsm_a(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-8 checksum of data with the `gsm_a` algorithm.

    Algorithm parameters:
        - poly: 0x1d
        - init: 0x00
        - xorout: 0x00
        - refin: False
        - refout: False

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def gsm_b(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-8 checksum of data with the `gsm_b` algorithm.

    Algorithm parameters:
        - poly: 0x49
        - init: 0x00
        - xorout: 0xff
        - refin: False
        - refout: False

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def i_432_1(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-8 checksum of data with the `i_432_1` algorithm.

    Algorithm parameters:
        - poly: 0x07
        - init: 0x00
        - xorout: 0x55
        - refin: False
        - refout: False

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def i_code(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-8 checksum of data with the `i_code` algorithm.

    Algorithm parameters:
        - poly: 0x1d
        - init: 0xfd
        - xorout: 0x00
        - refin: False
        - refout: False

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def lte(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-8 checksum of data with the `lte` algorithm.

    Algorithm parameters:
        - poly: 0x9b
        - init: 0x00
        - xorout: 0x00
        - refin: False
        - refout: False

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def maxim_dow(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-8 checksum of data with the `maxim_dow` algorithm.

    Algorithm parameters:
        - poly: 0x31
        - init: 0x00
        - xorout: 0x00
        - refin: True
        - refout: True

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def mifare_mad(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-8 checksum of data with the `mifare_mad` algorithm.

    Algorithm parameters:
        - poly: 0x1d
        - init: 0xc7
        - xorout: 0x00
        - refin: False
        - refout: False

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def nrsc_5(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-8 checksum of data with the `nrsc_5` algorithm.

    Algorithm parameters:
        - poly: 0x31
        - init: 0xff
        - xorout: 0x00
        - refin: False
        - refout: False

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def opensafety(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-8 checksum of data with the `opensafety` algorithm.

    Algorithm parameters:
        - poly: 0x2f
        - init: 0x00
        - xorout: 0x00
        - refin: False
        - refout: False

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def rohc(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-8 checksum of data with the `rohc` algorithm.

    Algorithm parameters:
        - poly: 0x07
        - init: 0xff
        - xorout: 0x00
        - refin: True
        - refout: True

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def sae_j1850(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-8 checksum of data with the `sae_j1850` algorithm.

    Algorithm parameters:
        - poly: 0x1d
        - init: 0xff
        - xorout: 0xff
        - refin: False
        - refout: False

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def smbus(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-8 checksum of data with the `smbus` algorithm.

    Algorithm parameters:
        - poly: 0x07
        - init: 0x00
        - xorout: 0x00
        - refin: False
        - refout: False

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def tech_3250(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-8 checksum of data with the `tech_3250` algorithm.

    Algorithm parameters:
        - poly: 0x1d
        - init: 0xff
        - xorout: 0x00
        - refin: True
        - refout: True

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def wcdma(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-8 checksum of data with the `wcdma` algorithm.

    Algorithm parameters:
        - poly: 0x9b
        - init: 0x00
        - xorout: 0x00
        - refin: True
        - refout: True

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """
