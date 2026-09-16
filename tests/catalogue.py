"""
The catalogue of algorithms fastcrc implements, which drives the test modules.

Every algorithm is listed with its Rocksoft-model parameters and its check value, the checksum
of ``b"123456789"``, as given in the reveng CRC catalogue
(https://reveng.sourceforge.io/crc-catalogue/all.htm); ``crc16.autosar`` is the AUTOSAR name
of CRC-16/IBM-3740. Three algorithms are not in the catalogue: ``crc64.tms570_iso`` is defined
by the C function in TI's application note SPNA235, which ``test_algorithms`` checks against,
and the experimental ``crc16.ibm_refin`` and ``crc32.k_reversed_reciprocal_refin`` are defined
by nothing but the parameters listed here, with check values computed by fastcrc itself.

``reference_crc`` computes the model bit by bit, independently of the extension, and
``public_functions`` lists what fastcrc exports so the tests can check that nothing is missing
from the catalogue.
"""
from typing import Callable, Dict, NamedTuple

import fastcrc

MODULES = ("crc8", "crc16", "crc32", "crc64")

CHECK_INPUT = b"123456789"


class Algorithm(NamedTuple):
    module: str
    name: str
    width: int
    poly: int
    init: int
    refin: bool
    refout: bool
    xorout: int
    check: int
    # Exported, but excluded from ``algorithms_guaranteed`` and may be removed.
    experimental: bool = False

    @property
    def function(self) -> Callable[..., int]:
        return getattr(getattr(fastcrc, self.module), self.name)

    def __str__(self) -> str:
        return f"{self.module}.{self.name}"


