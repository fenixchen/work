from mem_common import *
from mem_agents.mem_agent import MemAgent
from mem_global_var import *


class MemAgent_SRP_OUT_W(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self, name):
        super().__init__(name, name, DDROp.W)

    def calc_memory(self):
        if self._name == 'SRP_OUT_W_1':
            SRP_OUT_1_W_frame_rate = video_input_refresh_rate
            SRP_OUT_1_W_bits = 24
            SRP_OUT_1_W_H_res = output_Hactive/4
            SRP_OUT_1_W_VDE_res = output_Vactive
            SRP_OUT_1_W_CPR_ratio = video_comp_ratio
            SRP_OUT_1_W_Bandwidth = SRP_OUT_1_W_frame_rate*SRP_OUT_1_W_bits*SRP_OUT_1_W_H_res*SRP_OUT_1_W_VDE_res/SRP_OUT_1_W_CPR_ratio/8/1000/1000*(IF(LDG_on == 1, 1, 0))
            SRP_OUT_1_W_DDR_size = ROUNDUP(SRP_OUT_1_W_H_res*SRP_OUT_1_W_bits/8/1024, 0)*1024*SRP_OUT_1_W_VDE_res/SRP_OUT_1_W_CPR_ratio/1024/1024*(IF(LDG_on == 1, 1, 0))
            return SRP_OUT_1_W_DDR_size, SRP_OUT_1_W_Bandwidth
        elif self._name == 'SRP_OUT_W_2':
            SRP_OUT_2_W_frame_rate = video_input_refresh_rate
            SRP_OUT_2_W_bits = 24
            SRP_OUT_2_W_H_res = output_Hactive/4
            SRP_OUT_2_W_VDE_res = output_Vactive
            SRP_OUT_2_W_CPR_ratio = video_comp_ratio
            SRP_OUT_2_W_Bandwidth = SRP_OUT_2_W_frame_rate*SRP_OUT_2_W_bits*SRP_OUT_2_W_H_res*SRP_OUT_2_W_VDE_res/SRP_OUT_2_W_CPR_ratio/8/1000/1000*(IF(LDG_on == 1, 1, 0))
            SRP_OUT_2_W_DDR_size = ROUNDUP(SRP_OUT_2_W_H_res*SRP_OUT_2_W_bits/8/1024, 0)*1024*SRP_OUT_2_W_VDE_res/SRP_OUT_2_W_CPR_ratio/1024/1024*(IF(LDG_on == 1, 1, 0))
            return SRP_OUT_2_W_DDR_size, SRP_OUT_2_W_Bandwidth
        elif self._name == 'SRP_OUT_W_3':
            SRP_OUT_3_W_frame_rate = video_input_refresh_rate
            SRP_OUT_3_W_bits = 24
            SRP_OUT_3_W_H_res = output_Hactive/4
            SRP_OUT_3_W_VDE_res = output_Vactive
            SRP_OUT_3_W_CPR_ratio = video_comp_ratio
            SRP_OUT_3_W_Bandwidth = SRP_OUT_3_W_frame_rate*SRP_OUT_3_W_bits*SRP_OUT_3_W_H_res*SRP_OUT_3_W_VDE_res/SRP_OUT_3_W_CPR_ratio/8/1000/1000*(IF(LDG_on == 1, 1, 0))
            SRP_OUT_3_W_DDR_size = ROUNDUP(SRP_OUT_3_W_H_res*SRP_OUT_3_W_bits/8/1024, 0)*1024*SRP_OUT_3_W_VDE_res/SRP_OUT_3_W_CPR_ratio/1024/1024*(IF(LDG_on == 1, 1, 0))
            return SRP_OUT_3_W_DDR_size, SRP_OUT_3_W_Bandwidth
        elif self._name == 'SRP_OUT_W_4':
            SRP_OUT_4_W_frame_rate = video_input_refresh_rate
            SRP_OUT_4_W_bits = 24
            SRP_OUT_4_W_H_res = output_Hactive/4
            SRP_OUT_4_W_VDE_res = output_Vactive
            SRP_OUT_4_W_CPR_ratio = video_comp_ratio
            SRP_OUT_4_W_Bandwidth = SRP_OUT_4_W_frame_rate*SRP_OUT_4_W_bits*SRP_OUT_4_W_H_res*SRP_OUT_4_W_VDE_res/SRP_OUT_4_W_CPR_ratio/8/1000/1000*(IF(LDG_on == 1, 1, 0))
            SRP_OUT_4_W_DDR_size = ROUNDUP(SRP_OUT_4_W_H_res*SRP_OUT_4_W_bits/8/1024, 0)*1024*SRP_OUT_4_W_VDE_res/SRP_OUT_4_W_CPR_ratio/1024/1024*(IF(LDG_on == 1, 1, 0))
            return SRP_OUT_4_W_DDR_size, SRP_OUT_4_W_Bandwidth
        else:
            assert False, "Unknown SRP_OUT_W"
