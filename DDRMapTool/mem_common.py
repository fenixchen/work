import inspect
import os
from enum import Enum
import math
import colorama

DEBUG_ENABLE = True
VERBOSE_ENABLE = False

colorama.init()


def p_verbose(*args, **kwargs):
    if VERBOSE_ENABLE:
        caller = inspect.getframeinfo(inspect.stack()[1][0])
        print(colorama.Style.DIM, end='')
        print("[V][%s:%3d] - " % (os.path.basename(caller.filename), caller.lineno), end='')
        print(*args, **kwargs)
        print(colorama.Style.RESET_ALL, end='')


def p_debug(*args, **kwargs):
    if DEBUG_ENABLE:
        caller = inspect.getframeinfo(inspect.stack()[1][0])
        print(colorama.Fore.GREEN, end='')
        print("[D][%s:%3d] - " % (os.path.basename(caller.filename), caller.lineno), end='')
        print(*args, **kwargs)
        print(colorama.Style.RESET_ALL, end='')


def p_warn(*args, **kwargs):
    caller = inspect.getframeinfo(inspect.stack()[1][0])
    print(colorama.Fore.YELLOW, end='')
    print("[E][%s:%3d] - " % (os.path.basename(caller.filename), caller.lineno), end='')
    print(*args, **kwargs)
    print(colorama.Style.RESET_ALL, end='')


def p_error(*args, **kwargs):
    caller = inspect.getframeinfo(inspect.stack()[1][0])
    print(colorama.Fore.RED, end='')
    print("[E][%s:%3d] - " % (os.path.basename(caller.filename), caller.lineno), end='')
    print(*args, **kwargs)
    print(colorama.Style.RESET_ALL, end='')


def ROUNDUP(val, digit=0):
    # pylint: disable=invalid-name
    return math.ceil(val)


def DEC2HEX(val):
    # pylint: disable=invalid-name
    return int(val)


def HEX2DEC(val):
    # pylint: disable=invalid-name
    return int(val)


def IF(cond, yes_val, no_val):
    # pylint: disable=invalid-name
    return yes_val if cond else no_val


class DDRTag(Enum):
    DDR1 = 0
    DDR2 = 1
    DDR3 = 2
    DDR4 = 3
    NONE = 4


class DDROp(Enum):
    R = 0
    W = 1


class RegType(Enum):
    START = 0
    END = 1
    SIZE = 2
    OTHER = 3


if __name__ == '__main__':
    p_verbose('verbose message')
    p_debug('debug message')
    p_error('error message')
