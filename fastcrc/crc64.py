"""
Compute a CRC-64 checksum of data.
"""
from .fastcrc import crc64 as _crc64

__all__ = [
    "algorithms_available",
    "algorithms_guaranteed",
    "ecma_182",
    "go_iso",
    "we",
    "xz",
    "tms570_iso",
]

__always_supported = (
    "ecma_182",
    "go_iso",
    "we",
    "xz",
    "tms570_iso",
)

algorithms_guaranteed = set(__always_supported)
algorithms_available = set(__always_supported)

ecma_182 = _crc64.ecma_182
go_iso = _crc64.go_iso
we = _crc64.we
xz = _crc64.xz
tms570_iso = _crc64.tms570_iso
