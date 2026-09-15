//! Python bindings for fast CRC computation.
//!
//! CRC-16, CRC-32 and CRC-64 variants are computed with the `crc-fast` crate,
//! which folds with SIMD carry-less multiplication (PCLMULQDQ / VPCLMULQDQ on
//! x86, PMULL on aarch64) and falls back to lookup tables on other targets.
//! crc-fast only handles variants with `refin == refout`; the two experimental
//! variants with `refin = true, refout = false` are computed as the fully
//! reflected variant with the register bit-reversed on the way in and out.
//!
//! CRC-8 variants use slice-by-16 lookup tables built at compile time. For the
//! short inputs CRC-8 is typically used on, that beats the fixed setup cost of
//! the SIMD path.
use std::sync::OnceLock;

use crc_fast::{checksum, checksum_with_params, CrcAlgorithm, CrcParams, Digest};
use pyo3::exceptions::PyBufferError;
use pyo3::prelude::*;
use pyo3::types::PyBytes;
use pyo3::{ffi, wrap_pyfunction};

/// Rocksoft-model parameters of a CRC variant, as listed in the reveng CRC
/// catalogue (<https://reveng.sourceforge.io/crc-catalogue/all.htm>).
struct Params {
    width: u8,
    poly: u64,
    init: u64,
    refin: bool,
    refout: bool,
    xorout: u64,
    check: u64,
}

#[rustfmt::skip]
mod params {
    use super::Params;

    pub const CRC_8_AUTOSAR:    Params = Params { width:  8, poly: 0x2f, init: 0xff, refin: false, refout: false, xorout: 0xff, check: 0xdf };
    pub const CRC_8_BLUETOOTH:  Params = Params { width:  8, poly: 0xa7, init: 0x00, refin: true , refout: true , xorout: 0x00, check: 0x26 };
    pub const CRC_8_CDMA2000:   Params = Params { width:  8, poly: 0x9b, init: 0xff, refin: false, refout: false, xorout: 0x00, check: 0xda };
    pub const CRC_8_DARC:       Params = Params { width:  8, poly: 0x39, init: 0x00, refin: true , refout: true , xorout: 0x00, check: 0x15 };
    pub const CRC_8_DVB_S2:     Params = Params { width:  8, poly: 0xd5, init: 0x00, refin: false, refout: false, xorout: 0x00, check: 0xbc };
    pub const CRC_8_GSM_A:      Params = Params { width:  8, poly: 0x1d, init: 0x00, refin: false, refout: false, xorout: 0x00, check: 0x37 };
    pub const CRC_8_GSM_B:      Params = Params { width:  8, poly: 0x49, init: 0x00, refin: false, refout: false, xorout: 0xff, check: 0x94 };
    pub const CRC_8_I_432_1:    Params = Params { width:  8, poly: 0x07, init: 0x00, refin: false, refout: false, xorout: 0x55, check: 0xa1 };
    pub const CRC_8_I_CODE:     Params = Params { width:  8, poly: 0x1d, init: 0xfd, refin: false, refout: false, xorout: 0x00, check: 0x7e };
    pub const CRC_8_LTE:        Params = Params { width:  8, poly: 0x9b, init: 0x00, refin: false, refout: false, xorout: 0x00, check: 0xea };
    pub const CRC_8_MAXIM_DOW:  Params = Params { width:  8, poly: 0x31, init: 0x00, refin: true , refout: true , xorout: 0x00, check: 0xa1 };
    pub const CRC_8_MIFARE_MAD: Params = Params { width:  8, poly: 0x1d, init: 0xc7, refin: false, refout: false, xorout: 0x00, check: 0x99 };
    pub const CRC_8_NRSC_5:     Params = Params { width:  8, poly: 0x31, init: 0xff, refin: false, refout: false, xorout: 0x00, check: 0xf7 };
    pub const CRC_8_OPENSAFETY: Params = Params { width:  8, poly: 0x2f, init: 0x00, refin: false, refout: false, xorout: 0x00, check: 0x3e };
    pub const CRC_8_ROHC:       Params = Params { width:  8, poly: 0x07, init: 0xff, refin: true , refout: true , xorout: 0x00, check: 0xd0 };
    pub const CRC_8_SAE_J1850:  Params = Params { width:  8, poly: 0x1d, init: 0xff, refin: false, refout: false, xorout: 0xff, check: 0x4b };
    pub const CRC_8_SMBUS:      Params = Params { width:  8, poly: 0x07, init: 0x00, refin: false, refout: false, xorout: 0x00, check: 0xf4 };
    pub const CRC_8_TECH_3250:  Params = Params { width:  8, poly: 0x1d, init: 0xff, refin: true , refout: true , xorout: 0x00, check: 0x97 };
    pub const CRC_8_WCDMA:      Params = Params { width:  8, poly: 0x9b, init: 0x00, refin: true , refout: true , xorout: 0x00, check: 0x25 };

    pub const CRC_16_ARC:               Params = Params { width: 16, poly: 0x8005, init: 0x0000, refin: true , refout: true , xorout: 0x0000, check: 0xbb3d };
    pub const CRC_16_CDMA2000:          Params = Params { width: 16, poly: 0xc867, init: 0xffff, refin: false, refout: false, xorout: 0x0000, check: 0x4c06 };
    pub const CRC_16_CMS:               Params = Params { width: 16, poly: 0x8005, init: 0xffff, refin: false, refout: false, xorout: 0x0000, check: 0xaee7 };
    pub const CRC_16_DDS_110:           Params = Params { width: 16, poly: 0x8005, init: 0x800d, refin: false, refout: false, xorout: 0x0000, check: 0x9ecf };
    pub const CRC_16_DECT_R:            Params = Params { width: 16, poly: 0x0589, init: 0x0000, refin: false, refout: false, xorout: 0x0001, check: 0x007e };
    pub const CRC_16_DECT_X:            Params = Params { width: 16, poly: 0x0589, init: 0x0000, refin: false, refout: false, xorout: 0x0000, check: 0x007f };
    pub const CRC_16_DNP:               Params = Params { width: 16, poly: 0x3d65, init: 0x0000, refin: true , refout: true , xorout: 0xffff, check: 0xea82 };
    pub const CRC_16_EN_13757:          Params = Params { width: 16, poly: 0x3d65, init: 0x0000, refin: false, refout: false, xorout: 0xffff, check: 0xc2b7 };
    pub const CRC_16_GENIBUS:           Params = Params { width: 16, poly: 0x1021, init: 0xffff, refin: false, refout: false, xorout: 0xffff, check: 0xd64e };
    pub const CRC_16_GSM:               Params = Params { width: 16, poly: 0x1021, init: 0x0000, refin: false, refout: false, xorout: 0xffff, check: 0xce3c };
    pub const CRC_16_IBM_3740:          Params = Params { width: 16, poly: 0x1021, init: 0xffff, refin: false, refout: false, xorout: 0x0000, check: 0x29b1 };
    pub const CRC_16_IBM_SDLC:          Params = Params { width: 16, poly: 0x1021, init: 0xffff, refin: true , refout: true , xorout: 0xffff, check: 0x906e };
    pub const CRC_16_ISO_IEC_14443_3_A: Params = Params { width: 16, poly: 0x1021, init: 0xc6c6, refin: true , refout: true , xorout: 0x0000, check: 0xbf05 };
    pub const CRC_16_KERMIT:            Params = Params { width: 16, poly: 0x1021, init: 0x0000, refin: true , refout: true , xorout: 0x0000, check: 0x2189 };
    pub const CRC_16_LJ1200:            Params = Params { width: 16, poly: 0x6f63, init: 0x0000, refin: false, refout: false, xorout: 0x0000, check: 0xbdf4 };
    pub const CRC_16_MAXIM_DOW:         Params = Params { width: 16, poly: 0x8005, init: 0x0000, refin: true , refout: true , xorout: 0xffff, check: 0x44c2 };
    pub const CRC_16_MCRF4XX:           Params = Params { width: 16, poly: 0x1021, init: 0xffff, refin: true , refout: true , xorout: 0x0000, check: 0x6f91 };
    pub const CRC_16_MODBUS:            Params = Params { width: 16, poly: 0x8005, init: 0xffff, refin: true , refout: true , xorout: 0x0000, check: 0x4b37 };
    pub const CRC_16_NRSC_5:            Params = Params { width: 16, poly: 0x080b, init: 0xffff, refin: true , refout: true , xorout: 0x0000, check: 0xa066 };
    pub const CRC_16_OPENSAFETY_A:      Params = Params { width: 16, poly: 0x5935, init: 0x0000, refin: false, refout: false, xorout: 0x0000, check: 0x5d38 };
    pub const CRC_16_OPENSAFETY_B:      Params = Params { width: 16, poly: 0x755b, init: 0x0000, refin: false, refout: false, xorout: 0x0000, check: 0x20fe };
    pub const CRC_16_PROFIBUS:          Params = Params { width: 16, poly: 0x1dcf, init: 0xffff, refin: false, refout: false, xorout: 0xffff, check: 0xa819 };
    pub const CRC_16_RIELLO:            Params = Params { width: 16, poly: 0x1021, init: 0xb2aa, refin: true , refout: true , xorout: 0x0000, check: 0x63d0 };
    pub const CRC_16_SPI_FUJITSU:       Params = Params { width: 16, poly: 0x1021, init: 0x1d0f, refin: false, refout: false, xorout: 0x0000, check: 0xe5cc };
    pub const CRC_16_T10_DIF:           Params = Params { width: 16, poly: 0x8bb7, init: 0x0000, refin: false, refout: false, xorout: 0x0000, check: 0xd0db };
    pub const CRC_16_TELEDISK:          Params = Params { width: 16, poly: 0xa097, init: 0x0000, refin: false, refout: false, xorout: 0x0000, check: 0x0fb3 };
    pub const CRC_16_TMS37157:          Params = Params { width: 16, poly: 0x1021, init: 0x89ec, refin: true , refout: true , xorout: 0x0000, check: 0x26b1 };
    pub const CRC_16_UMTS:              Params = Params { width: 16, poly: 0x8005, init: 0x0000, refin: false, refout: false, xorout: 0x0000, check: 0xfee8 };
    pub const CRC_16_USB:               Params = Params { width: 16, poly: 0x8005, init: 0xffff, refin: true , refout: true , xorout: 0xffff, check: 0xb4c8 };
    pub const CRC_16_XMODEM:            Params = Params { width: 16, poly: 0x1021, init: 0x0000, refin: false, refout: false, xorout: 0x0000, check: 0x31c3 };
    pub const CRC_16_IBM_REFIN:         Params = Params { width: 16, poly: 0x8005, init: 0x0000, refin: true , refout: false, xorout: 0x0000, check: 0xbcdd };

