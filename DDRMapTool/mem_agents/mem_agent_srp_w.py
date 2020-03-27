import enum
from mem_common import *
from mem_reg import MemReg
from mem_agents.mem_agent import MemAgent
from mem_global_var import *


class SRPType(enum.Enum):
    SRP_FIR_WRITE_1 = 0
    SRP_FIR_WRITE_2 = 1
    SRP_FIR_WRITE_3 = 2
    SRP_FIR_WRITE_4 = 3
    SRP_NR_OUT_WRITE_1 = 4
    SRP_NR_OUT_WRITE_2 = 5
    SRP_NR_OUT_WRITE_3 = 6
    SRP_NR_OUT_WRITE_4 = 7


class MemAgent_SRP_W(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self, srp_type):
        self._srp_type = srp_type
        super().__init__(srp_type.name, srp_type.name, DDROp.W)

    def calc_memory(self):
        srp_type = self._srp_type
        if srp_type == SRPType.SRP_FIR_WRITE_1:
            SPR_FIR_Write_1_frame_rate = video_input_refresh_rate
            SPR_FIR_Write_1_bits = video_data_width
            SPR_FIR_Write_1_H_res = video_input_Hactive/4
            SPR_FIR_Write_1_V_res = video_input_Vtotal
            SPR_FIR_Write_1_VDE_res = video_input_Vactive
            SPR_FIR_Write_1_CPR_ratio = video_comp_ratio
            SPR_FIR_Write_1_Bandwidth = SPR_FIR_Write_1_frame_rate*SPR_FIR_Write_1_bits*SPR_FIR_Write_1_H_res*SPR_FIR_Write_1_V_res/SPR_FIR_Write_1_CPR_ratio/8/1000/1000*(IF(IIR_en == 1, 0, 1))
            SPR_FIR_Write_1_DDR_size = ROUNDUP(SPR_FIR_Write_1_H_res/1024, 0)*1024*SPR_FIR_Write_1_bits*SPR_FIR_Write_1_VDE_res/SPR_FIR_Write_1_CPR_ratio/8/1024/1024*(IF(IIR_en == 1, 0, FIR_buff_num))
            return SPR_FIR_Write_1_DDR_size, SPR_FIR_Write_1_Bandwidth
        elif srp_type == SRPType.SRP_FIR_WRITE_2:
            SPR_FIR_Write_2_frame_rate = video_input_refresh_rate
            SPR_FIR_Write_2_bits = video_data_width
            SPR_FIR_Write_2_H_res = video_input_Hactive/4
            SPR_FIR_Write_2_V_res = video_input_Vtotal
            SPR_FIR_Write_2_VDE_res = video_input_Vactive
            SPR_FIR_Write_2_CPR_ratio = video_comp_ratio
            SPR_FIR_Write_2_Bandwidth = SPR_FIR_Write_2_frame_rate*SPR_FIR_Write_2_bits*SPR_FIR_Write_2_H_res*SPR_FIR_Write_2_V_res/SPR_FIR_Write_2_CPR_ratio/8/1000/1000*(IF(IIR_en == 1, 0, 1))
            SPR_FIR_Write_2_DDR_size = ROUNDUP(SPR_FIR_Write_2_H_res/1024, 0)*1024*SPR_FIR_Write_2_bits*SPR_FIR_Write_2_VDE_res/SPR_FIR_Write_2_CPR_ratio/8/1024/1024*(IF(IIR_en == 1, 0, FIR_buff_num))
            return SPR_FIR_Write_2_DDR_size, SPR_FIR_Write_2_Bandwidth
        elif srp_type == SRPType.SRP_FIR_WRITE_3:
            SPR_FIR_Write_3_frame_rate = video_input_refresh_rate
            SPR_FIR_Write_3_bits = video_data_width
            SPR_FIR_Write_3_H_res = video_input_Hactive/4
            SPR_FIR_Write_3_V_res = video_input_Vtotal
            SPR_FIR_Write_3_VDE_res = video_input_Vactive
            SPR_FIR_Write_3_CPR_ratio = video_comp_ratio
            SPR_FIR_Write_3_Bandwidth = SPR_FIR_Write_3_frame_rate*SPR_FIR_Write_3_bits*SPR_FIR_Write_3_H_res*SPR_FIR_Write_3_V_res/SPR_FIR_Write_3_CPR_ratio/8/1000/1000*(IF(IIR_en == 1, 0, 1))
            SPR_FIR_Write_3_DDR_size = ROUNDUP(SPR_FIR_Write_3_H_res/1024, 0)*1024*SPR_FIR_Write_3_bits*SPR_FIR_Write_3_VDE_res/SPR_FIR_Write_3_CPR_ratio/8/1024/1024*(IF(IIR_en == 1, 0, FIR_buff_num))
            return SPR_FIR_Write_3_DDR_size, SPR_FIR_Write_3_Bandwidth
        elif srp_type == SRPType.SRP_FIR_WRITE_4:
            SPR_FIR_Write_4_frame_rate = video_input_refresh_rate
            SPR_FIR_Write_4_bits = video_data_width
            SPR_FIR_Write_4_H_res = video_input_Hactive/4
            SPR_FIR_Write_4_V_res = video_input_Vtotal
            SPR_FIR_Write_4_VDE_res = video_input_Vactive
            SPR_FIR_Write_4_CPR_ratio = video_comp_ratio
            SPR_FIR_Write_4_Bandwidth = SPR_FIR_Write_4_frame_rate*SPR_FIR_Write_4_bits*SPR_FIR_Write_4_H_res*SPR_FIR_Write_4_V_res/SPR_FIR_Write_4_CPR_ratio/8/1000/1000*(IF(IIR_en == 1, 0, 1))
            SPR_FIR_Write_4_DDR_size = ROUNDUP(SPR_FIR_Write_4_H_res/1024, 0)*1024*SPR_FIR_Write_4_bits*SPR_FIR_Write_4_VDE_res/SPR_FIR_Write_4_CPR_ratio/8/1024/1024*(IF(IIR_en == 1, 0, FIR_buff_num))
            return SPR_FIR_Write_4_DDR_size, SPR_FIR_Write_4_Bandwidth
        elif srp_type == SRPType.SRP_NR_OUT_WRITE_1:
            SRP_NR_out_Write_1_frame_rate = video_input_refresh_rate
            SRP_NR_out_Write_1_bits = video_data_width
            SRP_NR_out_Write_1_H_res = video_input_Hactive/4
            SRP_NR_out_Write_1_V_res = video_input_Vtotal
            SRP_NR_out_Write_1_VDE_res = video_input_Vactive
            SRP_NR_out_Write_1_CPR_ratio = video_comp_ratio
            SRP_NR_out_Write_1_Bandwidth = SRP_NR_out_Write_1_frame_rate*SRP_NR_out_Write_1_bits*SRP_NR_out_Write_1_H_res * \
                SRP_NR_out_Write_1_V_res/SRP_NR_out_Write_1_CPR_ratio/8/1000/1000*(IF(IIR_en == 1, 1, 0))
            SRP_NR_out_Write_1_DDR_size = ROUNDUP(SRP_NR_out_Write_1_H_res/1024, 0)*1024*SRP_NR_out_Write_1_bits*SRP_NR_out_Write_1_VDE_res / \
                SRP_NR_out_Write_1_CPR_ratio/8/1024/1024*(IF(IIR_en == 1, IIR_buff_num, 0))
            return SRP_NR_out_Write_1_DDR_size, SRP_NR_out_Write_1_Bandwidth
        elif srp_type == SRPType.SRP_NR_OUT_WRITE_2:
            SRP_NR_out_Write_2_frame_rate = video_input_refresh_rate
            SRP_NR_out_Write_2_bits = video_data_width
            SRP_NR_out_Write_2_H_res = video_input_Hactive/4
            SRP_NR_out_Write_2_V_res = video_input_Vtotal
            SRP_NR_out_Write_2_VDE_res = video_input_Vactive
            SRP_NR_out_Write_2_CPR_ratio = video_comp_ratio
            SRP_NR_out_Write_2_Bandwidth = SRP_NR_out_Write_2_frame_rate*SRP_NR_out_Write_2_bits*SRP_NR_out_Write_2_H_res * \
                SRP_NR_out_Write_2_V_res/SRP_NR_out_Write_2_CPR_ratio/8/1000/1000*(IF(IIR_en == 1, 1, 0))
            SRP_NR_out_Write_2_DDR_size = ROUNDUP(SRP_NR_out_Write_2_H_res/1024, 0)*1024*SRP_NR_out_Write_2_bits*SRP_NR_out_Write_2_VDE_res / \
                SRP_NR_out_Write_2_CPR_ratio/8/1024/1024*(IF(IIR_en == 1, IIR_buff_num, 0))
            return SRP_NR_out_Write_2_DDR_size, SRP_NR_out_Write_2_Bandwidth
        elif srp_type == SRPType.SRP_NR_OUT_WRITE_3:
            SRP_NR_out_Write_3_frame_rate = video_input_refresh_rate
            SRP_NR_out_Write_3_bits = video_data_width
            SRP_NR_out_Write_3_H_res = video_input_Hactive/4
            SRP_NR_out_Write_3_V_res = video_input_Vtotal
            SRP_NR_out_Write_3_VDE_res = video_input_Vactive
            SRP_NR_out_Write_3_CPR_ratio = video_comp_ratio
            SRP_NR_out_Write_3_Bandwidth = SRP_NR_out_Write_3_frame_rate*SRP_NR_out_Write_3_bits*SRP_NR_out_Write_3_H_res * \
                SRP_NR_out_Write_3_V_res/SRP_NR_out_Write_3_CPR_ratio/8/1000/1000*(IF(IIR_en == 1, 1, 0))
            SRP_NR_out_Write_3_DDR_size = ROUNDUP(SRP_NR_out_Write_3_H_res/1024, 0)*1024*SRP_NR_out_Write_3_bits*SRP_NR_out_Write_3_VDE_res / \
                SRP_NR_out_Write_3_CPR_ratio/8/1024/1024*(IF(IIR_en == 1, IIR_buff_num, 0))
            return SRP_NR_out_Write_3_DDR_size, SRP_NR_out_Write_3_Bandwidth
        elif srp_type == SRPType.SRP_NR_OUT_WRITE_4:
            SRP_NR_out_Write_4_frame_rate = video_input_refresh_rate
            SRP_NR_out_Write_4_bits = video_data_width
            SRP_NR_out_Write_4_H_res = video_input_Hactive/4
            SRP_NR_out_Write_4_V_res = video_input_Vtotal
            SRP_NR_out_Write_4_VDE_res = video_input_Vactive
            SRP_NR_out_Write_4_CPR_ratio = video_comp_ratio
            SRP_NR_out_Write_4_Bandwidth = SRP_NR_out_Write_4_frame_rate*SRP_NR_out_Write_4_bits*SRP_NR_out_Write_4_H_res * \
                SRP_NR_out_Write_4_V_res/SRP_NR_out_Write_4_CPR_ratio/8/1000/1000*(IF(IIR_en == 1, 1, 0))
            SRP_NR_out_Write_4_DDR_size = ROUNDUP(SRP_NR_out_Write_4_H_res/1024, 0)*1024*SRP_NR_out_Write_4_bits*SRP_NR_out_Write_4_VDE_res / \
                SRP_NR_out_Write_4_CPR_ratio/8/1024/1024*(IF(IIR_en == 1, IIR_buff_num, 0))
            return SRP_NR_out_Write_4_DDR_size, SRP_NR_out_Write_4_Bandwidth
        else:
            assert False, "Unknown type"
