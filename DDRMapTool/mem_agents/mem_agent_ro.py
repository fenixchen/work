from mem_common import DDROp

from mem_agents.mem_agent import MemAgent


class MemAgent_RO(MemAgent):
    """
    Read Agent, no size
    """
    # pylint: disable=invalid-name
    def __init__(self, name, bandwidth, write_agent_name):
        super().__init__(name, 0, bandwidth, DDROp.R)
        self._write_agent_name = write_agent_name

    @property
    def write_agent_name(self):
        return self._write_agent_name

    def get_regs(self, reg_dict):
        write_agent_start_addr_name = '%s_start_addr' % self._write_agent_name
        assert write_agent_start_addr_name in reg_dict
        self.start_addr = reg_dict[write_agent_start_addr_name]
        return  []
