from mem_common import *
from mem_agents.mem_agent import MemAgent
from mem_global_var import *


class MemAgent_PLDD_W(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self):
        super().__init__('PLDD_W', 'PLDD_W', DDROp.W)

    def calc_memory(self):
        PLDD_W_frame_rate = video_input_refresh_rate
        PLDD_W_bits = 8
        PLDD_W_H_res = 960
        PLDD_W_VDE_res = 540
        PLDD_W_CPR_ratio = 1
        PLDD_W_Bandwidth = PLDD_W_frame_rate*PLDD_W_bits*PLDD_W_H_res*PLDD_W_VDE_res/PLDD_W_CPR_ratio/8/1000/1000*(IF(Cadence_en == 1, 1, 0))
        PLDD_W_DDR_size = ROUNDUP(PLDD_W_H_res*PLDD_W_bits/8/1024, 0)*1024*PLDD_W_VDE_res/PLDD_W_CPR_ratio/1024/1024*2*(IF(Cadence_en == 1, 1, 0))
        return PLDD_W_DDR_size, PLDD_W_Bandwidth

class MemAgent_PLDD_R(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self):
        super().__init__('PLDD_R', 'PLDD_R', DDROp.R)

    def calc_memory(self):
        PLDD_R_frame_rate = video_input_refresh_rate
        PLDD_R_bits = 8
        PLDD_R_H_res = 960
        PLDD_R_VDE_res = 540
        PLDD_R_CPR_ratio = 1
        PLDD_R_Bandwidth = PLDD_R_frame_rate * PLDD_R_bits * PLDD_R_H_res * PLDD_R_VDE_res / PLDD_R_CPR_ratio/8/1000/1000*(IF(Cadence_en == 1, 1, 0))
        PLDD_R_DDR_size = 0
        return PLDD_R_DDR_size, PLDD_R_Bandwidth
