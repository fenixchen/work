from mem_common import *
from mem_agents.mem_agent import MemAgent
from mem_global_var import *


class MemAgent_DNN_IN(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self, name):
        super().__init__(name, name, DDROp.W)

    def calc_memory(self):
        name = self.name
        if name == 'DNN_IN_1':
            DNN_IN_1_W_frame_rate = GV.video_input_refresh_rate
            DNN_IN_1_W_bits = 24
            DNN_IN_1_W_H_res = 512
            DNN_IN_1_W_VDE_res = 256
            DNN_IN_1_W_CPR_ratio = 1
            DNN_IN_1_W_Bandwidth = DNN_IN_1_W_frame_rate*DNN_IN_1_W_bits*DNN_IN_1_W_H_res*DNN_IN_1_W_VDE_res/DNN_IN_1_W_CPR_ratio/8/1000/1000*(IF(GV.DNN_num == 0, 0, 1))/GV.DNN_Addr_Interleave
            DNN_IN_1_W_DDR_size = ROUNDUP(DNN_IN_1_W_H_res*DNN_IN_1_W_bits/8/1024, 0)*1024*DNN_IN_1_W_VDE_res/DNN_IN_1_W_CPR_ratio/1024/1024*(IF(GV.DNN_num == 0, 0, 1))/GV.DNN_Addr_Interleave
            return DNN_IN_1_W_DDR_size, DNN_IN_1_W_Bandwidth
        elif name == 'DNN_IN_2':
            DNN_IN_2_W_frame_rate = GV.video_input_refresh_rate
            DNN_IN_2_W_bits = 24
            DNN_IN_2_W_H_res = 512
            DNN_IN_2_W_VDE_res = 256
            DNN_IN_2_W_CPR_ratio = 1
            DNN_IN_2_W_Bandwidth = DNN_IN_2_W_frame_rate*DNN_IN_2_W_bits*DNN_IN_2_W_H_res*DNN_IN_2_W_VDE_res/DNN_IN_2_W_CPR_ratio/8/1000/1000*(IF(GV.DNN_num == 0, 0, 1))/GV.DNN_Addr_Interleave
            DNN_IN_2_W_DDR_size = ROUNDUP(DNN_IN_2_W_H_res*DNN_IN_2_W_bits/8/1024, 0)*1024*DNN_IN_2_W_VDE_res/DNN_IN_2_W_CPR_ratio / \
                1024/1024*(IF(GV.DNN_num == 0, 0, 1))/GV.DNN_Addr_Interleave*(IF(GV.DNN_Addr_Interleave > 1, 1, 0))
            return DNN_IN_2_W_DDR_size, DNN_IN_2_W_Bandwidth
        elif name == 'DNN_IN_3':
            DNN_IN_3_W_frame_rate = GV.video_input_refresh_rate
            DNN_IN_3_W_bits = 24
            DNN_IN_3_W_H_res = 512
            DNN_IN_3_W_VDE_res = 256
            DNN_IN_3_W_CPR_ratio = 1
            DNN_IN_3_W_Bandwidth = DNN_IN_3_W_frame_rate*DNN_IN_3_W_bits*DNN_IN_3_W_H_res*DNN_IN_3_W_VDE_res/DNN_IN_3_W_CPR_ratio/8/1000/1000*(IF(GV.DNN_num == 0, 0, 1))/GV.DNN_Addr_Interleave
            DNN_IN_3_W_DDR_size = ROUNDUP(DNN_IN_3_W_H_res*DNN_IN_3_W_bits/8/1024, 0)*1024*DNN_IN_3_W_VDE_res/DNN_IN_3_W_CPR_ratio / \
                1024/1024*(IF(GV.DNN_num == 0, 0, 1))/GV.DNN_Addr_Interleave*(IF(GV.DNN_Addr_Interleave > 2, 1, 0))
            return DNN_IN_3_W_DDR_size, DNN_IN_3_W_Bandwidth
        elif name == 'DNN_IN_4':
            DNN_IN_4_W_frame_rate = GV.video_input_refresh_rate
            DNN_IN_4_W_bits = 24
            DNN_IN_4_W_H_res = 512
            DNN_IN_4_W_VDE_res = 256
            DNN_IN_4_W_CPR_ratio = 1
            DNN_IN_4_W_Bandwidth = DNN_IN_4_W_frame_rate*DNN_IN_4_W_bits*DNN_IN_4_W_H_res*DNN_IN_4_W_VDE_res/DNN_IN_4_W_CPR_ratio/8/1000/1000*(IF(GV.DNN_num == 0, 0, 1))/GV.DNN_Addr_Interleave
            DNN_IN_4_W_DDR_size = ROUNDUP(DNN_IN_4_W_H_res*DNN_IN_4_W_bits/8/1024, 0)*1024*DNN_IN_4_W_VDE_res/DNN_IN_4_W_CPR_ratio / \
                1024/1024*(IF(GV.DNN_num == 0, 0, 1))/GV.DNN_Addr_Interleave*(IF(GV.DNN_Addr_Interleave > 3, 1, 0))
            return DNN_IN_4_W_DDR_size, DNN_IN_4_W_Bandwidth
        else:
            assert False, "Unknown DNN IN"
