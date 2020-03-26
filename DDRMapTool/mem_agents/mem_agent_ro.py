from mem_common import *
from mem_agents.mem_agent import MemAgent
from mem_global_var import *


class MemAgent_RO(MemAgent):
    """
    Read Agent, no size
    """
    # pylint: disable=invalid-name

    def __init__(self, name, write_agent_name, module_name):
        super().__init__(name, module_name, DDROp.R)
        self._write_agent_name = write_agent_name

    def calc_memory(self):
        name = self.name
        if name == 'KMC_5':
            KMC_5_frame_rate = MC_H_out_framerate
            KMC_5_bits = MC_H_bits
            KMC_5_H_res = MC_H_Hact/2+MC_H_Hoverlap
            KMC_5_V_res = MC_H_Vtotal/2
            KMC_5_VDE_res = MC_H_Vact/2
            KMC_5_CPR_ratio = MC_H_CPR_ratio
            KMC_5_Bandwidth = KMC_5_frame_rate*KMC_5_bits*KMC_5_H_res*KMC_5_V_res/KMC_5_CPR_ratio/8/1000/1000
            KMC_5_DDR_size = 0
            return KMC_5_DDR_size, KMC_5_Bandwidth
        elif name == 'KMC_4':
            KMC_4_frame_rate = MC_H_out_framerate
            KMC_4_bits = MC_H_bits*IF(MC_single_mode, 0, 1)
            KMC_4_H_res = MC_H_Hact/2+MC_H_Hoverlap
            KMC_4_V_res = MC_H_Vtotal/2
            KMC_4_VDE_res = MC_H_Vact/2
            KMC_4_CPR_ratio = MC_H_CPR_ratio
            KMC_4_Bandwidth = KMC_4_frame_rate*KMC_4_bits*KMC_4_H_res*KMC_4_V_res/KMC_4_CPR_ratio/8/1000/1000
            KMC_4_DDR_size = 0
            return KMC_4_DDR_size, KMC_4_Bandwidth
        elif name == 'KMC_7':
            KMC_7_frame_rate = MC_L_out_framerate
            KMC_7_bits = MC_L_bits
            KMC_7_H_res = MC_L_Hact/2+MC_L_Hoverlap
            KMC_7_V_res = MC_L_Vtotal/2
            KMC_7_VDE_res = MC_L_Vact/2
            KMC_7_CPR_ratio = MC_L_CPR_ratio
            KMC_7_Bandwidth = KMC_7_frame_rate*KMC_7_bits*KMC_7_H_res*KMC_7_V_res/KMC_7_CPR_ratio/8/1000/1000
            KMC_7_DDR_size = 0
            return KMC_7_DDR_size, KMC_7_Bandwidth
        elif name == 'KMC_6':
            KMC_6_frame_rate = MC_L_out_framerate
            KMC_6_bits = MC_L_bits
            KMC_6_H_res = MC_L_Hact/2+MC_L_Hoverlap
            KMC_6_V_res = MC_L_Vtotal/2
            KMC_6_VDE_res = MC_L_Vact/2
            KMC_6_CPR_ratio = MC_L_CPR_ratio
            KMC_6_Bandwidth = KMC_6_frame_rate*KMC_6_bits*KMC_6_H_res*KMC_6_V_res/KMC_6_CPR_ratio/8/1000/1000
            KMC_6_DDR_size = 0
            KMC_6_DDR_size = 0
            return KMC_6_DDR_size, KMC_6_Bandwidth
        elif name == 'KMC_11':
            KMC_5_frame_rate = MC_H_out_framerate
            KMC_5_bits = MC_H_bits
            KMC_5_H_res = MC_H_Hact/2+MC_H_Hoverlap
            KMC_5_V_res = MC_H_Vtotal/2
            KMC_5_VDE_res = MC_H_Vact/2
            KMC_5_CPR_ratio = MC_H_CPR_ratio
            KMC_5_Bandwidth = KMC_5_frame_rate*KMC_5_bits*KMC_5_H_res*KMC_5_V_res/KMC_5_CPR_ratio/8/1000/1000
            KMC_5_DDR_size = 0
            return KMC_5_DDR_size, KMC_5_Bandwidth
        elif name == 'KMC_10':
            KMC_10_frame_rate = MC_H_out_framerate
            KMC_10_bits = MC_H_bits*IF(MC_single_mode, 0, 1)
            KMC_10_H_res = MC_H_Hact/2+MC_H_Hoverlap
            KMC_10_V_res = MC_H_Vtotal/2
            KMC_10_VDE_res = MC_H_Vact/2
            KMC_10_CPR_ratio = MC_H_CPR_ratio
            KMC_10_Bandwidth = KMC_10_frame_rate*KMC_10_bits*KMC_10_H_res*KMC_10_V_res/KMC_10_CPR_ratio/8/1000/1000
            KMC_10_DDR_size = 0
            return KMC_10_DDR_size, KMC_10_Bandwidth
        elif name == 'KMC_13':
            KMC_13_frame_rate = MC_L_out_framerate
            KMC_13_bits = MC_L_bits
            KMC_13_H_res = MC_L_Hact/2+MC_L_Hoverlap
            KMC_13_V_res = MC_L_Vtotal/2
            KMC_13_VDE_res = MC_L_Vact/2
            KMC_13_CPR_ratio = MC_L_CPR_ratio
            KMC_13_Bandwidth = KMC_13_frame_rate*KMC_13_bits*KMC_13_H_res*KMC_13_V_res/KMC_13_CPR_ratio/8/1000/1000
            KMC_13_DDR_size = 0
            return KMC_13_DDR_size, KMC_13_Bandwidth
        elif name == 'KMC_12':
            KMC_12_frame_rate = MC_L_out_framerate
            KMC_12_bits = MC_L_bits
            KMC_12_H_res = MC_L_Hact/2+MC_L_Hoverlap
            KMC_12_V_res = MC_L_Vtotal/2
            KMC_12_VDE_res = MC_L_Vact/2
            KMC_12_CPR_ratio = MC_L_CPR_ratio
            KMC_12_Bandwidth = KMC_12_frame_rate*KMC_12_bits*KMC_12_H_res*KMC_12_V_res/KMC_12_CPR_ratio/8/1000/1000*IF(PC_mode, 0, 1)
            KMC_12_DDR_size = 0
            return KMC_12_DDR_size, KMC_12_Bandwidth
        elif name == 'KME_1':
            KME_1_frame_rate = ME_in_framerate
            KME_1_bits = ME_bits
            KME_1_H_res = ME_Hact+ME_Hoverlap
            KME_1_V_res = ME_Vtotal
            KME_1_VDE_res = ME_Vact
            KME_1_CPR_ratio = ME_CPR_ratio
            KME_1_Bandwidth = KME_1_frame_rate*KME_1_bits*KME_1_H_res*KME_1_V_res/KME_1_CPR_ratio/8/1000/1000
            KME_1_DDR_size = 0
            return KME_1_DDR_size, KME_1_Bandwidth
        elif name == 'KME_3':
            KME_3_frame_rate = ME_out_framerate
            KME_3_bits = ME_bits
            KME_3_H_res = ME_Hact+ME_Hoverlap
            KME_3_V_res = ME_Vtotal
            KME_3_VDE_res = ME_Vact
            KME_3_CPR_ratio = ME_CPR_ratio
            KME_3_Bandwidth = KME_3_frame_rate*KME_3_bits*KME_3_H_res*KME_3_V_res/KME_3_CPR_ratio/8/1000/1000
            KME_3_DDR_size = 0
            return KME_3_DDR_size, KME_3_Bandwidth
        elif name == 'KME_2':
            KME_2_frame_rate = ME_out_framerate
            KME_2_bits = ME_bits
            KME_2_H_res = ME_Hact+ME_Hoverlap
            KME_2_V_res = ME_Vtotal
            KME_2_VDE_res = ME_Vact
            KME_2_CPR_ratio = ME_CPR_ratio
            KME_2_Bandwidth = KME_2_frame_rate*KME_2_bits*KME_2_H_res*KME_2_V_res/KME_2_CPR_ratio/8/1000/1000
            KME_2_DDR_size = 0
            return KME_2_DDR_size, KME_2_Bandwidth
        elif name == 'KMV_11':
            KMV_11_frame_rate = ME_out_framerate
            KMV_11_bits = ME_bits
            KMV_11_H_res = ME_Hact+ME_Hoverlap
            KMV_11_V_res = ME_Vtotal
            KMV_11_VDE_res = ME_Vact
            KMV_11_CPR_ratio = ME_CPR_ratio
            KMV_11_Bandwidth = KMV_11_frame_rate*KMV_11_bits*KMV_11_H_res*KMV_11_V_res/KMV_11_CPR_ratio/8/1000/1000
            KMV_11_DDR_size = 0
            return KMV_11_DDR_size, KMV_11_Bandwidth
        elif name == 'KMV_10':
            KMV_10_frame_rate = ME_out_framerate
            KMV_10_bits = ME_bits
            KMV_10_H_res = ME_Hact+ME_Hoverlap
            KMV_10_V_res = ME_Vtotal
            KMV_10_VDE_res = ME_Vact
            KMV_10_CPR_ratio = ME_CPR_ratio
            KMV_10_Bandwidth = KMV_10_frame_rate*KMV_10_bits*KMV_10_H_res*KMV_10_V_res/KMV_10_CPR_ratio/8/1000/1000
            KMV_10_DDR_size = 0
            return KMV_10_DDR_size, KMV_10_Bandwidth
        elif name == 'KME_9':
            KME_9_frame_rate = ME_in_framerate
            KME_9_bits = ME_bits
            KME_9_H_res = MC_H_Hact/LOGO_MC_ratio_H
            KME_9_V_res = MC_H_Vtotal/LOGO_MC_ratio_V
            KME_9_VDE_res = MC_H_Vact/LOGO_MC_ratio_V
            KME_9_CPR_ratio = ME_CPR_ratio
            KME_9_Bandwidth = KME_9_frame_rate*KME_9_bits*KME_9_H_res*KME_9_V_res/KME_9_CPR_ratio/8/1000/1000*MEMC_en*IF(PC_mode, 0, 1)
            KME_9_DDR_size = 0
            return KME_9_DDR_size, KME_9_Bandwidth
        elif name == 'KME_11':
            KME_11_frame_rate = ME_in_framerate
            KME_11_bits = 4
            KME_11_H_res = MC_H_Hact/LOGO_MC_ratio_H
            KME_11_V_res = MC_H_Vtotal/LOGO_MC_ratio_V
            KME_11_VDE_res = MC_H_Vact/LOGO_MC_ratio_V
            KME_11_CPR_ratio = ME_CPR_ratio
            KME_11_Bandwidth = KME_11_frame_rate*KME_11_bits*KME_11_H_res*KME_11_V_res/KME_11_CPR_ratio/8/1000/1000*MEMC_en*IF(PC_mode, 0, 1)
            KME_11_DDR_size = 0
            return KME_11_DDR_size, KME_11_Bandwidth
        elif name == 'KME_13':
            KME_13_frame_rate = ME_out_framerate
            KME_13_bits = 1
            KME_13_H_res = MC_H_Hact/LOGO_MC_ratio_H
            KME_13_V_res = MC_H_Vtotal/LOGO_MC_ratio_V
            KME_13_VDE_res = MC_H_Vact/LOGO_MC_ratio_V
            KME_13_CPR_ratio = ME_CPR_ratio
            KME_13_Bandwidth = KME_13_frame_rate*KME_13_bits*KME_13_H_res*KME_13_V_res/KME_13_CPR_ratio/8/1000/1000*MEMC_en*IF(PC_mode, 0, 1)
            KME_13_DDR_size = 0
            return KME_13_DDR_size, KME_13_Bandwidth
        elif name == 'KME_15':
            KME_15_frame_rate = ME_in_framerate
            KME_15_bits = 4
            KME_15_H_res = MC_H_Hact/ME1_block_size_H
            KME_15_V_res = MC_H_Vtotal/ME1_block_size_V
            KME_15_VDE_res = MC_H_Vact/ME1_block_size_V
            KME_15_CPR_ratio = ME_CPR_ratio
            KME_15_Bandwidth = KME_15_frame_rate*KME_15_bits*KME_15_H_res*KME_15_V_res/KME_15_CPR_ratio/8/1000/1000*MEMC_en*IF(PC_mode, 0, 1)
            KME_15_DDR_size = 0
            return KME_15_DDR_size, KME_15_Bandwidth
        elif name == 'KMV_07':
            KMV_07_frame_rate = ME_out_framerate
            KMV_07_bits = 21
            KMV_07_H_res = MC_H_Hact/ME1_block_size_H
            KMV_07_V_res = MC_H_Vtotal/ME1_block_size_V
            KMV_07_VDE_res = MC_H_Vact/ME1_block_size_V
            KMV_07_CPR_ratio = ME_CPR_ratio
            KMV_07_Bandwidth = KMV_07_frame_rate*KMV_07_bits*KMV_07_H_res*KMV_07_V_res/KMV_07_CPR_ratio/8/1000/1000*MEMC_en*IF(PC_mode, 0, 1)
            KMV_07_DDR_size = 0
            return KMV_07_DDR_size, KMV_07_Bandwidth
        elif name == 'KMV_03':
            KMV_03_frame_rate = ME_out_framerate
            KMV_03_bits = 40
            KMV_03_H_res = MC_H_Hact/ME1_block_size_H
            KMV_03_V_res = MC_H_Vtotal/ME1_block_size_V
            KMV_03_VDE_res = MC_H_Vact/ME1_block_size_V
            KMV_03_CPR_ratio = ME_CPR_ratio
            KMV_03_Bandwidth = KMV_03_frame_rate*KMV_03_bits*KMV_03_H_res*KMV_03_V_res/KMV_03_CPR_ratio/8/1000/1000*MEMC_en*IF(PC_mode, 0, 1)
            KMV_03_DDR_size = 0
            return KMV_03_DDR_size, KMV_03_Bandwidth
        elif name == 'KMV_08':
            KMV_08_frame_rate = ME_out_framerate
            KMV_08_bits = 33
            KMV_08_H_res = MC_H_Hact/ME1_block_size_H
            KMV_08_V_res = MC_H_Vtotal/ME1_block_size_V
            KMV_08_VDE_res = MC_H_Vact/ME1_block_size_V
            KMV_08_CPR_ratio = ME_CPR_ratio
            KMV_08_Bandwidth = KMV_08_frame_rate*KMV_08_bits*KMV_08_H_res*KMV_08_V_res/KMV_08_CPR_ratio/8/1000/1000*MEMC_en*IF(PC_mode, 0, 1)
            KMV_08_DDR_size = 0
            return KMV_08_DDR_size, KMV_08_Bandwidth
        elif name == 'KMV_09':
            KMV_09_frame_rate = ME_out_framerate
            KMV_09_bits = 64
            KMV_09_H_res = MC_H_Hact/ME1_block_size_H
            KMV_09_V_res = MC_H_Vtotal/ME1_block_size_V
            KMV_09_VDE_res = MC_H_Vact/ME1_block_size_V
            KMV_09_CPR_ratio = ME_CPR_ratio
            KMV_09_Bandwidth = KMV_09_frame_rate*KMV_09_bits*KMV_09_H_res*KMV_09_V_res/KMV_09_CPR_ratio/8/1000/1000*MEMC_en*IF(PC_mode, 0, 1)
            KMV_09_DDR_size = 0
            return KMV_09_DDR_size, KMV_09_Bandwidth
        elif name == 'KMV_06':
            KMV_06_frame_rate = ME_out_framerate
            KMV_06_bits = 64
            KMV_06_H_res = MC_H_Hact/ME1_block_size_H
            KMV_06_V_res = MC_H_Vtotal/ME1_block_size_V
            KMV_06_VDE_res = MC_H_Vact/ME1_block_size_V
            KMV_06_CPR_ratio = ME_CPR_ratio
            KMV_06_Bandwidth = KMV_06_frame_rate*KMV_06_bits*KMV_06_H_res*KMV_06_V_res/KMV_06_CPR_ratio/8/1000/1000*MEMC_en*IF(PC_mode, 0, 1)
            KMV_06_DDR_size = 0
            return KMV_06_DDR_size, KMV_06_Bandwidth
        elif name == 'OD_R':
            OD_R_frame_rate = TOP_OD_framerate
            OD_R_bits = TOP_OD_bits
            OD_R_H_res = TOP_OD_Hact / 2
            OD_R_V_res = TOP_OD_Vtotal
            OD_R_VDE_res = TOP_OD_Vact
            OD_R_CPR_ratio = TOP_OD_CPR_ratio
            OD_R_Bandwidth = OD_R_frame_rate*OD_R_bits*OD_R_H_res*OD_R_V_res/OD_R_CPR_ratio/8/1000/1000
            OD_R_DDR_size = 0
            return OD_R_DDR_size, OD_R_Bandwidth
        elif name == 'TOP_OD_R':
            TOP_OD_R_frame_rate = TOP_OD_framerate
            TOP_OD_R_bits = TOP_OD_bits
            TOP_OD_R_H_res = TOP_OD_Hact / 2
            TOP_OD_R_V_res = TOP_OD_Vtotal
            TOP_OD_R_VDE_res = TOP_OD_Vact
            TOP_OD_R_CPR_ratio = TOP_OD_CPR_ratio
            TOP_OD_R_Bandwidth = TOP_OD_R_frame_rate*TOP_OD_R_bits*TOP_OD_R_H_res*TOP_OD_R_V_res/TOP_OD_R_CPR_ratio/8/1000/1000
            TOP_OD_R_DDR_size = 0
            return TOP_OD_R_DDR_size, TOP_OD_R_Bandwidth
        elif name == 'BOT_OD_R':
            BOT_OD_R_frame_rate = BOT_OD_framerate
            BOT_OD_R_bits = BOT_OD_bits
            BOT_OD_R_H_res = BOT_OD_Hact
            BOT_OD_R_V_res = BOT_OD_Vtotal
            BOT_OD_R_VDE_res = BOT_OD_Vact
            BOT_OD_R_CPR_ratio = BOT_OD_CPR_ratio
            BOT_OD_R_Bandwidth = BOT_OD_R_frame_rate*BOT_OD_R_bits*BOT_OD_R_H_res*BOT_OD_R_V_res/BOT_OD_R_CPR_ratio/8/1000/1000
            BOT_OD_R_DDR_size = 0
            return BOT_OD_R_DDR_size, BOT_OD_R_Bandwidth
        else:
            assert False, "Unknown agent:%s" % name

    @property
    def write_agent_name(self):
        return self._write_agent_name

    def get_regs(self, reg_dict):
        write_agent_start_addr_name = '%s_start_addr' % self._write_agent_name
        assert write_agent_start_addr_name in reg_dict
        self.start_addr = reg_dict[write_agent_start_addr_name]
        self.end_addr = self.start_addr
        return []
