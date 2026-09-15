import sys
from typing import Optional, Set

if sys.version_info >= (3, 12):
    from collections.abc import Buffer
else:
    from typing_extensions import Buffer

algorithms_guaranteed: Set[str]
algorithms_available: Set[str]

def arc(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-16 checksum of data with the `arc` algorithm.

    Algorithm parameters:
        - poly: 0x8005
        - init: 0x0000
        - xorout: 0x0000
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
    Compute a CRC-16 checksum of data with the `cdma2000` algorithm.

    Algorithm parameters:
        - poly: 0xc867
        - init: 0xffff
        - xorout: 0x0000
        - refin: False
        - refout: False

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def cms(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-16 checksum of data with the `cms` algorithm.

    Algorithm parameters:
        - poly: 0x8005
        - init: 0xffff
        - xorout: 0x0000
        - refin: False
        - refout: False

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def dds_110(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-16 checksum of data with the `dds 110` algorithm.

    Algorithm parameters:
        - poly: 0x8005
        - init: 0x800d
        - xorout: 0x0000
        - refin: False
        - refout: False

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def dect_r(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-16 checksum of data with the `dect r` algorithm.

    Algorithm parameters:
        - poly: 0x0589
        - init: 0x0000
        - xorout: 0x0001
        - refin: False
        - refout: False

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def dect_x(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-16 checksum of data with the `dect x` algorithm.

    Algorithm parameters:
        - poly: 0x0589
        - init: 0x0000
        - xorout: 0x0000
        - refin: False
        - refout: False

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def dnp(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-16 checksum of data with the `dnp` algorithm.

    Algorithm parameters:
        - poly: 0x3d65
        - init: 0x0000
        - xorout: 0xffff
        - refin: True
        - refout: True

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def en_13757(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-16 checksum of data with the `en 13757` algorithm.

    Algorithm parameters:
        - poly: 0x3d65
        - init: 0x0000
        - xorout: 0xffff
        - refin: False
        - refout: False

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def genibus(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-16 checksum of data with the `genibus` algorithm.

    Algorithm parameters:
        - poly: 0x1021
        - init: 0xffff
        - xorout: 0xffff
        - refin: False
        - refout: False

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def gsm(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-16 checksum of data with the `gsm` algorithm.

    Algorithm parameters:
        - poly: 0x1021
        - init: 0x0000
        - xorout: 0xffff
        - refin: False
        - refout: False

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def ibm_3740(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-16 checksum of data with the `ibm 3740` algorithm.

    Algorithm parameters:
        - poly: 0x1021
        - init: 0xffff
        - xorout: 0x0000
        - refin: False
        - refout: False

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def ibm_sdlc(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-16 checksum of data with the `ibm sdlc` algorithm.

    Algorithm parameters:
        - poly: 0x1021
        - init: 0xffff
        - xorout: 0xffff
        - refin: True
        - refout: True

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def iso_iec_14443_3_a(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-16 checksum of data with the `iso iec 14443 3 a` algorithm.

    Algorithm parameters:
        - poly: 0x1021
        - init: 0xc6c6
        - xorout: 0x0000
        - refin: True
        - refout: True

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def kermit(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-16 checksum of data with the `kermit` algorithm.

    Algorithm parameters:
        - poly: 0x1021
        - init: 0x0000
        - xorout: 0x0000
        - refin: True
        - refout: True

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def lj1200(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-16 checksum of data with the `lj1200` algorithm.

    Algorithm parameters:
        - poly: 0x6f63
        - init: 0x0000
        - xorout: 0x0000
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
    Compute a CRC-16 checksum of data with the `maxim dow` algorithm.

    Algorithm parameters:
        - poly: 0x8005
        - init: 0x0000
        - xorout: 0xffff
        - refin: True
        - refout: True

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def mcrf4xx(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-16 checksum of data with the `mcrf4xx` algorithm.

    Algorithm parameters:
        - poly: 0x1021
        - init: 0xffff
        - xorout: 0x0000
        - refin: True
        - refout: True

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def modbus(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-16 checksum of data with the `modbus` algorithm.

    Algorithm parameters:
        - poly: 0x8005
        - init: 0xffff
        - xorout: 0x0000
        - refin: True
        - refout: True

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def nrsc_5(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-16 checksum of data with the `nrsc 5` algorithm.

    Algorithm parameters:
        - poly: 0x080b
        - init: 0xffff
        - xorout: 0x0000
        - refin: True
        - refout: True

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def opensafety_a(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-16 checksum of data with the `opensafety a` algorithm.

    Algorithm parameters:
        - poly: 0x5935
        - init: 0x0000
        - xorout: 0x0000
        - refin: False
        - refout: False

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def opensafety_b(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-16 checksum of data with the `opensafety b` algorithm.

    Algorithm parameters:
        - poly: 0x755b
        - init: 0x0000
        - xorout: 0x0000
        - refin: False
        - refout: False

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def profibus(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-16 checksum of data with the `profibus` algorithm.

    Algorithm parameters:
        - poly: 0x1dcf
        - init: 0xffff
        - xorout: 0xffff
        - refin: False
        - refout: False

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def riello(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-16 checksum of data with the `riello` algorithm.

    Algorithm parameters:
        - poly: 0x1021
        - init: 0xb2aa
        - xorout: 0x0000
        - refin: True
        - refout: True

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def spi_fujitsu(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-16 checksum of data with the `spi fujitsu` algorithm.

    Algorithm parameters:
        - poly: 0x1021
        - init: 0x1d0f
        - xorout: 0x0000
        - refin: False
        - refout: False

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def t10_dif(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-16 checksum of data with the `t10 dif` algorithm.

    Algorithm parameters:
        - poly: 0x8bb7
        - init: 0x0000
        - xorout: 0x0000
        - refin: False
        - refout: False

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def teledisk(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-16 checksum of data with the `teledisk` algorithm.

    Algorithm parameters:
        - poly: 0xa097
        - init: 0x0000
        - xorout: 0x0000
        - refin: False
        - refout: False

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def tms37157(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-16 checksum of data with the `tms37157` algorithm.

    Algorithm parameters:
        - poly: 0x1021
        - init: 0x89ec
        - xorout: 0x0000
        - refin: True
        - refout: True

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def umts(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-16 checksum of data with the `umts` algorithm.

    Algorithm parameters:
        - poly: 0x8005
        - init: 0x0000
        - xorout: 0x0000
        - refin: False
        - refout: False

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def usb(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-16 checksum of data with the `usb` algorithm.

    Algorithm parameters:
        - poly: 0x8005
        - init: 0xffff
        - xorout: 0xffff
        - refin: True
        - refout: True

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def xmodem(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-16 checksum of data with the `xmodem` algorithm.

    Algorithm parameters:
        - poly: 0x1021
        - init: 0x0000
        - xorout: 0x0000
        - refin: False
        - refout: False

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """

def ibm_refin(data: Buffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-16 checksum of data with the `ibm refin` algorithm.

    **This method may be removed in the future.**

    Algorithm parameters:
        - poly: 0x8005
        - init: 0x0000
        - xorout: 0x0000
        - refin: True
        - refout: False

    :param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed
    :param Optional[int] initial: The optional starting value of the checksum
    :return: The checksum
    :rtype: int
    :raises TypeError: if the data is not a bytes-like object
    """