    pub const CRC_32_AIXM:                        Params = Params { width: 32, poly: 0x814141ab, init: 0x00000000, refin: false, refout: false, xorout: 0x00000000, check: 0x3010bf7f };
    pub const CRC_32_AUTOSAR:                     Params = Params { width: 32, poly: 0xf4acfb13, init: 0xffffffff, refin: true , refout: true , xorout: 0xffffffff, check: 0x1697d06a };
    pub const CRC_32_BASE91_D:                    Params = Params { width: 32, poly: 0xa833982b, init: 0xffffffff, refin: true , refout: true , xorout: 0xffffffff, check: 0x87315576 };
    pub const CRC_32_BZIP2:                       Params = Params { width: 32, poly: 0x04c11db7, init: 0xffffffff, refin: false, refout: false, xorout: 0xffffffff, check: 0xfc891918 };
    pub const CRC_32_CD_ROM_EDC:                  Params = Params { width: 32, poly: 0x8001801b, init: 0x00000000, refin: true , refout: true , xorout: 0x00000000, check: 0x6ec2edc4 };
    pub const CRC_32_CKSUM:                       Params = Params { width: 32, poly: 0x04c11db7, init: 0x00000000, refin: false, refout: false, xorout: 0xffffffff, check: 0x765e7680 };
    pub const CRC_32_ISCSI:                       Params = Params { width: 32, poly: 0x1edc6f41, init: 0xffffffff, refin: true , refout: true , xorout: 0xffffffff, check: 0xe3069283 };
    pub const CRC_32_ISO_HDLC:                    Params = Params { width: 32, poly: 0x04c11db7, init: 0xffffffff, refin: true , refout: true , xorout: 0xffffffff, check: 0xcbf43926 };
    pub const CRC_32_JAMCRC:                      Params = Params { width: 32, poly: 0x04c11db7, init: 0xffffffff, refin: true , refout: true , xorout: 0x00000000, check: 0x340bc6d9 };
    pub const CRC_32_MPEG_2:                      Params = Params { width: 32, poly: 0x04c11db7, init: 0xffffffff, refin: false, refout: false, xorout: 0x00000000, check: 0x0376e6e7 };
    pub const CRC_32_XFER:                        Params = Params { width: 32, poly: 0x000000af, init: 0x00000000, refin: false, refout: false, xorout: 0x00000000, check: 0xbd0be338 };
    pub const CRC_32_K_REVERSED_RECIPROCAL_REFIN: Params = Params { width: 32, poly: 0xba0dc66b, init: 0x00000000, refin: true , refout: false, xorout: 0x00000000, check: 0x949d7183 };

    pub const CRC_64_ECMA_182:   Params = Params { width: 64, poly: 0x42f0e1eba9ea3693, init: 0x0000000000000000, refin: false, refout: false, xorout: 0x0000000000000000, check: 0x6c40df5f0b497347 };
    pub const CRC_64_GO_ISO:     Params = Params { width: 64, poly: 0x000000000000001b, init: 0xffffffffffffffff, refin: true , refout: true , xorout: 0xffffffffffffffff, check: 0xb90956c775a41001 };
    pub const CRC_64_WE:         Params = Params { width: 64, poly: 0x42f0e1eba9ea3693, init: 0xffffffffffffffff, refin: false, refout: false, xorout: 0xffffffffffffffff, check: 0x62ec59e3f1a4f00a };
    pub const CRC_64_XZ:         Params = Params { width: 64, poly: 0x42f0e1eba9ea3693, init: 0xffffffffffffffff, refin: true , refout: true , xorout: 0xffffffffffffffff, check: 0x995dc9bbdf1939fa };
    pub const CRC_64_TMS570_ISO: Params = Params { width: 64, poly: 0x000000000000001b, init: 0x0000000000000000, refin: false, refout: false, xorout: 0x0000000000000000, check: 0xe4ffbea588933790 };
}
use params::*;

impl Params {
    /// Initial value of the CRC register in the form crc-fast keeps its state
    /// in: reflected for reflected variants, plain otherwise.
    const fn register_init(&self) -> u64 {
        if self.refin {
            self.init.reverse_bits() >> (64 - self.width)
        } else {
            self.init
        }
    }
}

/// Inputs shorter than this are computed byte by byte from a lookup table.
/// The SIMD path has a fixed setup cost of roughly 7-16 ns, the table path
/// costs about 1.5 ns per byte, so they break even around 8 bytes.
const SMALL_INPUT: usize = 8;

/// Byte-at-a-time lookup table for a CRC of width 16, 32 or 64. The state is
/// the CRC register in the same form crc-fast uses, so the two paths can be
/// mixed freely.
struct ByteTable {
    width: u8,
    reflected: bool,
    table: [u64; 256],
}

impl ByteTable {
    const fn new(width: u8, poly: u64, reflected: bool) -> Self {
        let mask = u64::MAX >> (64 - width);
        let mut table = [0u64; 256];
        let mut i = 0;
        while i < 256 {
            let mut crc;
            let mut bit = 0;
            if reflected {
                let poly = poly.reverse_bits() >> (64 - width);
                crc = i as u64;
                while bit < 8 {
                    crc = if crc & 1 != 0 {
                        (crc >> 1) ^ poly
                    } else {
                        crc >> 1
                    };
                    bit += 1;
                }
            } else {
                let top = 1u64 << (width - 1);
                crc = (i as u64) << (width - 8);
                while bit < 8 {
                    crc = if crc & top != 0 {
                        (crc << 1) ^ poly
                    } else {
                        crc << 1
                    } & mask;
                    bit += 1;
                }
            }
            table[i] = crc;
            i += 1;
        }
        Self {
            width,
            reflected,
            table,
        }
    }

