from dataclasses import dataclass


@dataclass
class Algorithm:
    poly: int
    init: int
    refin: bool
    refout: bool
    xorout: int
    check: int
    residue: int
