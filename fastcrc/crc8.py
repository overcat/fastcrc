"""
Compute a CRC-8 checksum of data.
"""
from .fastcrc import crc8 as _crc8

__all__ = [
    "algorithms_available",
    "algorithms_guaranteed",
    "autosar",
    "bluetooth",
    "cdma2000",
    "darc",
    "dvb_s2",
    "gsm_a",
    "gsm_b",
    "i_432_1",
    "i_code",
    "lte",
    "maxim_dow",
    "mifare_mad",
    "nrsc_5",
    "opensafety",
    "rohc",
    "sae_j1850",
    "smbus",
    "tech_3250",
    "wcdma",
]

__always_supported = (
    "autosar",
    "bluetooth",
    "cdma2000",
    "darc",
    "dvb_s2",
    "gsm_a",
    "gsm_b",
    "i_432_1",
    "i_code",
    "lte",
    "maxim_dow",
    "mifare_mad",
    "nrsc_5",
    "opensafety",
    "rohc",
    "sae_j1850",
    "smbus",
    "tech_3250",
    "wcdma",
)

algorithms_guaranteed = set(__always_supported)
algorithms_available = set(__always_supported)

autosar = _crc8.autosar
bluetooth = _crc8.bluetooth
cdma2000 = _crc8.cdma2000
darc = _crc8.darc
dvb_s2 = _crc8.dvb_s2
gsm_a = _crc8.gsm_a
gsm_b = _crc8.gsm_b
i_432_1 = _crc8.i_432_1
i_code = _crc8.i_code
lte = _crc8.lte
maxim_dow = _crc8.maxim_dow
mifare_mad = _crc8.mifare_mad
nrsc_5 = _crc8.nrsc_5
opensafety = _crc8.opensafety
rohc = _crc8.rohc
sae_j1850 = _crc8.sae_j1850
smbus = _crc8.smbus
tech_3250 = _crc8.tech_3250
wcdma = _crc8.wcdma
