from mem_manager import MemManager
from mem_common import *
from mem_global_var import DDR_bandwidth


class MemConfig:
    def __init__(self, name):
        self._name = name
        self._mm = MemManager()

    @property
    def name(self):
        return self._name

    def pre_place_memory(self):
        return NotImplementedError

    def place_memory(self):
        self.pre_place_memory()
        self._mm.allocate_agent_memory()
        return self._get_ddr_mapping()

    @property
    def agent_list(self):
        return self._mm.agent_list

    def get_agent(self, agent_name):
        return self._mm.get_agent(agent_name)

    def calc_memory_usage(self, ddr_tag):
        used = 0
        for agent in self._mm.agent_list:
            if agent.ddr_op == DDROp.W and agent.allocated and agent.ddr_tag == ddr_tag or ddr_tag == DDRTag.NONE:
                used += agent.size
        if ddr_tag == DDRTag.NONE:
            unused = DDR_SIZE_BYTE * DDR_COUNT - used
        else:
            unused = DDR_SIZE_BYTE - used
        return (used / 1024 / 1024, unused / 1024 / 1024)

    def calc_bandwidth_usage(self, ddr_tag):
        used = 0
        for agent in self._mm.agent_list:
            if agent.ddr_tag == ddr_tag or ddr_tag == DDRTag.NONE:
                used += agent.bandwidth
        if ddr_tag == DDRTag.NONE:
            unused = DDR_bandwidth * 4 - used
        else:
            unused = DDR_bandwidth - used
        return (used / 1024 / 1024, unused / 1024 / 1024)

    def _get_ddr_mapping(self):
        """
        return list[[agent0_on_ddr0, agent1_on_ddr0], [agent0_on_ddr1], [], []]
        """
        mapping = [None] * 4
        for i in range(DDR_COUNT):
            agents = []
            for agent in self.agent_list:
                if agent.ddr_tag.value == i:
                    agents.append(agent)
            agents.sort()
            mapping[i] = agents
        return mapping

    def print_mapping(self, mapping):
        p_debug(">>> DDR Mapping Result <%s>" % self.name)
        for i, agents in enumerate(mapping):
            bandwidth_sum = 0
            size_sum = 0.0
            p_debug("%s" % DDRTag(i).name)
            p_debug("=" * 110)
            next_start = 0
            for agent in agents:
                if agent.unused:
                    continue
                if agent.ddr_op == DDROp.R:
                    p_debug("        %-32s| %s bandwidth:%8.2fM" % (agent.name, ' '*42, agent.bandwidth_m))
                else:
                    if agent.start_addr > next_start:
                        p_debug("        %-32s| [0x%08X - 0x%08X]| size:%8.2fM| bandwidth:%8.2fM" % (
                            '<SPACE>', next_start, agent.start_addr, (agent.start_addr - next_start) / 1024.0 / 1024.0, 0.0))
                    p_debug("        %-32s| [0x%08X - 0x%08X]| size:%8.2fM| bandwidth:%8.2fM" % (
                        agent.name, agent.start_addr, agent.end_addr, agent.size_m, agent.bandwidth_m))
                    next_start = agent.end_addr
                bandwidth_sum += agent.bandwidth
                size_sum += agent.size
            if DDR_SIZE_BYTE > next_start:
                p_debug("        %-32s| [0x%08X - 0x%08X]| size:%8.2fM| bandwidth:%8.2fM" % (
                    '<SPACE>', next_start, DDR_SIZE_BYTE, (DDR_SIZE_BYTE - next_start) / 1024.0 / 1024.0, 0.0))
            p_debug("-" * 110)
            p_debug("        %-32s| %s| size:%8.2fM| bandwidth:%8.2fM" % (
                '<TOTAL>', ' ' * 25, size_sum / 1024.0 / 1024.0, bandwidth_sum / 1024.0 / 1024.0))
            p_debug("        %-32s| %s| size:%8.2fM| bandwidth:%8.2fM" % (
                '<FREE>', ' ' * 25, (DDR_SIZE_BYTE - size_sum) / 1024.0 / 1024.0, (DDR_bandwidth - bandwidth_sum) / 1024 / 1024))
            p_debug("-" * 110)

    def print_registers(self, mapping):
        p_debug(">>> DDR Mapping Registers <%s>" % self.name)
        for i, agents in enumerate(mapping):
            p_debug("%s" % DDRTag(i).name)
            p_debug("=" * 110)
            next_start = 0
            for agent in agents:
                if agent.unused or agent.ddr_op == DDROp.R:
                    continue
                regs = agent.registers
                if not regs:
                    continue
                p_debug("Register for <%s>, count: %d" % (agent.name, len(regs)))
                p_debug("-" * 110)
                for j, reg in enumerate(regs):
                    p_debug("[%2d] %s" % (j, reg))
                p_debug("-" * 110)
