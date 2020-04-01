class MemBlock:
    def __init__(self, block_name):
        self._block_name = block_name
        self._agent_list = []

    @property
    def name(self):
        return self._block_name

    @property
    def agent_list(self):
        return self._agent_list

    def add_agent(self, agent):
        assert agent not in self._agent_list, "duplicate agent:%s" % agent.name
        agent.block = self
        self._agent_list.append(agent)
