from mem_common import *


class MemReg:
    def __init__(self, name, addr, reg_type=RegType.OTHER, start_bit=0, end_bit=31):
        self._name = name
        self._addr = addr
        self._type = reg_type
        self._start_bit = start_bit
        self._end_bit = end_bit
        self._value = 0

    @property
    def name(self):
        return self._name

    @property
    def addr_str(self):
        if isinstance(self._addr, str):
            return self._addr
        else:
            return "0x%08X" % self._addr

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def __str__(self):
        if isinstance(self._addr, str):
            if self._start_bit != 0 or self._end_bit != 31:
                return "%-30s[%d:%d] <= 0x%08X" % (self._addr, self._start_bit, self._end_bit, self._value)
            else:
                return "%-30s <= 0x%08X" % (self._addr, self._value)
        else:
            if self._start_bit != 0 or self._end_bit != 31:
                return "0x%08X[%d:%d] <= 0x%08X" % (self._addr, self._start_bit, self._end_bit, self._value)
            else:
                return "0x%08X <= 0x%08X" % (self._addr, self._value)
