# fastcrc

A hyper-fast Python module for computing CRC(16, 32, 64) checksum.
## Installation

```
pip install fastcrc
```
## Usage

```python
from fastcrc import crc16, crc32, crc64

data = b"123456789"
print(f"crc16 checksum with xmodem algorithm: {crc16.xmodem(data)}")
print(f"crc32 checksum with aixm algorithm: {crc32.aixm(data)}")
print(f"crc64 checksum with ecma_182 algorithm: {crc64.ecma_182(data)}")
```
## License

fastcrc is licensed under [MIT License](./LICENSE).

## Thanks

fastcrc is made possible by [crc-rs](https://github.com/mrhooray/crc-rs).