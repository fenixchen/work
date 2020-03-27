from mem_common import *
from mem_agents.mem_agent import MemAgent
from mem_global_var import *


class MemAgent_MV_W_3DRS(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self):
        super().__init__('MV_W_3DRS', 'MV_W_3DRS', DDROp.W)

    def calc_memory(self):
        MV_W_3DRS_frame_rate = video_input_refresh_rate
        MV_W_3DRS_bits = 12
        MV_W_3DRS_H_res = 480
        MV_W_3DRS_V_res = video_input_Vtotal
        MV_W_3DRS_VDE_res = 4320
        MV_W_3DRS_CPR_ratio = 1
        MV_W_3DRS_Bandwidth = MV_W_3DRS_frame_rate*MV_W_3DRS_bits*MV_W_3DRS_H_res*MV_W_3DRS_VDE_res/MV_W_3DRS_CPR_ratio/8/1000/1000*(IF(IIR_en == 1, 1, 0))
        MV_W_3DRS_DDR_size = ROUNDUP(MV_W_3DRS_H_res*MV_W_3DRS_bits/8/1024, 0)*1024*MV_W_3DRS_VDE_res/MV_W_3DRS_CPR_ratio/1024/1024*(IF(IIR_en == 1, 2, 0))
        return MV_W_3DRS_DDR_size, MV_W_3DRS_Bandwidth


class MemAgent_MV_R_3DRS(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self):
        super().__init__('MV_R_3DRS', 'MV_R_3DRS', DDROp.R, 'MV_W_3DRS')

    def calc_memory(self):
        MV_R_3DRS_frame_rate = video_input_refresh_rate
        MV_R_3DRS_bits = 12
        MV_R_3DRS_H_res = 480
        MV_R_3DRS_V_res = video_input_Vtotal
        MV_R_3DRS_VDE_res = 4320
        MV_R_3DRS_CPR_ratio = 1
        MV_R_3DRS_Bandwidth = MV_R_3DRS_frame_rate*MV_R_3DRS_bits*MV_R_3DRS_H_res*MV_R_3DRS_VDE_res/MV_R_3DRS_CPR_ratio/8/1000/1000*(IF(IIR_en == 1, 1, 0))
        MV_R_3DRS_DDR_size = 0
        return MV_R_3DRS_DDR_size, MV_R_3DRS_Bandwidth


class MemAgent_CNT_W_3DRS(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self):
        super().__init__('CNT_W_3DRS', 'CNT_W_3DRS', DDROp.W)

    def calc_memory(self):
        CNT_W_3DRS_frame_rate = video_input_refresh_rate
        CNT_W_3DRS_bits = 4
        CNT_W_3DRS_H_res = 1920
        CNT_W_3DRS_V_res = video_input_Vtotal
        CNT_W_3DRS_VDE_res = 1080
        CNT_W_3DRS_CPR_ratio = 1
        CNT_W_3DRS_Bandwidth = CNT_W_3DRS_frame_rate*CNT_W_3DRS_bits*CNT_W_3DRS_H_res*CNT_W_3DRS_VDE_res/CNT_W_3DRS_CPR_ratio/8/1000/1000*(IF(IIR_en == 1, 1, 0))
        CNT_W_3DRS_DDR_size = ROUNDUP(CNT_W_3DRS_H_res*CNT_W_3DRS_bits/8/1024, 0)*1024*CNT_W_3DRS_VDE_res/CNT_W_3DRS_CPR_ratio/1024/1024*(IF(IIR_en == 1, 2, 0))
        return CNT_W_3DRS_DDR_size, CNT_W_3DRS_Bandwidth


class MemAgent_CNT_R_3DRS(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self):
        super().__init__('CNT_R_3DRS', 'CNT_R_3DRS', DDROp.R, 'CNT_W_3DRS')

    def calc_memory(self):
        CNT_R_3DRS_frame_rate = video_input_refresh_rate
        CNT_R_3DRS_bits = 4
        CNT_R_3DRS_H_res = 1920
        CNT_R_3DRS_V_res = video_input_Vtotal
        CNT_R_3DRS_VDE_res = 1080
        CNT_R_3DRS_CPR_ratio = 1
        CNT_R_3DRS_Bandwidth = CNT_R_3DRS_frame_rate*CNT_R_3DRS_bits*CNT_R_3DRS_H_res*CNT_R_3DRS_VDE_res/CNT_R_3DRS_CPR_ratio/8/1000/1000*(IF(IIR_en == 1, 1, 0))
        CNT_R_3DRS_DDR_size = 0
        return CNT_R_3DRS_DDR_size, CNT_R_3DRS_Bandwidth
