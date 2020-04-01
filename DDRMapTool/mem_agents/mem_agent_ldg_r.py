from mem_common import *
from mem_agents.mem_agent import MemAgent
from mem_global_var import *


class MemAgent_LDG_R(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self, name):
        super().__init__(name, name, DDROp.R)

    def calc_memory(self):
        if self._name == 'LDR_R1':
            LDG_1_R_frame_rate = GV.output_refresh_rate
            LDG_1_R_bits = 24
            LDG_1_R_H_res = GV.output_Hactive/4
            LDG_1_R_VDE_res = GV.output_Vactive
            LDG_1_R_CPR_ratio = GV.video_comp_ratio
            LDG_1_R_Bandwidth = LDG_1_R_frame_rate*LDG_1_R_bits*LDG_1_R_H_res*LDG_1_R_VDE_res/LDG_1_R_CPR_ratio/8/1000/1000*(IF(GV.LDG_on == 1, 1, 0))
            LDG_1_R_DDR_size = 0
            return LDG_1_R_DDR_size, LDG_1_R_Bandwidth
        elif self._name == 'LDR_R2':
            LDG_2_R_frame_rate = GV.output_refresh_rate
            LDG_2_R_bits = 24
            LDG_2_R_H_res = GV.output_Hactive/4
            LDG_2_R_VDE_res = GV.output_Vactive
            LDG_2_R_CPR_ratio = GV.video_comp_ratio
            LDG_2_R_Bandwidth = LDG_2_R_frame_rate*LDG_2_R_bits*LDG_2_R_H_res*LDG_2_R_VDE_res/LDG_2_R_CPR_ratio/8/1000/1000*(IF(GV.LDG_on == 1, 1, 0))
            LDG_2_R_DDR_size = 0
            return LDG_2_R_DDR_size, LDG_2_R_Bandwidth
        elif self._name == 'LDR_R3':
            LDG_3_R_frame_rate = GV.output_refresh_rate
            LDG_3_R_bits = 24
            LDG_3_R_H_res = GV.output_Hactive/4
            LDG_3_R_VDE_res = GV.output_Vactive
            LDG_3_R_CPR_ratio = GV.video_comp_ratio
            LDG_3_R_Bandwidth = LDG_3_R_frame_rate*LDG_3_R_bits*LDG_3_R_H_res*LDG_3_R_VDE_res/LDG_3_R_CPR_ratio/8/1000/1000*(IF(GV.LDG_on == 1, 1, 0))
            LDG_3_R_DDR_size = 0
            return LDG_3_R_DDR_size, LDG_3_R_Bandwidth
        elif self._name == 'LDR_R4':
            LDG_4_R_frame_rate = GV.output_refresh_rate
            LDG_4_R_bits = 24
            LDG_4_R_H_res = GV.output_Hactive/4
            LDG_4_R_VDE_res = GV.output_Vactive
            LDG_4_R_CPR_ratio = GV.video_comp_ratio
            LDG_4_R_Bandwidth = LDG_4_R_frame_rate*LDG_4_R_bits*LDG_4_R_H_res*LDG_4_R_VDE_res/LDG_4_R_CPR_ratio/8/1000/1000*(IF(GV.LDG_on == 1, 1, 0))
            LDG_4_R_DDR_size = 0
            return LDG_4_R_DDR_size, LDG_4_R_Bandwidth
        else:
            assert False, "Unknown LDG_R %s" % self._name
