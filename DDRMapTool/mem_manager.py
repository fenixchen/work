from mem_common import DDR_COUNT, p_debug, p_error, p_verbose
from mem_block import MemBlock


class MemManager:
    def __init__(self):
        self._agent_list = []
        self._block_list = []

    def add_block(self, block_name):
        block = MemBlock(block_name)
        return block

    def add_agent(self, agent, block):
        self._agent_list.append(agent)
        block.add_agent(agent)
        p_debug('%s, %-20s, %-16s, bandwidth:%8.2fM, size:%8.2fM, IP:%s' % (
            agent.op_str, agent.module_name, agent.name, agent.bandwidth_m, agent.size_m, agent.block_name))

    def plot(self):
        pass

    @property
    def agent_list(self):
        return self._agent_list

    def get_agent(self, name):
        for agent in self._agent_list:
            if agent.name == name:
                return agent
        return None

    def generate_registers(self):
        all_regs = []
        for i in range(DDR_COUNT):
            reg_dict = {}
            p_verbose('>>> Allicate DDR%s' % (i + 1))
            size_k = 0
            bandwidth_m = 0
            for agent in self._agent_list:
                if agent.ddr_tag.value != i:
                    continue
                regs = agent.get_regs(reg_dict)

                assert agent.start_addr is not None, "start_addr of <%s> is None" % agent.name
                assert agent.end_addr is not None, "end_addr of <%s> is None" % agent.name

                reg_dict['%s_start_addr' % agent.name] = agent.start_addr
                all_regs += regs

                size_k += agent.size_k
                bandwidth_m += agent.bandwidth_m
                for reg in regs:
                    p_verbose(reg)
            p_verbose('Total, Size:%.2fM, Bandwidth:%.2fM\n' % (size_k, bandwidth_m))
            if size_k > 256 * 1024:
                p_error('DDR %d overflow' % i)
        return all_regs