    #[inline(always)]
    fn update(&self, mut state: u64, data: &[u8]) -> u64 {
        if self.reflected {
            for &byte in data {
                state = self.table[((state ^ byte as u64) & 0xff) as usize] ^ (state >> 8);
            }
        } else {
            let shift = self.width - 8;
            let mask = u64::MAX >> (64 - self.width);
            for &byte in data {
                state = self.table[(((state >> shift) ^ byte as u64) & 0xff) as usize]
                    ^ ((state << 8) & mask);
            }
        }
        state
    }
}

/// Inputs at least this large are processed with the GIL released so other
/// Python threads can run while the checksum is computed.
const DETACH_THRESHOLD: usize = 16 * 1024;

/// A borrowed, contiguous, read-only view of any object that supports the
/// buffer protocol, obtained the way CPython's `y*` argument format does it.
struct SimpleBuffer(ffi::Py_buffer);

impl SimpleBuffer {
    #[inline(always)]
    fn get(obj: &Bound<'_, PyAny>) -> PyResult<Self> {
        let mut view = std::mem::MaybeUninit::<ffi::Py_buffer>::uninit();
        // SAFETY: `PyObject_GetBuffer` fully initialises `view` when it
        // returns 0, and sets a Python exception otherwise.
        let rc =
            unsafe { ffi::PyObject_GetBuffer(obj.as_ptr(), view.as_mut_ptr(), ffi::PyBUF_SIMPLE) };
        if rc != 0 {
            return Err(PyErr::fetch(obj.py()));
        }
        let buffer = Self(unsafe { view.assume_init() });
        // A PyBUF_SIMPLE request may only succeed for C-contiguous data, but
        // PyPy 3.10 also exports strided memoryviews through it (as the first
        // `len` bytes of the underlying buffer) while still filling in shape
        // and strides, so check those. CPython and PyPy 3.11 refuse such
        // views themselves and leave `strides` NULL, which by the protocol
        // means C-contiguous, so they skip the call.
        // SAFETY: `buffer.0` is a fully initialised, still exported view.
        if !buffer.0.strides.is_null()
            && unsafe { ffi::PyBuffer_IsContiguous(&buffer.0, b'C' as std::ffi::c_char) } == 0
        {
            return Err(PyBufferError::new_err("buffer is not C-contiguous"));
        }
        Ok(buffer)
    }

    #[inline(always)]
    fn as_bytes(&self) -> &[u8] {
        if self.0.len == 0 {
            return &[];
        }
        // SAFETY: a simple buffer is contiguous, `len` bytes long and stays
        // valid until `PyBuffer_Release`, which happens when `self` drops.
        // Immutability during the borrow is the documented caller contract
        // (see `with_data`).
        unsafe { std::slice::from_raw_parts(self.0.buf as *const u8, self.0.len as usize) }
    }
}

impl Drop for SimpleBuffer {
    fn drop(&mut self) {
        // SAFETY: the view was filled in by a successful `PyObject_GetBuffer`
        // and is released exactly once, with the GIL held.
        unsafe { ffi::PyBuffer_Release(&mut self.0) }
    }
}

/// Runs `f` on the contents of `data`. `bytes` objects are borrowed directly;
/// anything else goes through the buffer protocol. Large inputs are processed
/// with the GIL released; the buffer export keeps the memory alive, and a
/// `bytearray` unresizable, for the duration.
///
/// Like `hashlib`, `zlib` and other zero-copy consumers, this borrows the
/// buffer as an immutable slice instead of copying it. The caller must not
/// write to a mutable buffer from another thread while its checksum is being
/// computed: that is a data race, undefined behaviour in Rust, and at best
/// produces a meaningless checksum. Copying would make every non-`bytes`
/// input roughly twice as slow, so the contract is documented instead.
#[inline(always)]
fn with_data<T: Send>(
    py: Python<'_>,
    data: &Bound<'_, PyAny>,
    f: impl FnOnce(&[u8]) -> T + Send,
) -> PyResult<T> {
    let buffer;
    let bytes: &[u8] = match data.cast::<PyBytes>() {
        Ok(bytes) => bytes.as_bytes(),
        Err(_) => {
            buffer = SimpleBuffer::get(data)?;
            buffer.as_bytes()
        }
    };
    Ok(if bytes.len() >= DETACH_THRESHOLD {
        py.detach(move || f(bytes))
    } else {
        f(bytes)
    })
}

/// Slice-by-16 tables for an 8-bit CRC: `tables[k][v]` is the register after
/// feeding byte `v` followed by `k` zero bytes into an all-zero register.
const fn crc8_tables(poly: u8, reflected: bool) -> [[u8; 256]; 16] {
    let mut tables = [[0u8; 256]; 16];
    let mut i = 0;
    while i < 256 {
        let mut crc = i as u8;
        let mut bit = 0;
        while bit < 8 {
            crc = if reflected {
                if crc & 1 != 0 {
                    (crc >> 1) ^ poly.reverse_bits()
                } else {
                    crc >> 1
                }
            } else if crc & 0x80 != 0 {
                (crc << 1) ^ poly
            } else {
                crc << 1
            };
            bit += 1;
        }
        tables[0][i] = crc;
        i += 1;
    }
    let mut k = 1;
    while k < 16 {
        let mut i = 0;
        while i < 256 {
            tables[k][i] = tables[0][tables[k - 1][i] as usize];
            i += 1;
        }
        k += 1;
    }
    tables
}

#[inline(always)]
fn crc8_update(mut crc: u8, tables: &[[u8; 256]; 16], data: &[u8]) -> u8 {
    let (chunks, remainder) = data.as_chunks::<16>();
    for c in chunks {
        // The lookup that depends on the previous `crc` goes last so the 15
        // independent lookups and XORs overlap with its load latency.
        crc = tables[0][c[15] as usize]
            ^ tables[1][c[14] as usize]
            ^ tables[2][c[13] as usize]
            ^ tables[3][c[12] as usize]
            ^ tables[4][c[11] as usize]
            ^ tables[5][c[10] as usize]
            ^ tables[6][c[9] as usize]
            ^ tables[7][c[8] as usize]
            ^ tables[8][c[7] as usize]
            ^ tables[9][c[6] as usize]
            ^ tables[10][c[5] as usize]
            ^ tables[11][c[4] as usize]
            ^ tables[12][c[3] as usize]
            ^ tables[13][c[2] as usize]
            ^ tables[14][c[1] as usize]
            ^ tables[15][(c[0] ^ crc) as usize];
    }
    for &byte in remainder {
        crc = tables[0][(byte ^ crc) as usize];
    }
    crc
}

// Shared tail of every function's docstring.
macro_rules! doc_tail {
    () => {
        "\n\n:param data: The data to be computed, any bytes-like object; a mutable buffer must not be modified by another thread while its checksum is computed\n:param Optional[int] initial: The optional starting value of the checksum\n:return: The checksum\n:rtype: int\n:raises TypeError: if the data is not a bytes-like object"
    };
}

// CRC-8 variants (`refin == refout`), slice-by-16 tables built at compile time.
macro_rules! define_crc8_fn {
    ($name:ident, $pyname:literal, $params:expr, $doc:expr) => {
        #[pyfunction]
        #[pyo3(name = $pyname, signature = (data, initial=None))]
        #[doc = concat!($doc, doc_tail!())]
        fn $name(py: Python<'_>, data: &Bound<'_, PyAny>, initial: Option<u8>) -> PyResult<u8> {
            const _: () = assert!($params.width == 8 && $params.refin == $params.refout);
            static TABLES: [[u8; 256]; 16] = crc8_tables($params.poly as u8, $params.refin);
            with_data(py, data, move |data| {
                let xorout = $params.xorout as u8;
                let start = match initial {
                    // `initial` is a previously returned checksum, i.e. the
                    // register with `xorout` already applied; undo it.
                    Some(value) => value ^ xorout,
                    None if $params.refin => ($params.init as u8).reverse_bits(),
                    None => $params.init as u8,
                };
                crc8_update(start, &TABLES, data) ^ xorout
            })
        }
    };
}

