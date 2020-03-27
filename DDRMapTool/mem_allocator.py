from mem_common import *


class MemAllocator():
    def __init__(self):
        self._used_bank_list = []
        self._request_agents = []

    def best_fit(self, block_size, process_size):
        m = len(block_size)
        n = len(process_size)
        # Stores block id of the block
        # allocated to a process
        allocation = [-1] * n

        # pick each process and find suitable
        # blocks according to its size ad
        # assign to it
        for i in range(n):
            # Find the best fit block for
            # current process
            best_index = -1
            for j in range(m):
                if block_size[j] >= process_size[i]:
                    if best_index == -1:
                        best_index = j
                    elif block_size[best_index] > block_size[j]:
                        best_index = j
            # If we could find a block for
            # current process
            if best_index != -1:

                # allocate block j to p[i] process
                allocation[i] = best_index

                # Reduce available memory in this block.
                block_size[best_index] -= process_size[i]
        print("Process No. Process Size     Block no.")
        for i in range(n):
            print(i + 1, "       ", process_size[i],
                  end="      ")
            if allocation[i] != -1:
                print(allocation[i] + 1)
            else:
                print("Not Allocated")

    def add_agent(self, agent):
        if agent.allocated:
            self._used_bank_list.append((agent.start_addr, agent.end_addr, agent.name))
        else:
            self._request_agents.append(agent)

    def fit(self):
        self._used_bank_list.sort(key=lambda bank: bank[0])

        p_verbose(">>> Used Blocks")
        for i, bank in enumerate(self._used_bank_list):
            start_addr, end_addr = bank[0], bank[1]
            p_verbose('[0x%08X - 0x%08X], size:%.2fM, %s' % (start_addr, end_addr, (end_addr - start_addr)/1024.0/1024.0, bank[2]))
            if i > 0:
                if start_addr < self._used_bank_list[i - 1][1]:
                    assert False, "Error allocated memory"

        free_block_list = []  # [(size, start, end), ...]
        next_start = 0
        for i, bank in enumerate(self._used_bank_list):
            start_addr, end_addr = bank[0], bank[1]
            if start_addr > next_start:
                free_block_list.append([next_start, start_addr, start_addr - next_start])
            next_start = end_addr

        if next_start < DDR_SIZE_BYTE:
            free_block_list.append([next_start, DDR_SIZE_BYTE, DDR_SIZE_BYTE - next_start])

        p_verbose(">>> Free Blocks")
        for free_block in free_block_list:
            p_verbose("[0x%08X, 0x%08X], size:%.2fM" % (free_block[0], free_block[1], free_block[2] / 1024.0 / 1024.0))

        for agent in self._request_agents:
            p_verbose("Allocate %.2fM for agent <%s>" % (agent.size_m, agent.name))
            best_index = self._find_best_index(free_block_list, agent.size)
            if best_index == -1:
                p_error("Allocate %.2fM failed for agent <%s>" % (agent.size_m, agent.name))
                assert False
            else:
                agent.set_memory_range(free_block_list[best_index][0], None)
                p_verbose("Allocate %.2fM success for agent <%s> at 0x%08X" % (agent.size_m, agent.name, agent.start_addr))
                free_block_list[best_index][0] += agent.size
                free_block_list[best_index][2] -= agent.size

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

    @property
    def unallocated_agents(self):
        return self._request_agents
