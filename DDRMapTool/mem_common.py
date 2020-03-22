
from enum import Enum
import math

DDR_SIZE = 256  # 256M DDR Size
DDR_COUNT = 4

DEBUG_ENABLE = True

def pdebug(*args, **kwargs):
    if DEBUG_ENABLE:
        print(*args, **kwargs)

def perror(*args, **kwargs):
    print("!!!", *args, **kwargs)

def ROUNDUP(val, digit):
    # pylint: disable=invalid-name
    return math.ceil(val)

def DEC2HEX(val):
    # pylint: disable=invalid-name
    return int(val)

def HEX2DEC(val):
    # pylint: disable=invalid-name
    return int(val)

class DDRTag(Enum):
    DDR1 = 0
    DDR2 = 1
    DDR3 = 2
    DDR4 = 3
    NONE = 4

class DDROp(Enum):
    R = 0
    W = 1


def ddr_base_addr(tag):
    return tag.value * DDR_SIZE * 1024 * 1024

class RegType(Enum):
    START = 0
    END = 1
    SIZE = 2
    OTHER = 3
    