// Variants in crc-fast's catalogue.
macro_rules! define_fast_crc_fn {
    ($name:ident, $pyname:literal, $word:ty, $params:expr, $alg:expr, $doc:expr) => {
        #[pyfunction]
        #[pyo3(name = $pyname, signature = (data, initial=None))]
        #[doc = concat!($doc, doc_tail!())]
        fn $name(
            py: Python<'_>,
            data: &Bound<'_, PyAny>,
            initial: Option<$word>,
        ) -> PyResult<$word> {
            const _: () = assert!($params.refin == $params.refout);
            static BYTE_TABLE: ByteTable =
                ByteTable::new($params.width, $params.poly, $params.refin);
            with_data(py, data, move |data| {
                if data.len() < SMALL_INPUT {
                    let start = match initial {
                        Some(value) => (value as u64) ^ $params.xorout,
                        None => $params.register_init(),
                    };
                    return (BYTE_TABLE.update(start, data) ^ $params.xorout) as $word;
                }
                match initial {
                    // One-shot path: avoids copying `CrcParams` into a `Digest`.
                    None => checksum($alg, data) as $word,
                    Some(value) => {
                        let mut digest =
                            Digest::new_with_init_state($alg, (value as u64) ^ $params.xorout);
                        digest.update(data);
                        digest.finalize() as $word
                    }
                }
            })
        }
    };
}

// Variants outside crc-fast's catalogue with `refin == refout`; folding keys
// are generated once at first use.
macro_rules! define_custom_crc_fn {
    ($name:ident, $pyname:literal, $word:ty, $params:expr, $doc:expr) => {
        #[pyfunction]
        #[pyo3(name = $pyname, signature = (data, initial=None))]
        #[doc = concat!($doc, doc_tail!())]
        fn $name(
            py: Python<'_>,
            data: &Bound<'_, PyAny>,
            initial: Option<$word>,
        ) -> PyResult<$word> {
            const _: () = assert!($params.refin == $params.refout);
            static PARAMS: OnceLock<CrcParams> = OnceLock::new();
            let params = PARAMS.get_or_init(|| {
                CrcParams::new(
                    stringify!($name),
                    $params.width,
                    $params.poly,
                    $params.init,
                    $params.refin,
                    $params.xorout,
                    $params.check,
                )
            });
            static BYTE_TABLE: ByteTable =
                ByteTable::new($params.width, $params.poly, $params.refin);
            with_data(py, data, move |data| {
                if data.len() < SMALL_INPUT {
                    let start = match initial {
                        Some(value) => (value as u64) ^ $params.xorout,
                        None => $params.register_init(),
                    };
                    return (BYTE_TABLE.update(start, data) ^ $params.xorout) as $word;
                }
                let mut params = *params;
                if let Some(value) = initial {
                    params.init_algorithm = (value as u64) ^ $params.xorout;
                }
                checksum_with_params(params, data) as $word
            })
        }
    };
}

// Variants with `refin = true, refout = false`. A reflected register that is
// read out without reflection equals the fully reflected variant (same poly
// and init, no xorout) with its register bit-reversed, so run that variant
// and reverse on the way in and out.
macro_rules! define_refin_only_crc_fn {
    ($name:ident, $pyname:literal, $word:ty, $params:expr, $doc:expr) => {
        #[pyfunction]
        #[pyo3(name = $pyname, signature = (data, initial=None))]
        #[doc = concat!($doc, doc_tail!())]
        fn $name(
            py: Python<'_>,
            data: &Bound<'_, PyAny>,
            initial: Option<$word>,
        ) -> PyResult<$word> {
            const _: () = assert!($params.refin && !$params.refout);
            static PARAMS: OnceLock<CrcParams> = OnceLock::new();
            let params = PARAMS.get_or_init(|| {
                CrcParams::new(
                    stringify!($name),
                    $params.width,
                    $params.poly,
                    $params.init,
                    true,
                    0,
                    0,
                )
            });
            static BYTE_TABLE: ByteTable = ByteTable::new($params.width, $params.poly, true);
            with_data(py, data, move |data| {
                let xorout = $params.xorout as $word;
                // Checksum-form value of the initial register, when none was given.
                let start = initial.unwrap_or(($params.init as $word) ^ xorout);
                let state = (start ^ xorout).reverse_bits() as u64;
                let register = if data.len() < SMALL_INPUT {
                    BYTE_TABLE.update(state, data)
                } else {
                    let mut params = *params;
                    params.init_algorithm = state;
                    checksum_with_params(params, data)
                };
                (register as $word).reverse_bits() ^ xorout
            })
        }
    };
}

