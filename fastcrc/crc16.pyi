from _typeshed import ReadableBuffer
from typing import Optional, Set

algorithms_guaranteed: Set[str]
algorithms_available: Set[str]

def arc(data: ReadableBuffer, initial: Optional[int] = None) -> int:
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

def autosar(data: ReadableBuffer, initial: Optional[int] = None) -> int:
    """
    Compute a CRC-16 checksum of data with the `autosar` algorithm.

    This is the CRC16 routine of the AUTOSAR CRC library, also known as CRC-16/CCITT-FALSE;
    it is the same algorithm as `ibm_3740`.

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

def cdma2000(data: ReadableBuffer, initial: Optional[int] = None) -> int:
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

def cms(data: ReadableBuffer, initial: Optional[int] = None) -> int:
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

def dds_110(data: ReadableBuffer, initial: Optional[int] = None) -> int:
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

def dect_r(data: ReadableBuffer, initial: Optional[int] = None) -> int:
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

def dect_x(data: ReadableBuffer, initial: Optional[int] = None) -> int:
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

def dnp(data: ReadableBuffer, initial: Optional[int] = None) -> int:
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

def en_13757(data: ReadableBuffer, initial: Optional[int] = None) -> int:
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

def genibus(data: ReadableBuffer, initial: Optional[int] = None) -> int:
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

def gsm(data: ReadableBuffer, initial: Optional[int] = None) -> int:
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

def ibm_3740(data: ReadableBuffer, initial: Optional[int] = None) -> int:
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

def ibm_sdlc(data: ReadableBuffer, initial: Optional[int] = None) -> int:
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

def iso_iec_14443_3_a(data: ReadableBuffer, initial: Optional[int] = None) -> int:
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

def kermit(data: ReadableBuffer, initial: Optional[int] = None) -> int:
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

def lj1200(data: ReadableBuffer, initial: Optional[int] = None) -> int:
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

def maxim_dow(data: ReadableBuffer, initial: Optional[int] = None) -> int:
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

def mcrf4xx(data: ReadableBuffer, initial: Optional[int] = None) -> int:
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

def modbus(data: ReadableBuffer, initial: Optional[int] = None) -> int:
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

def nrsc_5(data: ReadableBuffer, initial: Optional[int] = None) -> int:
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

def opensafety_a(data: ReadableBuffer, initial: Optional[int] = None) -> int:
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

def opensafety_b(data: ReadableBuffer, initial: Optional[int] = None) -> int:
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

def profibus(data: ReadableBuffer, initial: Optional[int] = None) -> int:
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

def riello(data: ReadableBuffer, initial: Optional[int] = None) -> int:
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

def spi_fujitsu(data: ReadableBuffer, initial: Optional[int] = None) -> int:
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

def t10_dif(data: ReadableBuffer, initial: Optional[int] = None) -> int:
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

def teledisk(data: ReadableBuffer, initial: Optional[int] = None) -> int:
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

def tms37157(data: ReadableBuffer, initial: Optional[int] = None) -> int:
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

def umts(data: ReadableBuffer, initial: Optional[int] = None) -> int:
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

def usb(data: ReadableBuffer, initial: Optional[int] = None) -> int:
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

def xmodem(data: ReadableBuffer, initial: Optional[int] = None) -> int:
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

def ibm_refin(data: ReadableBuffer, initial: Optional[int] = None) -> int:
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
