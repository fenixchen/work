from mem_common import DDR_COUNT, pdebug, perror


class MemManager:
    def __init__(self):
        self._agent_list = []

    def add_agent(self, agent):
        self._agent_list.append(agent)

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
            print('>>> DDR%s' % (i + 1))
            start_addr = 0
            bandwidth = 0
            for agent in self._agent_list:
                if agent.ddr_tag.value != i:
                    continue
                regs = agent.get_regs(reg_dict)
                
                assert agent.start_addr is not None
                
                reg_dict['%s_start_addr' % agent.name] = agent.start_addr
                all_regs += regs

                start_addr += agent.size_k
                bandwidth += agent.bandwidth_m
                pdebug("+ %8s(%.2fM) => %.2fM" % (agent.name, agent.size_m, start_addr))
                for reg in regs:
                    print(reg)
            pdebug('Total, Size:%.2fM, Bandwidth:%.2fM\n' % (start_addr, bandwidth))
            if start_addr > 256 * 1024:
                perror('DDR %d overflow' % i)
        return all_regs
