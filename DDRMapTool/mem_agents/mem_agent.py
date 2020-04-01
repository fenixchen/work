import functools
from mem_common import *
from mem_global_var import GV


@functools.total_ordering
class MemAgent:
    def __init__(self, name, module_name, op, write_agent_name=None):
        self._name = name
        self._module_name = module_name
        self._op = op
        self._write_agent_name = write_agent_name  # for R agent to detect DDR tag
        self._block = None
        self._ddr_tag = None
        self._start_addr = None
        self._end_addr = None
        self._mem_size = 0
        self.reset_memory()

    def reset_memory(self):
        self._ddr_tag = DDRTag.NONE
        mem_size, bandwidth = self.calc_memory()
        if self._op == DDROp.R and bandwidth != 0:
            assert self._write_agent_name is not None, "write_agent_name is None for non-empty read agent <%s>" % self._name
        self._mem_size = int(mem_size * 1024 * 1024)
        self._bandwidth = int(bandwidth * 1024 * 1024)
        self._start_addr = None
        self._end_addr = None

    def __eq__(self, other):
        if not isinstance(other, MemAgent):
            return False
        self_start_addr = 0 if self._start_addr is None else self._start_addr
        other_start_addr = 0 if other._start_addr is None else other._start_addr
        return (self._ddr_tag.value, self_start_addr, self._name) == (other._ddr_tag.value, other_start_addr, other._name)

    def __lt__(self, other):
        if not isinstance(other, MemAgent):
            return False
        self_start_addr = 0 if self._start_addr is None else self._start_addr
        other_start_addr = 0 if other._start_addr is None else other._start_addr
        return (self._ddr_tag.value, self_start_addr, self._name) < (other._ddr_tag.value, other_start_addr, other._name)

    @property
    def unused(self):
        return self._bandwidth == 0

    @property
    def allocated(self):
        if self._ddr_tag != DDRTag.NONE and self._start_addr is not None and self._end_addr is not None:
            return True
        else:
            return False

    @property
    def ddr_base_offset(self):
        assert self._ddr_tag != DDRTag.NONE
        return self._ddr_tag.value * GV.DDR_size_byte

    @property
    def debug_info(self):
        msg = 'Agent:<%s>\n' % self.name
        msg += 'DDR_TAG:%s\n' % self.ddr_tag.name
        if self._start_addr is None:
            msg += 'Start_addr:None\n'
        else:
            msg += 'Start_addr:0x%08X\n' % self._start_addr
        if self._end_addr is None:
            msg += 'End_addr:None\n'
        else:
            msg += 'End_addr:0x%08X\n' % self._end_addr
        return msg

    @property
    def alloc_info(self):
        return "%-20s: [0x%08X - 0x%08X], size:%.2fM" % (self.name, self._start_addr, self._end_addr, self.size_m)

    def calc_memory(self):
        """
        return (size, bandwidth)
        """
        raise NotImplementedError()

    @property
    def write_agent_name(self):
        return self._write_agent_name

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
    def start_addr(self):
        return self._start_addr

    @property
    def absolute_start_addr(self):
        return self.ddr_base_offset + self._start_addr

    @property
    def absolute_end_addr(self):
        return self.ddr_base_offset + self._end_addr

    def init_memory(self, ddr_tag, start_addr=None):
        """
        set a initial ddr tag and address
        """
        self._ddr_tag = ddr_tag
        self._start_addr = start_addr

    @property
    def end_addr(self):
        return self._end_addr

    @property
    def ddr_tag(self):
        return self._ddr_tag

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
    def size(self):
        return self._mem_size

    @property
    def size_m(self):
        return self._mem_size / 1024.0 / 1024.0

    @property
    def bandwidth(self):
        return self._bandwidth

    @property
    def bandwidth_m(self):
        return self._bandwidth / 1024.0 / 1024

    def __str__(self):
        return "name:%s, %s, [0x%08X, 0x%08X], size:%.2fM, bandwidth:%.2fM" % (
            self._name,
            self._ddr_tag.name,
            self._start_addr,
            self._end_addr,
            self.size_m,
            self.bandwidth_m)

    def allocate_memory(self, reg_dict):
        pass

    @property
    def registers(self):
        return []

    def set_memory_range(self, start_addr, end_addr, ddr_tag=None):
        assert start_addr is not None
        self._start_addr = start_addr

        if end_addr is None:
            assert self._mem_size is not None
            self._end_addr = ROUNDUP(start_addr + self._mem_size)
            p_verbose("Set end address of <%s> as start_addr(0x%08X) + size(%.2fM) = 0x%08X" % (
                self._name, self._start_addr, self.size_m, self._end_addr))
        else:
            self._end_addr = end_addr
            new_size = self.end_addr - self.start_addr
            if new_size > self._mem_size:
                p_verbose("Increase <%s> memory from %.2fM to end_addr(0x%08X) - start_addr(0x%08X) = %.2fM" % (
                    self._name, self.size_m, self.end_addr, self.start_addr, new_size / 1024.0 / 1024.0))
            self._mem_size = new_size
        if ddr_tag is not None:
            self._ddr_tag = ddr_tag
