from mem_common import HEX2DEC, RegType, DEC2HEX, ROUNDUP, DDROp
from mem_reg import MemReg
from mem_agents.mem_agent import MemAgent
from mem_global_var import *


class MemAgent_KME_14(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self):
        super().__init__('KME_14', 'HOG_history_W', DDROp.W)

        self._reg_kme_14_start_address0 = MemReg('reg_kme_14_start_address0', 'reg_kme_14_start_address0', RegType.START)
        self._reg_kme_14_start_address1 = MemReg('reg_kme_14_start_address1', 'reg_kme_14_start_address1', RegType.START)
        self._reg_kme_14_line_offset_addr = MemReg('reg_kme_14_line_offset_addr', 'reg_kme_14_line_offset_addr', RegType.OTHER)
        self._reg_kme_14_mode = MemReg('reg_kme_14_mode', 'reg_kme_14_mode', RegType.OTHER)
        self._reg_kme_14_mode.value = 1

    def calc_memory(self):
        KME_14_frame_rate = GV.ME_in_framerate
        KME_14_bits = 4
        KME_14_H_res = GV.MC_H_Hact/GV.ME1_block_size_H
        KME_14_V_res = GV.MC_H_Vtotal/GV.ME1_block_size_V
        KME_14_VDE_res = GV.MC_H_Vact/GV.ME1_block_size_V
        KME_14_CPR_ratio = GV.ME_CPR_ratio
        KME_14_Bandwidth = KME_14_frame_rate*KME_14_bits*KME_14_H_res*KME_14_V_res/KME_14_CPR_ratio/8/1000/1000*GV.MEMC_en*IF(GV.PC_mode, 0, 1)
        KME_14_DDR_size = KME_14_bits*KME_14_H_res*KME_14_VDE_res/KME_14_CPR_ratio/8/1024/1024*GV.MEMC_en*IF(GV.PC_mode, 0, 1)
        return KME_14_DDR_size, KME_14_Bandwidth

    def allocate_memory(self, reg_dict):

        # KME_14  270*ROUNDUP(ROUNDUP(480*data_width/CRP_ration,0)/128,0)*128/8
        C14 = 4  # data_width
        D14 = 480  # H
        E14 = 270  # V
        F14 = 1  # CPR ratio
        KME_14_LineOffset = DEC2HEX(ROUNDUP(ROUNDUP(D14*C14/F14, 0)/128, 0)*128/8)
        KME_14_HOG_history = DEC2HEX((HEX2DEC(KME_14_LineOffset) * E14))

        reg_kme_12_start_address1 = reg_dict['reg_kme_12_start_address1']
        KME_12_Pixel_LOGO = reg_dict['KME_12_Pixel_LOGO']

        reg_kme_14_start_address0 = DEC2HEX(HEX2DEC(reg_kme_12_start_address1)+HEX2DEC(KME_12_Pixel_LOGO))

        reg_kme_14_start_address1 = reg_kme_14_start_address0
        reg_kme_14_line_offset_addr = KME_14_LineOffset
        reg_kme_14_mode = 1

        self._reg_kme_14_start_address0.value = reg_kme_14_start_address0
        self._reg_kme_14_start_address1.value = reg_kme_14_start_address1
        self._reg_kme_14_line_offset_addr.value = reg_kme_14_line_offset_addr
        self._reg_kme_14_mode.value = reg_kme_14_mode

        regs = [self._reg_kme_14_start_address0, self._reg_kme_14_start_address1]
        for reg in regs:
            reg.value += self.ddr_base_offset

        self.set_memory_range(reg_kme_14_start_address0, None)

    @property
    def registers(self):
        return [self._reg_kme_14_start_address0,
                self._reg_kme_14_start_address1,
                self._reg_kme_14_line_offset_addr,
                self._reg_kme_14_mode]
