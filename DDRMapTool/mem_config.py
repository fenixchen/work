from mem_manager import MemManager
from mem_common import DDR_COUNT, DDROp
import mem_agents

class MemConfig:
    def __init__(self, name):
        self._name = name
        self._mm = MemManager()

    @property
    def name(self):
        return self._name

    def place_memory(self):
        return NotImplementedError

    def generate_registers(self):
        self.place_memory()
        for agent in self._mm.agent_list:
            if agent.ddr_op == DDROp.R and agent.bandwidth_m != 0:
                assert isinstance(agent, mem_agents.MemAgent_RO)
                write_agent = self._mm.get_agent(agent.write_agent_name)
                assert write_agent is not None
                agent.start_addr = write_agent.start_addr
                agent.ddr_tag = write_agent.ddr_tag
        return self._mm.generate_registers()

    @property
    def agent_list(self):
        return self._mm.agent_list

    def get_ddr_mapping(self):
        """
        return list[[agent0_on_ddr0, agent1_on_ddr0], [agent0_on_ddr1], [], []]
        """
        mapping = [None] * 4
        for i in range(DDR_COUNT):
            agents = []
            for agent in self.agent_list:
                if agent.ddr_tag.value == i:
                    agents.append(agent)
            agents.sort(key=lambda agent: agent.start_addr)
            mapping[i] = agents
        return mapping
