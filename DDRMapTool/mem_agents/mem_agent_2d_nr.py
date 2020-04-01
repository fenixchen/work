from mem_common import *
from mem_agents.mem_agent import MemAgent
from mem_global_var import *


class MemAgent_2D_NR_DECONTOUR_W(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self):
        super().__init__('2D_NR_DECONTOUR_W', '2D_NR_DECONTOUR_W', DDROp.W)

    def calc_memory(self):
        DCN_W_frame_rate = GV.video_input_refresh_rate
        DCN_W_bits = 96
        DCN_W_H_res = 512
        DCN_W_VDE_res = 256
        DCN_W_CPR_ratio = 1
        DCN_W_Bandwidth = DCN_W_frame_rate*DCN_W_bits*DCN_W_H_res*DCN_W_VDE_res/DCN_W_CPR_ratio/8/1000/1000
        DCN_W_DDR_size = ROUNDUP(DCN_W_H_res*DCN_W_bits/8/1024, 0)*1024*DCN_W_VDE_res/DCN_W_CPR_ratio/1024/1024*2
        return DCN_W_DDR_size, DCN_W_Bandwidth


class MemAgent_2D_NR_DECONTOUR_R(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self):
        super().__init__('2D_NR_DECONTOUR_R', '2D_NR_DECONTOUR_R', DDROp.R, '2D_NR_DECONTOUR_W')

    def calc_memory(self):
        DCN_R_frame_rate = GV.video_input_refresh_rate
        DCN_R_bits = 96
        DCN_R_H_res = 512
        DCN_R_VDE_res = 256
        DCN_R_CPR_ratio = 1
        DCN_R_Bandwidth = DCN_R_frame_rate*DCN_R_bits*DCN_R_H_res*DCN_R_VDE_res/DCN_R_CPR_ratio/8/1000/1000
        DCN_R_DDR_size = 0
        return DCN_R_DDR_size, DCN_R_Bandwidth


class MemAgent_2D_NR_BMNR_W(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self):
        super().__init__('2D_NR_BMNR_W', '2D_NR_BMNR_W', DDROp.W)

    def calc_memory(self):
        BMNR_W_frame_rate = GV.video_input_refresh_rate
        BMNR_W_bits = 16
        BMNR_W_H_res = 1024
        BMNR_W_VDE_res = 512
        BMNR_W_CPR_ratio = 1
        BMNR_W_Bandwidth = BMNR_W_frame_rate*BMNR_W_bits*BMNR_W_H_res*BMNR_W_VDE_res/BMNR_W_CPR_ratio/8/1000/1000*(IF(GV.Detect_common == 1, 0, 1))
        BMNR_W_DDR_size = ROUNDUP(BMNR_W_H_res*BMNR_W_bits/8/1024, 0)*1024*BMNR_W_VDE_res/BMNR_W_CPR_ratio/1024/1024*2*(IF(GV.Detect_common == 1, 0, 1))
        return BMNR_W_DDR_size, BMNR_W_Bandwidth


class MemAgent_2D_NR_BMNR_R(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self):
        super().__init__('2D_NR_BMNR_R', '2D_NR_BMNR_R', DDROp.R, '2D_NR_BMNR_W')

    def calc_memory(self):
        BMNR_R_frame_rate = GV.video_input_refresh_rate
        BMNR_R_bits = 16
        BMNR_R_H_res = 1024
        BMNR_R_VDE_res = 512
        BMNR_R_CPR_ratio = 1
        BMNR_R_Bandwidth = BMNR_R_frame_rate*BMNR_R_bits*BMNR_R_H_res*BMNR_R_VDE_res/BMNR_R_CPR_ratio/8/1000/1000*(IF(GV.Detect_common == 1, 0, 1))
        BMNR_R_DDR_size = 0
        return BMNR_R_DDR_size, BMNR_R_Bandwidth
