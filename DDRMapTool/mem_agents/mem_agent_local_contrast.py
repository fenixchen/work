from mem_common import *
from mem_agents.mem_agent import MemAgent
from mem_global_var import *


class MemAgent_LOCAL_CONTRAST_1_W(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self):
        super().__init__('LOCAL_CONTRAST_1_W', 'LOCAL_CONTRAST_1_W', DDROp.W)

    def calc_memory(self):
        Local_Contrast_1_W_frame_rate = GV.video_input_refresh_rate
        Local_Contrast_1_W_bits = 12
        Local_Contrast_1_W_H_res = 960
        Local_Contrast_1_W_VDE_res = 540
        Local_Contrast_1_W_CPR_ratio = 1
        Local_Contrast_1_W_Bandwidth = Local_Contrast_1_W_frame_rate*Local_Contrast_1_W_bits*Local_Contrast_1_W_H_res*Local_Contrast_1_W_VDE_res/Local_Contrast_1_W_CPR_ratio/8/1000/1000
        Local_Contrast_1_W_DDR_size = ROUNDUP(Local_Contrast_1_W_H_res*Local_Contrast_1_W_bits/8/1024, 0)*1024*Local_Contrast_1_W_VDE_res/Local_Contrast_1_W_CPR_ratio/1024/1024*2
        return Local_Contrast_1_W_DDR_size, Local_Contrast_1_W_Bandwidth


class MemAgent_LOCAL_CONTRAST_1_R(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self):
        super().__init__('LOCAL_CONTRAST_1_R', 'LOCAL_CONTRAST_1_R', DDROp.W)

    def calc_memory(self):
        Local_Contrast_1_R_frame_rate = GV.video_input_refresh_rate
        Local_Contrast_1_R_bits = 12
        Local_Contrast_1_R_H_res = 960
        Local_Contrast_1_R_VDE_res = 540
        Local_Contrast_1_R_CPR_ratio = 1
        Local_Contrast_1_R_Bandwidth = Local_Contrast_1_R_frame_rate*Local_Contrast_1_R_bits*Local_Contrast_1_R_H_res*Local_Contrast_1_R_VDE_res/Local_Contrast_1_R_CPR_ratio/8/1000/1000
        Local_Contrast_1_R_DDR_size = 0
        return Local_Contrast_1_R_DDR_size, Local_Contrast_1_R_Bandwidth


class MemAgent_LOCAL_CONTRAST_2_W(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self):
        super().__init__('LOCAL_CONTRAST_2_W', 'LOCAL_CONTRAST_2_W', DDROp.W)

    def calc_memory(self):
        Local_Contrast_2_W_frame_rate = GV.video_input_refresh_rate
        Local_Contrast_2_W_bits = 22
        Local_Contrast_2_W_H_res = 120
        Local_Contrast_2_W_VDE_res = 67
        Local_Contrast_2_W_CPR_ratio = 1
        Local_Contrast_2_W_Bandwidth = Local_Contrast_2_W_frame_rate*Local_Contrast_2_W_bits*Local_Contrast_2_W_H_res*Local_Contrast_2_W_VDE_res/Local_Contrast_2_W_CPR_ratio/8/1000/1000
        Local_Contrast_2_W_DDR_size = ROUNDUP(Local_Contrast_2_W_H_res*Local_Contrast_2_W_bits/8/1024, 0)*1024*Local_Contrast_2_W_VDE_res/Local_Contrast_2_W_CPR_ratio/1024/1024*2
        return Local_Contrast_2_W_DDR_size, Local_Contrast_2_W_Bandwidth


class MemAgent_LOCAL_CONTRAST_2_R(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self):
        super().__init__('LOCAL_CONTRAST_2_R', 'LOCAL_CONTRAST_2_R', DDROp.W)

    def calc_memory(self):
        Local_Contrast_2_R_frame_rate = GV.video_input_refresh_rate
        Local_Contrast_2_R_bits = 22
        Local_Contrast_2_R_H_res = 120
        Local_Contrast_2_R_VDE_res = 67
        Local_Contrast_2_R_CPR_ratio = 1
        Local_Contrast_2_R_Bandwidth = Local_Contrast_2_R_frame_rate*Local_Contrast_2_R_bits*Local_Contrast_2_R_H_res*Local_Contrast_2_R_VDE_res/Local_Contrast_2_R_CPR_ratio/8/1000/1000
        Local_Contrast_2_R_DDR_size = 0
        return Local_Contrast_2_R_DDR_size, Local_Contrast_2_R_Bandwidth
