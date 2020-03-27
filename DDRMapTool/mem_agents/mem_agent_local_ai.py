from mem_common import *
from mem_agents.mem_agent import MemAgent
from mem_global_var import *


class MemAgent_LOCAL_AI_W(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self):
        super().__init__('LOCAL_AI_W', 'LOCAL_AI_W', DDROp.W)

    def calc_memory(self):
        Local_AI_W_frame_rate = video_input_refresh_rate
        Local_AI_W_bits = 6
        Local_AI_W_H_res = 960
        Local_AI_W_VDE_res = 540
        Local_AI_W_CPR_ratio = 1
        Local_AI_W_Bandwidth = Local_AI_W_frame_rate*Local_AI_W_bits*Local_AI_W_H_res*Local_AI_W_VDE_res/Local_AI_W_CPR_ratio/8/1000/1000
        Local_AI_W_DDR_size = ROUNDUP(Local_AI_W_H_res*Local_AI_W_bits/8/1024, 0)*1024*Local_AI_W_VDE_res/Local_AI_W_CPR_ratio/1024/1024*2
        return Local_AI_W_DDR_size, Local_AI_W_Bandwidth


class MemAgent_LOCAL_AI_R(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self):
        super().__init__('LOCAL_AI_R', 'LOCAL_AI_R', DDROp.R, 'LOCAL_AI_W')

    def calc_memory(self):
        Local_AI_R_frame_rate = video_input_refresh_rate
        Local_AI_R_bits = 6
        Local_AI_R_H_res = 960
        Local_AI_R_VDE_res = 540
        Local_AI_R_CPR_ratio = 1
        Local_AI_R_Bandwidth = Local_AI_R_frame_rate*Local_AI_R_bits*Local_AI_R_H_res*Local_AI_R_VDE_res/Local_AI_R_CPR_ratio/8/1000/1000
        Local_AI_R_DDR_size = 0
        return Local_AI_R_DDR_size, Local_AI_R_Bandwidth
