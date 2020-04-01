from mem_common import *
from mem_agents.mem_agent import MemAgent
from mem_global_var import *


class MemAgent_LOCAL_DIMMING_W(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self):
        super().__init__('LOCAL_DIMMING_W', 'LOCAL_DIMMING_W', DDROp.W)

    def calc_memory(self):
        Local_Dimming_W_frame_rate = GV.output_refresh_rate
        Local_Dimming_W_bits = 32
        Local_Dimming_W_H_res = 560
        Local_Dimming_W_VDE_res = 120
        Local_Dimming_W_CPR_ratio = 1
        Local_Dimming_W_Bandwidth = Local_Dimming_W_frame_rate*Local_Dimming_W_bits*Local_Dimming_W_H_res * \
            Local_Dimming_W_VDE_res/Local_Dimming_W_CPR_ratio/8/1000/1000*2*(IF(GV.Local_Dimming_en == 1, 1, 0))
        Local_Dimming_W_DDR_size = ROUNDUP(Local_Dimming_W_H_res*Local_Dimming_W_bits/8/1024, 0)*1024*Local_Dimming_W_VDE_res/Local_Dimming_W_CPR_ratio/1024/1024*4*(IF(GV.Local_Dimming_en == 1, 1, 0))
        return Local_Dimming_W_DDR_size, Local_Dimming_W_Bandwidth


class MemAgent_LOCAL_DIMMING_R(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self):
        super().__init__('LOCAL_DIMMING_R', 'LOCAL_DIMMING_R', DDROp.R, 'LOCAL_DIMMING_W')

    def calc_memory(self):
        Local_Dimming_R_frame_rate = GV.output_refresh_rate
        Local_Dimming_R_bits = 32
        Local_Dimming_R_H_res = 560
        Local_Dimming_R_VDE_res = 120
        Local_Dimming_R_CPR_ratio = 1
        Local_Dimming_R_Bandwidth = Local_Dimming_R_frame_rate*Local_Dimming_R_bits*Local_Dimming_R_H_res * \
            Local_Dimming_R_VDE_res/Local_Dimming_R_CPR_ratio/8/1000/1000*2*(IF(GV.Local_Dimming_en == 1, 1, 0))
        Local_Dimming_R_DDR_size = 0
        return Local_Dimming_R_DDR_size, Local_Dimming_R_Bandwidth
