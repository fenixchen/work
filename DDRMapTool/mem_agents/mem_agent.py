import math
from mem_common import *


class MemAgent:
    def __init__(self, name, module_name, op):
        self._name = name
        self._module_name = module_name
        self._op = op
        self._ddr_tag = DDRTag.NONE
        mem_size, bandwidth = self.calc_memory()
        self._mem_size = math.ceil(mem_size * 1024)
        self._bandwidth = math.ceil(bandwidth * 1024)
        self._start_addr = None
        self._end_addr = None
        self._block = None

    def calc_memory(self):
        raise NotImplementedError()

    @property
    def block(self):
        return self._block

    @block.setter
    def block(self, value):
        self._block = value

    @property
    def block_name(self):
        assert self._block is not None
        return self._block.name

    @property
    def module_name(self):
        return self._module_name

    @property
    def absolute_addr(self):
        return ddr_base_addr(self._ddr_tag) + self._start_addr

    @property
    def start_addr(self):
        return self._start_addr

    @start_addr.setter
    def start_addr(self, value):
        self._start_addr = value

    @property
    def end_addr(self):
        return self._end_addr

    @end_addr.setter
    def end_addr(self, value):
        self._end_addr = value

    @property
    def ddr_tag(self):
        return self._ddr_tag

    @ddr_tag.setter
    def ddr_tag(self, tag):
        self._ddr_tag = tag

    @property
    def bandwidth_m(self):
        return self._bandwidth / 1024.0

    @property
    def ddr_op(self):
        return self._op

    @property
    def op_str(self):
        if self._op == DDROp.R:
            return "R"
        else:
            return "W"

    @property
    def name(self):
        return self._name

    @property
    def size_m(self):
        return self._mem_size / 1024.0

    @property
    def size_k(self):
        return self._mem_size

    def get_regs(self, reg_dict):
        return NotImplementedError()

    def __str__(self):
        return "name:%s, %s, [0x%08X, 0x%08X], size:%.2fM, bandwidth:%.2fM" % (
            self._name, self._ddr_tag.name, self._start_addr, self._end_addr, self.size_m, self.bandwidth_m)
