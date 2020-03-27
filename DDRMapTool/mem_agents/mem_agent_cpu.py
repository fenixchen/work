from mem_common import *
from mem_agents.mem_agent import MemAgent
from mem_global_var import *


class MemAgent_CPU(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self):
        super().__init__('CPU', 'CPU', DDROp.W)

    def calc_memory(self):
        return 64, 150