define_crc8_fn!(
    crc_8_autosar,
    "autosar",
    CRC_8_AUTOSAR,
    concat!(
        "Compute a CRC-8 checksum of data with the `autosar` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x2f\n",
        "    - init: 0xff\n",
        "    - xorout: 0xff\n",
        "    - refin: False\n",
        "    - refout: False",
    )
);
define_crc8_fn!(
    crc_8_bluetooth,
    "bluetooth",
    CRC_8_BLUETOOTH,
    concat!(
        "Compute a CRC-8 checksum of data with the `bluetooth` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0xa7\n",
        "    - init: 0x00\n",
        "    - xorout: 0x00\n",
        "    - refin: True\n",
        "    - refout: True",
    )
);
define_crc8_fn!(
    crc_8_cdma2000,
    "cdma2000",
    CRC_8_CDMA2000,
    concat!(
        "Compute a CRC-8 checksum of data with the `cdma2000` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x9b\n",
        "    - init: 0xff\n",
        "    - xorout: 0x00\n",
        "    - refin: False\n",
        "    - refout: False",
    )
);
define_crc8_fn!(
    crc_8_darc,
    "darc",
    CRC_8_DARC,
    concat!(
        "Compute a CRC-8 checksum of data with the `darc` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x39\n",
        "    - init: 0x00\n",
        "    - xorout: 0x00\n",
        "    - refin: True\n",
        "    - refout: True",
    )
);
define_crc8_fn!(
    crc_8_dvb_s2,
    "dvb_s2",
    CRC_8_DVB_S2,
    concat!(
        "Compute a CRC-8 checksum of data with the `dvb_s2` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0xd5\n",
        "    - init: 0x00\n",
        "    - xorout: 0x00\n",
        "    - refin: False\n",
        "    - refout: False",
    )
);
define_crc8_fn!(
    crc_8_gsm_a,
    "gsm_a",
    CRC_8_GSM_A,
    concat!(
        "Compute a CRC-8 checksum of data with the `gsm_a` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x1d\n",
        "    - init: 0x00\n",
        "    - xorout: 0x00\n",
        "    - refin: False\n",
        "    - refout: False",
    )
);
define_crc8_fn!(
    crc_8_gsm_b,
    "gsm_b",
    CRC_8_GSM_B,
    concat!(
        "Compute a CRC-8 checksum of data with the `gsm_b` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x49\n",
        "    - init: 0x00\n",
        "    - xorout: 0xff\n",
        "    - refin: False\n",
        "    - refout: False",
    )
);
define_crc8_fn!(
    crc_8_i_432_1,
    "i_432_1",
    CRC_8_I_432_1,
    concat!(
        "Compute a CRC-8 checksum of data with the `i_432_1` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x07\n",
        "    - init: 0x00\n",
        "    - xorout: 0x55\n",
        "    - refin: False\n",
        "    - refout: False",
    )
);
define_crc8_fn!(
    crc_8_i_code,
    "i_code",
    CRC_8_I_CODE,
    concat!(
        "Compute a CRC-8 checksum of data with the `i_code` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x1d\n",
        "    - init: 0xfd\n",
        "    - xorout: 0x00\n",
        "    - refin: False\n",
        "    - refout: False",
    )
);
define_crc8_fn!(
    crc_8_lte,
    "lte",
    CRC_8_LTE,
    concat!(
        "Compute a CRC-8 checksum of data with the `lte` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x9b\n",
        "    - init: 0x00\n",
        "    - xorout: 0x00\n",
        "    - refin: False\n",
        "    - refout: False",
    )
);
define_crc8_fn!(
    crc_8_maxim_dow,
    "maxim_dow",
    CRC_8_MAXIM_DOW,
    concat!(
        "Compute a CRC-8 checksum of data with the `maxim_dow` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x31\n",
        "    - init: 0x00\n",
        "    - xorout: 0x00\n",
        "    - refin: True\n",
        "    - refout: True",
    )
);
define_crc8_fn!(
    crc_8_mifare_mad,
    "mifare_mad",
    CRC_8_MIFARE_MAD,
    concat!(
        "Compute a CRC-8 checksum of data with the `mifare_mad` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x1d\n",
        "    - init: 0xc7\n",
        "    - xorout: 0x00\n",
        "    - refin: False\n",
        "    - refout: False",
    )
);
define_crc8_fn!(
    crc_8_nrsc_5,
    "nrsc_5",
    CRC_8_NRSC_5,
    concat!(
        "Compute a CRC-8 checksum of data with the `nrsc_5` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x31\n",
        "    - init: 0xff\n",
        "    - xorout: 0x00\n",
        "    - refin: False\n",
        "    - refout: False",
    )
);
define_crc8_fn!(
    crc_8_opensafety,
    "opensafety",
    CRC_8_OPENSAFETY,
    concat!(
        "Compute a CRC-8 checksum of data with the `opensafety` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x2f\n",
        "    - init: 0x00\n",
        "    - xorout: 0x00\n",
        "    - refin: False\n",
        "    - refout: False",
    )
);
define_crc8_fn!(
    crc_8_rohc,
    "rohc",
    CRC_8_ROHC,
    concat!(
        "Compute a CRC-8 checksum of data with the `rohc` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x07\n",
        "    - init: 0xff\n",
        "    - xorout: 0x00\n",
        "    - refin: True\n",
        "    - refout: True",
    )
);
define_crc8_fn!(
    crc_8_sae_j1850,
    "sae_j1850",
    CRC_8_SAE_J1850,
    concat!(
        "Compute a CRC-8 checksum of data with the `sae_j1850` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x1d\n",
        "    - init: 0xff\n",
        "    - xorout: 0xff\n",
        "    - refin: False\n",
        "    - refout: False",
    )
);
define_crc8_fn!(
    crc_8_smbus,
    "smbus",
    CRC_8_SMBUS,
    concat!(
        "Compute a CRC-8 checksum of data with the `smbus` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x07\n",
        "    - init: 0x00\n",
        "    - xorout: 0x00\n",
        "    - refin: False\n",
        "    - refout: False",
    )
);
define_crc8_fn!(
    crc_8_tech_3250,
    "tech_3250",
    CRC_8_TECH_3250,
    concat!(
        "Compute a CRC-8 checksum of data with the `tech_3250` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x1d\n",
        "    - init: 0xff\n",
        "    - xorout: 0x00\n",
        "    - refin: True\n",
        "    - refout: True",
    )
);
define_crc8_fn!(
    crc_8_wcdma,
    "wcdma",
    CRC_8_WCDMA,
    concat!(
        "Compute a CRC-8 checksum of data with the `wcdma` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x9b\n",
        "    - init: 0x00\n",
        "    - xorout: 0x00\n",
        "    - refin: True\n",
        "    - refout: True",
    )
);
define_fast_crc_fn!(
    crc_16_arc,
    "arc",
    u16,
    CRC_16_ARC,
    CrcAlgorithm::Crc16Arc,
    concat!(
        "Compute a CRC-16 checksum of data with the `arc` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x8005\n",
        "    - init: 0x0000\n",
        "    - xorout: 0x0000\n",
        "    - refin: True\n",
        "    - refout: True",
    )
);
define_fast_crc_fn!(
    crc_16_autosar,
    "autosar",
    u16,
    CRC_16_IBM_3740,
    CrcAlgorithm::Crc16Ibm3740,
    concat!(
        "Compute a CRC-16 checksum of data with the `autosar` algorithm.\n",
        "\n",
        "This is the CRC16 routine of the AUTOSAR CRC library, also known as CRC-16/CCITT-FALSE;\n",
        "it is the same algorithm as `ibm_3740`.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x1021\n",
        "    - init: 0xffff\n",
        "    - xorout: 0x0000\n",
        "    - refin: False\n",
        "    - refout: False",
    )
);
define_fast_crc_fn!(
    crc_16_cdma2000,
    "cdma2000",
    u16,
    CRC_16_CDMA2000,
    CrcAlgorithm::Crc16Cdma2000,
    concat!(
        "Compute a CRC-16 checksum of data with the `cdma2000` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0xc867\n",
        "    - init: 0xffff\n",
        "    - xorout: 0x0000\n",
        "    - refin: False\n",
        "    - refout: False",
    )
);
define_fast_crc_fn!(
    crc_16_cms,
    "cms",
    u16,
    CRC_16_CMS,
    CrcAlgorithm::Crc16Cms,
    concat!(
        "Compute a CRC-16 checksum of data with the `cms` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x8005\n",
        "    - init: 0xffff\n",
        "    - xorout: 0x0000\n",
        "    - refin: False\n",
        "    - refout: False",
    )
);
define_fast_crc_fn!(
    crc_16_dds_110,
    "dds_110",
    u16,
    CRC_16_DDS_110,
    CrcAlgorithm::Crc16Dds110,
    concat!(
        "Compute a CRC-16 checksum of data with the `dds 110` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x8005\n",
        "    - init: 0x800d\n",
        "    - xorout: 0x0000\n",
        "    - refin: False\n",
        "    - refout: False",
    )
);
define_fast_crc_fn!(
    crc_16_dect_r,
    "dect_r",
    u16,
    CRC_16_DECT_R,
    CrcAlgorithm::Crc16DectR,
    concat!(
        "Compute a CRC-16 checksum of data with the `dect r` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x0589\n",
        "    - init: 0x0000\n",
        "    - xorout: 0x0001\n",
        "    - refin: False\n",
        "    - refout: False",
    )
);
define_fast_crc_fn!(
    crc_16_dect_x,
    "dect_x",
    u16,
    CRC_16_DECT_X,
    CrcAlgorithm::Crc16DectX,
    concat!(
        "Compute a CRC-16 checksum of data with the `dect x` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x0589\n",
        "    - init: 0x0000\n",
        "    - xorout: 0x0000\n",
        "    - refin: False\n",
        "    - refout: False",
    )
);
define_fast_crc_fn!(
    crc_16_dnp,
    "dnp",
    u16,
    CRC_16_DNP,
    CrcAlgorithm::Crc16Dnp,
    concat!(
        "Compute a CRC-16 checksum of data with the `dnp` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x3d65\n",
        "    - init: 0x0000\n",
        "    - xorout: 0xffff\n",
        "    - refin: True\n",
        "    - refout: True",
    )
);
define_fast_crc_fn!(
    crc_16_en_13757,
    "en_13757",
    u16,
    CRC_16_EN_13757,
    CrcAlgorithm::Crc16En13757,
    concat!(
        "Compute a CRC-16 checksum of data with the `en 13757` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x3d65\n",
        "    - init: 0x0000\n",
        "    - xorout: 0xffff\n",
        "    - refin: False\n",
        "    - refout: False",
    )
);
define_fast_crc_fn!(
    crc_16_genibus,
    "genibus",
    u16,
    CRC_16_GENIBUS,
    CrcAlgorithm::Crc16Genibus,
    concat!(
        "Compute a CRC-16 checksum of data with the `genibus` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x1021\n",
        "    - init: 0xffff\n",
        "    - xorout: 0xffff\n",
        "    - refin: False\n",
        "    - refout: False",
    )
);
define_fast_crc_fn!(
    crc_16_gsm,
    "gsm",
    u16,
    CRC_16_GSM,
    CrcAlgorithm::Crc16Gsm,
    concat!(
        "Compute a CRC-16 checksum of data with the `gsm` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x1021\n",
        "    - init: 0x0000\n",
        "    - xorout: 0xffff\n",
        "    - refin: False\n",
        "    - refout: False",
    )
);
define_fast_crc_fn!(
    crc_16_ibm_3740,
    "ibm_3740",
    u16,
    CRC_16_IBM_3740,
    CrcAlgorithm::Crc16Ibm3740,
    concat!(
        "Compute a CRC-16 checksum of data with the `ibm 3740` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x1021\n",
        "    - init: 0xffff\n",
        "    - xorout: 0x0000\n",
        "    - refin: False\n",
        "    - refout: False",
    )
);
define_fast_crc_fn!(
    crc_16_ibm_sdlc,
    "ibm_sdlc",
    u16,
    CRC_16_IBM_SDLC,
    CrcAlgorithm::Crc16IbmSdlc,
    concat!(
        "Compute a CRC-16 checksum of data with the `ibm sdlc` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x1021\n",
        "    - init: 0xffff\n",
        "    - xorout: 0xffff\n",
        "    - refin: True\n",
        "    - refout: True",
    )
);
define_fast_crc_fn!(
    crc_16_iso_iec_14443_3_a,
    "iso_iec_14443_3_a",
    u16,
    CRC_16_ISO_IEC_14443_3_A,
    CrcAlgorithm::Crc16IsoIec144433A,
    concat!(
        "Compute a CRC-16 checksum of data with the `iso iec 14443 3 a` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x1021\n",
        "    - init: 0xc6c6\n",
        "    - xorout: 0x0000\n",
        "    - refin: True\n",
        "    - refout: True",
    )
);
define_fast_crc_fn!(
    crc_16_kermit,
    "kermit",
    u16,
    CRC_16_KERMIT,
    CrcAlgorithm::Crc16Kermit,
    concat!(
        "Compute a CRC-16 checksum of data with the `kermit` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x1021\n",
        "    - init: 0x0000\n",
        "    - xorout: 0x0000\n",
        "    - refin: True\n",
        "    - refout: True",
    )
);
define_fast_crc_fn!(
    crc_16_lj1200,
    "lj1200",
    u16,
    CRC_16_LJ1200,
    CrcAlgorithm::Crc16Lj1200,
    concat!(
        "Compute a CRC-16 checksum of data with the `lj1200` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x6f63\n",
        "    - init: 0x0000\n",
        "    - xorout: 0x0000\n",
        "    - refin: False\n",
        "    - refout: False",
    )
);
define_fast_crc_fn!(
    crc_16_maxim_dow,
    "maxim_dow",
    u16,
    CRC_16_MAXIM_DOW,
    CrcAlgorithm::Crc16MaximDow,
    concat!(
        "Compute a CRC-16 checksum of data with the `maxim dow` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x8005\n",
        "    - init: 0x0000\n",
        "    - xorout: 0xffff\n",
        "    - refin: True\n",
        "    - refout: True",
    )
);
define_fast_crc_fn!(
    crc_16_mcrf4xx,
    "mcrf4xx",
    u16,
    CRC_16_MCRF4XX,
    CrcAlgorithm::Crc16Mcrf4xx,
    concat!(
        "Compute a CRC-16 checksum of data with the `mcrf4xx` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x1021\n",
        "    - init: 0xffff\n",
        "    - xorout: 0x0000\n",
        "    - refin: True\n",
        "    - refout: True",
    )
);
define_fast_crc_fn!(
    crc_16_modbus,
    "modbus",
    u16,
    CRC_16_MODBUS,
    CrcAlgorithm::Crc16Modbus,
    concat!(
        "Compute a CRC-16 checksum of data with the `modbus` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x8005\n",
        "    - init: 0xffff\n",
        "    - xorout: 0x0000\n",
        "    - refin: True\n",
        "    - refout: True",
    )
);
define_fast_crc_fn!(
    crc_16_nrsc_5,
    "nrsc_5",
    u16,
    CRC_16_NRSC_5,
    CrcAlgorithm::Crc16Nrsc5,
    concat!(
        "Compute a CRC-16 checksum of data with the `nrsc 5` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x080b\n",
        "    - init: 0xffff\n",
        "    - xorout: 0x0000\n",
        "    - refin: True\n",
        "    - refout: True",
    )
);
define_fast_crc_fn!(
    crc_16_opensafety_a,
    "opensafety_a",
    u16,
    CRC_16_OPENSAFETY_A,
    CrcAlgorithm::Crc16OpensafetyA,
    concat!(
        "Compute a CRC-16 checksum of data with the `opensafety a` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x5935\n",
        "    - init: 0x0000\n",
        "    - xorout: 0x0000\n",
        "    - refin: False\n",
        "    - refout: False",
    )
);
define_fast_crc_fn!(
    crc_16_opensafety_b,
    "opensafety_b",
    u16,
    CRC_16_OPENSAFETY_B,
    CrcAlgorithm::Crc16OpensafetyB,
    concat!(
        "Compute a CRC-16 checksum of data with the `opensafety b` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x755b\n",
        "    - init: 0x0000\n",
        "    - xorout: 0x0000\n",
        "    - refin: False\n",
        "    - refout: False",
    )
);
define_fast_crc_fn!(
    crc_16_profibus,
    "profibus",
    u16,
    CRC_16_PROFIBUS,
    CrcAlgorithm::Crc16Profibus,
    concat!(
        "Compute a CRC-16 checksum of data with the `profibus` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x1dcf\n",
        "    - init: 0xffff\n",
        "    - xorout: 0xffff\n",
        "    - refin: False\n",
        "    - refout: False",
    )
);
define_fast_crc_fn!(
    crc_16_riello,
    "riello",
    u16,
    CRC_16_RIELLO,
    CrcAlgorithm::Crc16Riello,
    concat!(
        "Compute a CRC-16 checksum of data with the `riello` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x1021\n",
        "    - init: 0xb2aa\n",
        "    - xorout: 0x0000\n",
        "    - refin: True\n",
        "    - refout: True",
    )
);
define_fast_crc_fn!(
    crc_16_spi_fujitsu,
    "spi_fujitsu",
    u16,
    CRC_16_SPI_FUJITSU,
    CrcAlgorithm::Crc16SpiFujitsu,
    concat!(
        "Compute a CRC-16 checksum of data with the `spi fujitsu` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x1021\n",
        "    - init: 0x1d0f\n",
        "    - xorout: 0x0000\n",
        "    - refin: False\n",
        "    - refout: False",
    )
);
define_fast_crc_fn!(
    crc_16_t10_dif,
    "t10_dif",
    u16,
    CRC_16_T10_DIF,
    CrcAlgorithm::Crc16T10Dif,
    concat!(
        "Compute a CRC-16 checksum of data with the `t10 dif` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x8bb7\n",
        "    - init: 0x0000\n",
        "    - xorout: 0x0000\n",
        "    - refin: False\n",
        "    - refout: False",
    )
);
define_fast_crc_fn!(
    crc_16_teledisk,
    "teledisk",
    u16,
    CRC_16_TELEDISK,
    CrcAlgorithm::Crc16Teledisk,
    concat!(
        "Compute a CRC-16 checksum of data with the `teledisk` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0xa097\n",
        "    - init: 0x0000\n",
        "    - xorout: 0x0000\n",
        "    - refin: False\n",
        "    - refout: False",
    )
);
define_fast_crc_fn!(
    crc_16_tms37157,
    "tms37157",
    u16,
    CRC_16_TMS37157,
    CrcAlgorithm::Crc16Tms37157,
    concat!(
        "Compute a CRC-16 checksum of data with the `tms37157` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x1021\n",
        "    - init: 0x89ec\n",
        "    - xorout: 0x0000\n",
        "    - refin: True\n",
        "    - refout: True",
    )
);
define_fast_crc_fn!(
    crc_16_umts,
    "umts",
    u16,
    CRC_16_UMTS,
    CrcAlgorithm::Crc16Umts,
    concat!(
        "Compute a CRC-16 checksum of data with the `umts` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x8005\n",
        "    - init: 0x0000\n",
        "    - xorout: 0x0000\n",
        "    - refin: False\n",
        "    - refout: False",
    )
);
define_fast_crc_fn!(
    crc_16_usb,
    "usb",
    u16,
    CRC_16_USB,
    CrcAlgorithm::Crc16Usb,
    concat!(
        "Compute a CRC-16 checksum of data with the `usb` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x8005\n",
        "    - init: 0xffff\n",
        "    - xorout: 0xffff\n",
        "    - refin: True\n",
        "    - refout: True",
    )
);
define_fast_crc_fn!(
    crc_16_xmodem,
    "xmodem",
    u16,
    CRC_16_XMODEM,
    CrcAlgorithm::Crc16Xmodem,
    concat!(
        "Compute a CRC-16 checksum of data with the `xmodem` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x1021\n",
        "    - init: 0x0000\n",
        "    - xorout: 0x0000\n",
        "    - refin: False\n",
        "    - refout: False",
    )
);
define_fast_crc_fn!(
    crc_32_aixm,
    "aixm",
    u32,
    CRC_32_AIXM,
    CrcAlgorithm::Crc32Aixm,
    concat!(
        "Compute a CRC-32 checksum of data with the `aixm` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x814141ab\n",
        "    - init: 0x00000000\n",
        "    - xorout: 0x00000000\n",
        "    - refin: False\n",
        "    - refout: False",
    )
);
define_fast_crc_fn!(
    crc_32_autosar,
    "autosar",
    u32,
    CRC_32_AUTOSAR,
    CrcAlgorithm::Crc32Autosar,
    concat!(
        "Compute a CRC-32 checksum of data with the `autosar` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0xf4acfb13\n",
        "    - init: 0xffffffff\n",
        "    - xorout: 0xffffffff\n",
        "    - refin: True\n",
        "    - refout: True",
    )
);
define_fast_crc_fn!(
    crc_32_base91_d,
    "base91_d",
    u32,
    CRC_32_BASE91_D,
    CrcAlgorithm::Crc32Base91D,
    concat!(
        "Compute a CRC-32 checksum of data with the `base91 d` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0xa833982b\n",
        "    - init: 0xffffffff\n",
        "    - xorout: 0xffffffff\n",
        "    - refin: True\n",
        "    - refout: True",
    )
);
define_fast_crc_fn!(
    crc_32_bzip2,
    "bzip2",
    u32,
    CRC_32_BZIP2,
    CrcAlgorithm::Crc32Bzip2,
    concat!(
        "Compute a CRC-32 checksum of data with the `bzip2` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x04c11db7\n",
        "    - init: 0xffffffff\n",
        "    - xorout: 0xffffffff\n",
        "    - refin: False\n",
        "    - refout: False",
    )
);
define_fast_crc_fn!(
    crc_32_cd_rom_edc,
    "cd_rom_edc",
    u32,
    CRC_32_CD_ROM_EDC,
    CrcAlgorithm::Crc32CdRomEdc,
    concat!(
        "Compute a CRC-32 checksum of data with the `cd rom edc` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x8001801b\n",
        "    - init: 0x00000000\n",
        "    - xorout: 0x00000000\n",
        "    - refin: True\n",
        "    - refout: True",
    )
);
define_fast_crc_fn!(
    crc_32_cksum,
    "cksum",
    u32,
    CRC_32_CKSUM,
    CrcAlgorithm::Crc32Cksum,
    concat!(
        "Compute a CRC-32 checksum of data with the `cksum` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x04c11db7\n",
        "    - init: 0x00000000\n",
        "    - xorout: 0xffffffff\n",
        "    - refin: False\n",
        "    - refout: False",
    )
);
define_fast_crc_fn!(
    crc_32_iscsi,
    "iscsi",
    u32,
    CRC_32_ISCSI,
    CrcAlgorithm::Crc32Iscsi,
    concat!(
        "Compute a CRC-32 checksum of data with the `iscsi` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x1edc6f41\n",
        "    - init: 0xffffffff\n",
        "    - xorout: 0xffffffff\n",
        "    - refin: True\n",
        "    - refout: True",
    )
);
define_fast_crc_fn!(
    crc_32_iso_hdlc,
    "iso_hdlc",
    u32,
    CRC_32_ISO_HDLC,
    CrcAlgorithm::Crc32IsoHdlc,
    concat!(
        "Compute a CRC-32 checksum of data with the `iso hdlc` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x04c11db7\n",
        "    - init: 0xffffffff\n",
        "    - xorout: 0xffffffff\n",
        "    - refin: True\n",
        "    - refout: True",
    )
);
define_fast_crc_fn!(
    crc_32_jamcrc,
    "jamcrc",
    u32,
    CRC_32_JAMCRC,
    CrcAlgorithm::Crc32Jamcrc,
    concat!(
        "Compute a CRC-32 checksum of data with the `jamcrc` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x04c11db7\n",
        "    - init: 0xffffffff\n",
        "    - xorout: 0x00000000\n",
        "    - refin: True\n",
        "    - refout: True",
    )
);
define_fast_crc_fn!(
    crc_32_mpeg_2,
    "mpeg_2",
    u32,
    CRC_32_MPEG_2,
    CrcAlgorithm::Crc32Mpeg2,
    concat!(
        "Compute a CRC-32 checksum of data with the `mpeg 2` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x04c11db7\n",
        "    - init: 0xffffffff\n",
        "    - xorout: 0x00000000\n",
        "    - refin: False\n",
        "    - refout: False",
    )
);
define_fast_crc_fn!(
    crc_32_xfer,
    "xfer",
    u32,
    CRC_32_XFER,
    CrcAlgorithm::Crc32Xfer,
    concat!(
        "Compute a CRC-32 checksum of data with the `xfer` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x000000af\n",
        "    - init: 0x00000000\n",
        "    - xorout: 0x00000000\n",
        "    - refin: False\n",
        "    - refout: False",
    )
);
define_fast_crc_fn!(
    crc_64_ecma_182,
    "ecma_182",
    u64,
    CRC_64_ECMA_182,
    CrcAlgorithm::Crc64Ecma182,
    concat!(
        "Compute a CRC-64 checksum of data with the `ecma 182` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x42f0e1eba9ea3693\n",
        "    - init: 0x0000000000000000\n",
        "    - xorout: 0x0000000000000000\n",
        "    - refin: False\n",
        "    - refout: False",
    )
);
define_fast_crc_fn!(
    crc_64_go_iso,
    "go_iso",
    u64,
    CRC_64_GO_ISO,
    CrcAlgorithm::Crc64GoIso,
    concat!(
        "Compute a CRC-64 checksum of data with the `go iso` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x000000000000001b\n",
        "    - init: 0xffffffffffffffff\n",
        "    - xorout: 0xffffffffffffffff\n",
        "    - refin: True\n",
        "    - refout: True",
    )
);
define_fast_crc_fn!(
    crc_64_we,
    "we",
    u64,
    CRC_64_WE,
    CrcAlgorithm::Crc64We,
    concat!(
        "Compute a CRC-64 checksum of data with the `we` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x42f0e1eba9ea3693\n",
        "    - init: 0xffffffffffffffff\n",
        "    - xorout: 0xffffffffffffffff\n",
        "    - refin: False\n",
        "    - refout: False",
    )
);
define_fast_crc_fn!(
    crc_64_xz,
    "xz",
    u64,
    CRC_64_XZ,
    CrcAlgorithm::Crc64Xz,
    concat!(
        "Compute a CRC-64 checksum of data with the `xz` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x42f0e1eba9ea3693\n",
        "    - init: 0xffffffffffffffff\n",
        "    - xorout: 0xffffffffffffffff\n",
        "    - refin: True\n",
        "    - refout: True",
    )
);
define_refin_only_crc_fn!(
    crc_16_ibm_refin,
    "ibm_refin",
    u16,
    CRC_16_IBM_REFIN,
    concat!(
        "Compute a CRC-16 checksum of data with the `ibm refin` algorithm.\n",
        "\n",
        "**This method may be removed in the future.**\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x8005\n",
        "    - init: 0x0000\n",
        "    - xorout: 0x0000\n",
        "    - refin: True\n",
        "    - refout: False",
    )
);
define_refin_only_crc_fn!(
    crc_32_k_reversed_reciprocal_refin,
    "k_reversed_reciprocal_refin",
    u32,
    CRC_32_K_REVERSED_RECIPROCAL_REFIN,
    concat!(
        "Compute a CRC-32 checksum of data with the `k reversed reciprocal refin` algorithm.\n",
        "\n",
        "**This method may be removed in the future.**\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0xba0dc66b\n",
        "    - init: 0x00000000\n",
        "    - xorout: 0x00000000\n",
        "    - refin: True\n",
        "    - refout: False",
    )
);
define_custom_crc_fn!(
    crc_64_tms570_iso,
    "tms570_iso",
    u64,
    CRC_64_TMS570_ISO,
    concat!(
        "Compute a CRC-64 checksum of data with the `tms570_iso` algorithm.\n",
        "\n",
        "Algorithm parameters:\n",
        "    - poly: 0x000000000000001b\n",
        "    - init: 0x0000000000000000\n",
        "    - xorout: 0x0000000000000000\n",
        "    - refin: False\n",
        "    - refout: False",
    )
);

