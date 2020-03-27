from mem_common import *
from mem_agents.mem_agent import MemAgent
from mem_global_var import *


class MemAgent_AISR_R(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self):
        super().__init__('AISR_R', 'AISR_R', DDROp.R)

    def calc_memory(self):
        return 0, 0


class MemAgent_AISR_W_1(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self):
        super().__init__('AISR_W_1', 'AISR_W_1', DDROp.R)

    def calc_memory(self):
        return 0, 0


class MemAgent_AISR_W_2(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self):
        super().__init__('AISR_W_2', 'AISR_W_2', DDROp.R)

    def calc_memory(self):
        return 0, 0


class MemAgent_AISR_MAP(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self):
        super().__init__('AISR_MAP', 'AISR_MAP', DDROp.R, 'DNN_IN_1')

    def calc_memory(self):
        AISR_MAP_frame_rate = video_input_refresh_rate
        AISR_MAP_bits = 8
        AISR_MAP_H_res = 240
        AISR_MAP_VDE_res = 135
        AISR_MAP_CPR_ratio = 1
        AISR_MAP_Bandwidth = AISR_MAP_frame_rate*AISR_MAP_bits*AISR_MAP_H_res*AISR_MAP_VDE_res/AISR_MAP_CPR_ratio/8/1000/1000
        AISR_MAP_DDR_size = ROUNDUP(AISR_MAP_H_res*AISR_MAP_bits/8/1024, 0)*1024*AISR_MAP_VDE_res/AISR_MAP_CPR_ratio/1024/1024
        return AISR_MAP_DDR_size, AISR_MAP_Bandwidth
