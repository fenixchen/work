from mem_common import *
from mem_global_var import GV


class MemAllocator():
    def __init__(self, ddr_tag):
        self._ddr_tag = ddr_tag
        self._used_bank_list = []
        self._request_agent_list = []
        self._free_block_list = []  # [(size, start, end), ...]

    def add_agent(self, agent):
        if agent.allocated:
            self._used_bank_list.append((agent.start_addr, agent.end_addr, agent.name))
        else:
            self._request_agent_list.append(agent)

    def fit(self):
        self._used_bank_list.sort(key=lambda bank: bank[0])

        p_verbose(">>> Used Blocks")
        for i, bank in enumerate(self._used_bank_list):
            start_addr, end_addr = bank[0], bank[1]
            p_verbose('[0x%08X - 0x%08X], size:%.2fM, %s' % (start_addr, end_addr, (end_addr - start_addr)/1024.0/1024.0, bank[2]))
            if i > 0:
                if start_addr < self._used_bank_list[i - 1][1]:
                    assert False, "Error allocated memory"

        next_start = 0
        for i, bank in enumerate(self._used_bank_list):
            start_addr, end_addr = bank[0], bank[1]
            if start_addr > next_start:
                self._free_block_list.append([next_start, start_addr, start_addr - next_start])
            next_start = end_addr

        if next_start < GV.DDR_size_byte:
            self._free_block_list.append([next_start, GV.DDR_size_byte, GV.DDR_size_byte - next_start])

        p_verbose(">>> Free Blocks")
        for free_block in self._free_block_list:
            p_verbose("[0x%08X, 0x%08X], size:%.2fM" % (free_block[0], free_block[1], free_block[2] / 1024.0 / 1024.0))

        for agent in self._request_agent_list:
            p_verbose("Allocate %.2fM for agent(tagged:%s) <%s>" % (agent.size_m, agent.ddr_tag.name, agent.name))
            self.allocate_memory(agent)

    @staticmethod
    def _find_best_index(free_block_list, allocate_size):
        best_index = -1
        for i, free_block in enumerate(free_block_list):
            start_addr = free_block[0]
            size = free_block[2]
            if size >= allocate_size:
                if best_index == -1 or size < free_block_list[best_index][2]:
                    best_index = i
        return best_index

    def allocate_memory(self, agent):
        best_index = self._find_best_index(self._free_block_list, agent.size)
        if best_index == -1:
            p_error("Allocate %.2fM failed for agent <%s>" % (agent.size_m, agent.name))
            for i, free_block in enumerate(self._free_block_list):
                p_error('free_block[%d] [0x%08X - 0x%08X] %.2fM' % (i, free_block[0], free_block[1], free_block[2] / 1024.0 / 1024.0))
            return False
        else:
            agent.set_memory_range(self._free_block_list[best_index][0], None, self._ddr_tag)
            p_debug("Allocate %.2fM success for agent <%s> at 0x%08X" % (agent.size_m, agent.name, agent.start_addr))
            self._free_block_list[best_index][0] += agent.size
            self._free_block_list[best_index][2] -= agent.size
            return True

    @property
    def unallocated_agents(self):
        return self._request_agent_list