# fmt: off
CATALOGUE = [
    #          module   name           width poly  init  refin  refout xorout check
    Algorithm("crc8", "autosar",         8, 0x2f, 0xff, False, False, 0xff, 0xdf),
    Algorithm("crc8", "bluetooth",       8, 0xa7, 0x00, True,  True,  0x00, 0x26),
    Algorithm("crc8", "cdma2000",        8, 0x9b, 0xff, False, False, 0x00, 0xda),
    Algorithm("crc8", "darc",            8, 0x39, 0x00, True,  True,  0x00, 0x15),
    Algorithm("crc8", "dvb_s2",          8, 0xd5, 0x00, False, False, 0x00, 0xbc),
    Algorithm("crc8", "gsm_a",           8, 0x1d, 0x00, False, False, 0x00, 0x37),
    Algorithm("crc8", "gsm_b",           8, 0x49, 0x00, False, False, 0xff, 0x94),
    Algorithm("crc8", "i_432_1",         8, 0x07, 0x00, False, False, 0x55, 0xa1),
    Algorithm("crc8", "i_code",          8, 0x1d, 0xfd, False, False, 0x00, 0x7e),
    Algorithm("crc8", "lte",             8, 0x9b, 0x00, False, False, 0x00, 0xea),
    Algorithm("crc8", "maxim_dow",       8, 0x31, 0x00, True,  True,  0x00, 0xa1),
    Algorithm("crc8", "mifare_mad",      8, 0x1d, 0xc7, False, False, 0x00, 0x99),
    Algorithm("crc8", "nrsc_5",          8, 0x31, 0xff, False, False, 0x00, 0xf7),
    Algorithm("crc8", "opensafety",      8, 0x2f, 0x00, False, False, 0x00, 0x3e),
    Algorithm("crc8", "rohc",            8, 0x07, 0xff, True,  True,  0x00, 0xd0),
    Algorithm("crc8", "sae_j1850",       8, 0x1d, 0xff, False, False, 0xff, 0x4b),
    Algorithm("crc8", "smbus",           8, 0x07, 0x00, False, False, 0x00, 0xf4),
    Algorithm("crc8", "tech_3250",       8, 0x1d, 0xff, True,  True,  0x00, 0x97),
    Algorithm("crc8", "wcdma",           8, 0x9b, 0x00, True,  True,  0x00, 0x25),

    #          module    name                  width poly    init    refin  refout xorout  check
    Algorithm("crc16", "arc",                   16, 0x8005, 0x0000, True,  True,  0x0000, 0xbb3d),
    Algorithm("crc16", "autosar",               16, 0x1021, 0xffff, False, False, 0x0000, 0x29b1),
    Algorithm("crc16", "cdma2000",              16, 0xc867, 0xffff, False, False, 0x0000, 0x4c06),
    Algorithm("crc16", "cms",                   16, 0x8005, 0xffff, False, False, 0x0000, 0xaee7),
    Algorithm("crc16", "dds_110",               16, 0x8005, 0x800d, False, False, 0x0000, 0x9ecf),
    Algorithm("crc16", "dect_r",                16, 0x0589, 0x0000, False, False, 0x0001, 0x007e),
    Algorithm("crc16", "dect_x",                16, 0x0589, 0x0000, False, False, 0x0000, 0x007f),
    Algorithm("crc16", "dnp",                   16, 0x3d65, 0x0000, True,  True,  0xffff, 0xea82),
    Algorithm("crc16", "en_13757",              16, 0x3d65, 0x0000, False, False, 0xffff, 0xc2b7),
    Algorithm("crc16", "genibus",               16, 0x1021, 0xffff, False, False, 0xffff, 0xd64e),
    Algorithm("crc16", "gsm",                   16, 0x1021, 0x0000, False, False, 0xffff, 0xce3c),
    Algorithm("crc16", "ibm_3740",              16, 0x1021, 0xffff, False, False, 0x0000, 0x29b1),
    Algorithm("crc16", "ibm_sdlc",              16, 0x1021, 0xffff, True,  True,  0xffff, 0x906e),
    Algorithm("crc16", "iso_iec_14443_3_a",     16, 0x1021, 0xc6c6, True,  True,  0x0000, 0xbf05),
    Algorithm("crc16", "kermit",                16, 0x1021, 0x0000, True,  True,  0x0000, 0x2189),
    Algorithm("crc16", "lj1200",                16, 0x6f63, 0x0000, False, False, 0x0000, 0xbdf4),
    Algorithm("crc16", "maxim_dow",             16, 0x8005, 0x0000, True,  True,  0xffff, 0x44c2),
    Algorithm("crc16", "mcrf4xx",               16, 0x1021, 0xffff, True,  True,  0x0000, 0x6f91),
    Algorithm("crc16", "modbus",                16, 0x8005, 0xffff, True,  True,  0x0000, 0x4b37),
    Algorithm("crc16", "nrsc_5",                16, 0x080b, 0xffff, True,  True,  0x0000, 0xa066),
    Algorithm("crc16", "opensafety_a",          16, 0x5935, 0x0000, False, False, 0x0000, 0x5d38),
    Algorithm("crc16", "opensafety_b",          16, 0x755b, 0x0000, False, False, 0x0000, 0x20fe),
    Algorithm("crc16", "profibus",              16, 0x1dcf, 0xffff, False, False, 0xffff, 0xa819),
    Algorithm("crc16", "riello",                16, 0x1021, 0xb2aa, True,  True,  0x0000, 0x63d0),
    Algorithm("crc16", "spi_fujitsu",           16, 0x1021, 0x1d0f, False, False, 0x0000, 0xe5cc),
    Algorithm("crc16", "t10_dif",               16, 0x8bb7, 0x0000, False, False, 0x0000, 0xd0db),
    Algorithm("crc16", "teledisk",              16, 0xa097, 0x0000, False, False, 0x0000, 0x0fb3),
    Algorithm("crc16", "tms37157",              16, 0x1021, 0x89ec, True,  True,  0x0000, 0x26b1),
    Algorithm("crc16", "umts",                  16, 0x8005, 0x0000, False, False, 0x0000, 0xfee8),
    Algorithm("crc16", "usb",                   16, 0x8005, 0xffff, True,  True,  0xffff, 0xb4c8),
    Algorithm("crc16", "xmodem",                16, 0x1021, 0x0000, False, False, 0x0000, 0x31c3),
    # Experimental: reflected input, unreflected output.
    Algorithm("crc16", "ibm_refin",             16, 0x8005, 0x0000, True,  False, 0x0000, 0xbcdd, experimental=True),

    #          module    name                         width poly        init        refin  refout xorout      check
    Algorithm("crc32", "aixm",                        32, 0x814141ab, 0x00000000, False, False, 0x00000000, 0x3010bf7f),
    Algorithm("crc32", "autosar",                     32, 0xf4acfb13, 0xffffffff, True,  True,  0xffffffff, 0x1697d06a),
    Algorithm("crc32", "base91_d",                    32, 0xa833982b, 0xffffffff, True,  True,  0xffffffff, 0x87315576),
    Algorithm("crc32", "bzip2",                       32, 0x04c11db7, 0xffffffff, False, False, 0xffffffff, 0xfc891918),
    Algorithm("crc32", "cd_rom_edc",                  32, 0x8001801b, 0x00000000, True,  True,  0x00000000, 0x6ec2edc4),
    Algorithm("crc32", "cksum",                       32, 0x04c11db7, 0x00000000, False, False, 0xffffffff, 0x765e7680),
    Algorithm("crc32", "iscsi",                       32, 0x1edc6f41, 0xffffffff, True,  True,  0xffffffff, 0xe3069283),
    Algorithm("crc32", "iso_hdlc",                    32, 0x04c11db7, 0xffffffff, True,  True,  0xffffffff, 0xcbf43926),
    Algorithm("crc32", "jamcrc",                      32, 0x04c11db7, 0xffffffff, True,  True,  0x00000000, 0x340bc6d9),
    Algorithm("crc32", "mpeg_2",                      32, 0x04c11db7, 0xffffffff, False, False, 0x00000000, 0x0376e6e7),
    Algorithm("crc32", "xfer",                        32, 0x000000af, 0x00000000, False, False, 0x00000000, 0xbd0be338),
    # Experimental: reflected input, unreflected output.
    Algorithm("crc32", "k_reversed_reciprocal_refin", 32, 0xba0dc66b, 0x00000000, True,  False, 0x00000000, 0x949d7183, experimental=True),

    #          module    name        width poly                init                refin  refout xorout              check
    Algorithm("crc64", "ecma_182",   64, 0x42f0e1eba9ea3693, 0x0000000000000000, False, False, 0x0000000000000000, 0x6c40df5f0b497347),
    Algorithm("crc64", "go_iso",     64, 0x000000000000001b, 0xffffffffffffffff, True,  True,  0xffffffffffffffff, 0xb90956c775a41001),
    Algorithm("crc64", "we",         64, 0x42f0e1eba9ea3693, 0xffffffffffffffff, False, False, 0xffffffffffffffff, 0x62ec59e3f1a4f00a),
    Algorithm("crc64", "xz",         64, 0x42f0e1eba9ea3693, 0xffffffffffffffff, True,  True,  0xffffffffffffffff, 0x995dc9bbdf1939fa),
    Algorithm("crc64", "tms570_iso", 64, 0x000000000000001b, 0x0000000000000000, False, False, 0x0000000000000000, 0xe4ffbea588933790),
]
# fmt: on


