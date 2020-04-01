from mem_common import HEX2DEC, RegType, DEC2HEX, ROUNDUP, DDROp
from mem_reg import MemReg
from mem_agents.mem_agent import MemAgent
from mem_global_var import *


class MemAgent_KME_10(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self):
        super().__init__('KME_10', 'IP_MASK_W', DDROp.W)

        self._reg_kme_10_start_address0 = MemReg('reg_kme_10_start_address0', 'reg_kme_10_start_address0', RegType.START)
        self._reg_kme_10_start_address1 = MemReg('reg_kme_10_start_address1', 'reg_kme_10_start_address1', RegType.START)
        self._reg_kme_10_line_offset_addr = MemReg('reg_kme_10_line_offset_addr', 'reg_kme_10_line_offset_addr', RegType.OTHER)
        self._reg_kme_10_mode = MemReg('reg_kme_10_mode', 'reg_kme_10_mode', RegType.OTHER)
        self._reg_kme_10_mode.value = 1

    def calc_memory(self):
        KME_10_frame_rate = GV.ME_in_framerate
        KME_10_bits = 4
        KME_10_H_res = GV.MC_H_Hact/GV.LOGO_MC_ratio_H
        KME_10_V_res = GV.MC_H_Vtotal/GV.LOGO_MC_ratio_V
        KME_10_VDE_res = GV.MC_H_Vact/GV.LOGO_MC_ratio_V
        KME_10_CPR_ratio = GV.ME_CPR_ratio
        KME_10_Bandwidth = KME_10_frame_rate*KME_10_bits*KME_10_H_res*KME_10_V_res/KME_10_CPR_ratio/8/1000/1000*GV.MEMC_en*IF(GV.PC_mode, 0, 1)
        KME_10_DDR_size = KME_10_bits*KME_10_H_res*KME_10_VDE_res/KME_10_CPR_ratio/8/1024/1024*GV.MEMC_en*IF(GV.PC_mode, 0, 1)
        return KME_10_DDR_size, KME_10_Bandwidth

    def allocate_memory(self, reg_dict):
        # KME_10  1080*ROUNDUP(ROUNDUP(1920*data_width/CRP_ration,0)/128,0)*128/8
        C12 = 4  # data_width
        D12 = 1920  # H
        E12 = 1080  # V
        F12 = 1  # CPR ratio
        KME_10_LineOffset = DEC2HEX(ROUNDUP(ROUNDUP(D12*C12/F12, 0)/128, 0)*128/8)
        KME_10_LOGO_MASK = DEC2HEX((HEX2DEC(KME_10_LineOffset) * E12))

        reg_kme_10_start_address0 = self.start_addr

        reg_kme_10_start_address1 = reg_kme_10_start_address0
        reg_kme_10_line_offset_addr = KME_10_LineOffset
        reg_kme_10_mode = 1

        self._reg_kme_10_start_address0.value = reg_kme_10_start_address0
        self._reg_kme_10_start_address1.value = reg_kme_10_start_address1
        self._reg_kme_10_line_offset_addr.value = reg_kme_10_line_offset_addr
        self._reg_kme_10_mode.value = reg_kme_10_mode

        regs = [self._reg_kme_10_start_address0, self._reg_kme_10_start_address1]
        for reg in regs:
            reg.value += self.ddr_base_offset

        self.set_memory_range(reg_kme_10_start_address0, reg_kme_10_start_address0 + KME_10_LOGO_MASK)

    @property
    def registers(self):
        return [self._reg_kme_10_start_address0,
                self._reg_kme_10_start_address1,
                self._reg_kme_10_line_offset_addr,
                self._reg_kme_10_mode]
