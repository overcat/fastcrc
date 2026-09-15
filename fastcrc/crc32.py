"""
Compute a CRC-32 checksum of data.
"""
from .fastcrc import crc32 as _crc32

__all__ = [
    "algorithms_available",
    "algorithms_guaranteed",
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
    "k_reversed_reciprocal_refin",
]

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

aixm = _crc32.aixm
autosar = _crc32.autosar
base91_d = _crc32.base91_d
bzip2 = _crc32.bzip2
cd_rom_edc = _crc32.cd_rom_edc
cksum = _crc32.cksum
iscsi = _crc32.iscsi
iso_hdlc = _crc32.iso_hdlc
jamcrc = _crc32.jamcrc
mpeg_2 = _crc32.mpeg_2
xfer = _crc32.xfer
k_reversed_reciprocal_refin = _crc32.k_reversed_reciprocal_refin