def reflect(value: int, width: int) -> int:
    """Reverse the order of the low ``width`` bits of ``value``."""
    return int(f"{value:0{width}b}"[::-1], 2)


_REFLECTED_BYTES = [reflect(byte, 8) for byte in range(256)]


def reference_crc(algorithm: Algorithm, data: bytes) -> int:
    """
    The checksum of ``data``, computed bit by bit straight from the Rocksoft model.

    Slow, but obviously correct, and independent of any lookup table or SIMD trick.
    """
    width = algorithm.width
    mask = (1 << width) - 1
    top = 1 << (width - 1)
    register = algorithm.init
    for byte in data:
        if algorithm.refin:
            byte = _REFLECTED_BYTES[byte]
        register ^= byte << (width - 8)
        for _ in range(8):
            register = ((register << 1) ^ algorithm.poly) if register & top else register << 1
            register &= mask
    if algorithm.refout:
        register = reflect(register, width)
    return register ^ algorithm.xorout


def public_functions() -> Dict[str, Callable[..., int]]:
    """The checksum functions fastcrc exports, keyed like ``"crc16.xmodem"``."""
    functions = {}
    for module_name in MODULES:
        module = getattr(fastcrc, module_name)
        for name in module.__all__:
            if not name.startswith("algorithms_"):
                functions[f"{module_name}.{name}"] = getattr(module, name)
    return functions
