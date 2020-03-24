import inspect
import os
from enum import Enum
import math

DDR_SIZE = 256  # 256M DDR Size
DDR_COUNT = 4

DEBUG_ENABLE = True

VERBOSE_ENABLE = False


def p_verbose(*args, **kwargs):
    if VERBOSE_ENABLE:
        caller = inspect.getframeinfo(inspect.stack()[1][0])
        print("[V][%s:%d] - " % (os.path.basename(caller.filename), caller.lineno), end='')
        print(*args, **kwargs)

def p_debug(*args, **kwargs):
    if DEBUG_ENABLE:
        caller = inspect.getframeinfo(inspect.stack()[1][0])
        print("[D][%s:%d] - " % (os.path.basename(caller.filename), caller.lineno), end='')
        print(*args, **kwargs)

def p_error(*args, **kwargs):    
    caller = inspect.getframeinfo(inspect.stack()[1][0])
    print("[E][%s:%d] - " % (os.path.basename(caller.filename), caller.lineno), end='')
    print(*args, **kwargs)

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
    
if __name__ == '__main__':
    p_verbose('verbose message')
    p_debug('debug message')
    p_error('error message')
    