#[pymodule(gil_used = false)]
fn fastcrc(py: Python<'_>, m: &Bound<'_, PyModule>) -> PyResult<()> {
    let crc8 = PyModule::new(py, "fastcrc.crc8")?;
    crc8.add_function(wrap_pyfunction!(crc_8_autosar, &crc8)?)?;
    crc8.add_function(wrap_pyfunction!(crc_8_bluetooth, &crc8)?)?;
    crc8.add_function(wrap_pyfunction!(crc_8_cdma2000, &crc8)?)?;
    crc8.add_function(wrap_pyfunction!(crc_8_darc, &crc8)?)?;
    crc8.add_function(wrap_pyfunction!(crc_8_dvb_s2, &crc8)?)?;
    crc8.add_function(wrap_pyfunction!(crc_8_gsm_a, &crc8)?)?;
    crc8.add_function(wrap_pyfunction!(crc_8_gsm_b, &crc8)?)?;
    crc8.add_function(wrap_pyfunction!(crc_8_i_432_1, &crc8)?)?;
    crc8.add_function(wrap_pyfunction!(crc_8_i_code, &crc8)?)?;
    crc8.add_function(wrap_pyfunction!(crc_8_lte, &crc8)?)?;
    crc8.add_function(wrap_pyfunction!(crc_8_maxim_dow, &crc8)?)?;
    crc8.add_function(wrap_pyfunction!(crc_8_mifare_mad, &crc8)?)?;
    crc8.add_function(wrap_pyfunction!(crc_8_nrsc_5, &crc8)?)?;
    crc8.add_function(wrap_pyfunction!(crc_8_opensafety, &crc8)?)?;
    crc8.add_function(wrap_pyfunction!(crc_8_rohc, &crc8)?)?;
    crc8.add_function(wrap_pyfunction!(crc_8_sae_j1850, &crc8)?)?;
    crc8.add_function(wrap_pyfunction!(crc_8_smbus, &crc8)?)?;
    crc8.add_function(wrap_pyfunction!(crc_8_tech_3250, &crc8)?)?;
    crc8.add_function(wrap_pyfunction!(crc_8_wcdma, &crc8)?)?;
    m.add("crc8", &crc8)?;

    let crc16 = PyModule::new(py, "fastcrc.crc16")?;
    crc16.add_function(wrap_pyfunction!(crc_16_arc, &crc16)?)?;
    crc16.add_function(wrap_pyfunction!(crc_16_autosar, &crc16)?)?;
    crc16.add_function(wrap_pyfunction!(crc_16_cdma2000, &crc16)?)?;
    crc16.add_function(wrap_pyfunction!(crc_16_cms, &crc16)?)?;
    crc16.add_function(wrap_pyfunction!(crc_16_dds_110, &crc16)?)?;
    crc16.add_function(wrap_pyfunction!(crc_16_dect_r, &crc16)?)?;
    crc16.add_function(wrap_pyfunction!(crc_16_dect_x, &crc16)?)?;
    crc16.add_function(wrap_pyfunction!(crc_16_dnp, &crc16)?)?;
    crc16.add_function(wrap_pyfunction!(crc_16_en_13757, &crc16)?)?;
    crc16.add_function(wrap_pyfunction!(crc_16_genibus, &crc16)?)?;
    crc16.add_function(wrap_pyfunction!(crc_16_gsm, &crc16)?)?;
    crc16.add_function(wrap_pyfunction!(crc_16_ibm_3740, &crc16)?)?;
    crc16.add_function(wrap_pyfunction!(crc_16_ibm_sdlc, &crc16)?)?;
    crc16.add_function(wrap_pyfunction!(crc_16_iso_iec_14443_3_a, &crc16)?)?;
    crc16.add_function(wrap_pyfunction!(crc_16_kermit, &crc16)?)?;
    crc16.add_function(wrap_pyfunction!(crc_16_lj1200, &crc16)?)?;
    crc16.add_function(wrap_pyfunction!(crc_16_maxim_dow, &crc16)?)?;
    crc16.add_function(wrap_pyfunction!(crc_16_mcrf4xx, &crc16)?)?;
    crc16.add_function(wrap_pyfunction!(crc_16_modbus, &crc16)?)?;
    crc16.add_function(wrap_pyfunction!(crc_16_nrsc_5, &crc16)?)?;
    crc16.add_function(wrap_pyfunction!(crc_16_opensafety_a, &crc16)?)?;
    crc16.add_function(wrap_pyfunction!(crc_16_opensafety_b, &crc16)?)?;
    crc16.add_function(wrap_pyfunction!(crc_16_profibus, &crc16)?)?;
    crc16.add_function(wrap_pyfunction!(crc_16_riello, &crc16)?)?;
    crc16.add_function(wrap_pyfunction!(crc_16_spi_fujitsu, &crc16)?)?;
    crc16.add_function(wrap_pyfunction!(crc_16_t10_dif, &crc16)?)?;
    crc16.add_function(wrap_pyfunction!(crc_16_teledisk, &crc16)?)?;
    crc16.add_function(wrap_pyfunction!(crc_16_tms37157, &crc16)?)?;
    crc16.add_function(wrap_pyfunction!(crc_16_umts, &crc16)?)?;
    crc16.add_function(wrap_pyfunction!(crc_16_usb, &crc16)?)?;
    crc16.add_function(wrap_pyfunction!(crc_16_xmodem, &crc16)?)?;
    crc16.add_function(wrap_pyfunction!(crc_16_ibm_refin, &crc16)?)?;
    m.add("crc16", &crc16)?;

    let crc32 = PyModule::new(py, "fastcrc.crc32")?;
    crc32.add_function(wrap_pyfunction!(crc_32_aixm, &crc32)?)?;
    crc32.add_function(wrap_pyfunction!(crc_32_autosar, &crc32)?)?;
    crc32.add_function(wrap_pyfunction!(crc_32_base91_d, &crc32)?)?;
    crc32.add_function(wrap_pyfunction!(crc_32_bzip2, &crc32)?)?;
    crc32.add_function(wrap_pyfunction!(crc_32_cd_rom_edc, &crc32)?)?;
    crc32.add_function(wrap_pyfunction!(crc_32_cksum, &crc32)?)?;
    crc32.add_function(wrap_pyfunction!(crc_32_iscsi, &crc32)?)?;
    crc32.add_function(wrap_pyfunction!(crc_32_iso_hdlc, &crc32)?)?;
    crc32.add_function(wrap_pyfunction!(crc_32_jamcrc, &crc32)?)?;
    crc32.add_function(wrap_pyfunction!(crc_32_mpeg_2, &crc32)?)?;
    crc32.add_function(wrap_pyfunction!(crc_32_xfer, &crc32)?)?;
    crc32.add_function(wrap_pyfunction!(
        crc_32_k_reversed_reciprocal_refin,
        &crc32
    )?)?;
    m.add("crc32", &crc32)?;

    let crc64 = PyModule::new(py, "fastcrc.crc64")?;
    crc64.add_function(wrap_pyfunction!(crc_64_ecma_182, &crc64)?)?;
    crc64.add_function(wrap_pyfunction!(crc_64_go_iso, &crc64)?)?;
    crc64.add_function(wrap_pyfunction!(crc_64_we, &crc64)?)?;
    crc64.add_function(wrap_pyfunction!(crc_64_xz, &crc64)?)?;
    crc64.add_function(wrap_pyfunction!(crc_64_tms570_iso, &crc64)?)?;
    m.add("crc64", &crc64)?;

    Ok(())
}
