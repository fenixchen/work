import enum
from mem_common import *
from mem_agents.mem_agent import MemAgent
from mem_global_var import *


class GFXType(enum.Enum):
    GFX_IN_1 = 0
    GFX_IN_2 = 1
    GFX_ALPHA = 2
    GFX_R_1 = 3
    GFX_R_2 = 4
    GFX_ALPHA_R = 5


class MemAgent_GFX(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self, gfx_type):
        self._gfx_type = gfx_type
        gfx_op = [DDROp.W,
                  DDROp.W,
                  DDROp.W,
                  DDROp.R,
                  DDROp.R,
                  DDROp.R
                  ]
        write_agent_name_list = [
            None,
            None,
            None,
            "GFX_IN_1",  # for GFX_R_1
            "GFX_IN_2",  # for GFX_R_2
            "GFX_ALPHA",  # for GFX_ALPHA_R
        ]
        super().__init__(gfx_type.name, gfx_type.name, gfx_op[gfx_type.value], write_agent_name_list[gfx_type.value])

    def calc_memory(self):
        gfx_type = self._gfx_type
        if gfx_type == GFXType.GFX_IN_1:
            GFX_IN1_W_frame_rate = GV.OSD_input_refresh_rate
            GFX_IN1_W_bits = GV.OSD_data_width
            GFX_IN1_W_H_res = GV.OSD_input_Hactive/2
            GFX_IN1_W_V_res = GV.OSD_input_Vtotal
            GFX_IN1_W_VDE_res = GV.OSD_input_Vactive
            GFX_IN1_W_CPR_ratio = GV.OSD_data_comp_ratio
            GFX_IN1_W_Bandwidth = GFX_IN1_W_frame_rate*GFX_IN1_W_bits*GFX_IN1_W_H_res*GFX_IN1_W_V_res/GFX_IN1_W_CPR_ratio/8/1000/1000*GV.OSD_en
            GFX_IN1_W_DDR_size = ROUNDUP(GFX_IN1_W_H_res / 1024.0, 0)*1024*GFX_IN1_W_bits*GFX_IN1_W_VDE_res/8/1024/1024*GV.OSD_en*GV.OSD_Framedelay
            return GFX_IN1_W_DDR_size, GFX_IN1_W_Bandwidth
        elif gfx_type == GFXType.GFX_IN_2:
            GFX_IN2_W_frame_rate = GV.OSD_input_refresh_rate
            GFX_IN2_W_bits = GV.OSD_data_width
            GFX_IN2_W_H_res = GV.OSD_input_Hactive/2
            GFX_IN2_W_V_res = GV.OSD_input_Vtotal
            GFX_IN2_W_VDE_res = GV.OSD_input_Vactive
            GFX_IN2_W_CPR_ratio = GV.OSD_data_comp_ratio
            GFX_IN2_W_Bandwidth = GFX_IN2_W_frame_rate*GFX_IN2_W_bits*GFX_IN2_W_H_res*GFX_IN2_W_V_res/GFX_IN2_W_CPR_ratio/8/1000/1000*GV.OSD_en
            GFX_IN2_W_DDR_size = ROUNDUP(GFX_IN2_W_H_res / 1024.0, 0)*1024 * GFX_IN2_W_bits*GFX_IN2_W_VDE_res/8/1024/1024*GV.OSD_en*GV.OSD_Framedelay
            return GFX_IN2_W_DDR_size, GFX_IN2_W_Bandwidth
        elif gfx_type == GFXType.GFX_ALPHA:
            GFX_alpha_W_frame_rate = GV.OSD_input_refresh_rate
            GFX_alpha_W_bits = GV.OSD_alpha_width
            GFX_alpha_W_H_res = GV.OSD_input_Hactive
            GFX_alpha_W_V_res = GV.OSD_input_Vtotal
            GFX_alpha_W_VDE_res = GV.OSD_input_Vactive
            GFX_alpha_W_CPR_ratio = GV.OSD_alpha_comp_ratio
            GFX_alpha_W_Bandwidth = GFX_alpha_W_frame_rate*GFX_alpha_W_bits*GFX_alpha_W_H_res*GFX_alpha_W_V_res/GFX_alpha_W_CPR_ratio/8/1000/1000*GV.OSD_en
            GFX_alpha_W_DDR_size = ROUNDUP(GFX_alpha_W_H_res / 1024.0, 0)*1024 * GFX_alpha_W_bits*GFX_alpha_W_VDE_res/GFX_alpha_W_CPR_ratio/8/1024/1024*GV.OSD_en*GV.OSD_Framedelay
            return GFX_alpha_W_DDR_size, GFX_alpha_W_Bandwidth
        elif gfx_type == GFXType.GFX_R_1:
            GFX_1_R_frame_rate = GV.OSD_output_refresh_rate
            GFX_1_R_bits = GV.OSD_data_width
            GFX_1_R_H_res = GV.OSD_input_Hactive/2
            GFX_1_R_V_res = GV.OSD_input_Vtotal
            GFX_1_R_VDE_res = GV.OSD_input_Vactive
            GFX_1_R_CPR_ratio = GV.OSD_data_comp_ratio
            GFX_1_R_Bandwidth = GFX_1_R_frame_rate*GFX_1_R_bits*GFX_1_R_H_res*GFX_1_R_V_res/GFX_1_R_CPR_ratio/8/1000/1000*GV.OSD_en
            GFX_1_R_DDR_size = 0
            return GFX_1_R_DDR_size, GFX_1_R_Bandwidth
        elif gfx_type == GFXType.GFX_R_2:
            GFX_2_R_frame_rate = GV.OSD_output_refresh_rate
            GFX_2_R_bits = GV.OSD_data_width
            GFX_2_R_H_res = GV.OSD_input_Hactive/2
            GFX_2_R_V_res = GV.OSD_input_Vtotal
            GFX_2_R_VDE_res = GV.OSD_input_Vactive
            GFX_2_R_CPR_ratio = GV.OSD_data_comp_ratio
            GFX_2_R_Bandwidth = GFX_2_R_frame_rate*GFX_2_R_bits*GFX_2_R_H_res*GFX_2_R_V_res/GFX_2_R_CPR_ratio/8/1000/1000*GV.OSD_en
            GFX_2_R_DDR_size = 0
            return GFX_2_R_DDR_size, GFX_2_R_Bandwidth
        elif gfx_type == GFXType.GFX_ALPHA_R:
            GFX_alpha_R_frame_rate = GV.OSD_output_refresh_rate
            GFX_alpha_R_bits = GV.OSD_alpha_width
            GFX_alpha_R_H_res = GV.OSD_input_Hactive
            GFX_alpha_R_V_res = GV.OSD_input_Vtotal
            GFX_alpha_R_VDE_res = GV.OSD_input_Vactive
            GFX_alpha_R_CPR_ratio = GV.OSD_alpha_comp_ratio
            GFX_alpha_R_Bandwidth = GFX_alpha_R_frame_rate*GFX_alpha_R_bits*GFX_alpha_R_H_res*GFX_alpha_R_V_res/GFX_alpha_R_CPR_ratio/8/1000/1000*GV.OSD_en
            GFX_alpha_R_DDR_size = 0
            return GFX_alpha_R_DDR_size, GFX_alpha_R_Bandwidth
        else:
            assert False, "Unknown type"
