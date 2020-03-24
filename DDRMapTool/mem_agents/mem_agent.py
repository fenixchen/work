import math
from mem_common import DDRTag, DDROp, ddr_base_addr

class MemAgent:
    def __init__(self, name, mem_size, bandwidth, op):
        self._name = name
        self._op = op
        self._ddr_tag = DDRTag.NONE
        self._mem_size = math.ceil(mem_size * 1024)
        self._bandwidth = math.ceil(bandwidth  * 1024)
        self._start_addr = 0

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
        return "name:%s, ddr_tag:%s, start_addr:0x%08X, size:%.2fM" % (self._name, self._ddr_tag.name, self._start_addr, self.size_m)
