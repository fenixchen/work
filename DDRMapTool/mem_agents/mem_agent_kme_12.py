from mem_common import HEX2DEC, RegType, DEC2HEX, ROUNDUP, DDROp
from mem_reg import MemReg
from mem_agents.mem_agent import MemAgent
from mem_global_var import *


class MemAgent_KME_12(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self):
        super().__init__('KME_12', 'Pixel_LOGO_W', DDROp.W)

        self._reg_kme_12_start_address0 = MemReg('reg_kme_12_start_address0', 'reg_kme_12_start_address0', RegType.START)
        self._reg_kme_12_end_address0 = MemReg('reg_kme_12_end_address0', 'reg_kme_12_end_address0', RegType.END)
        self._reg_kme_12_start_address1 = MemReg('reg_kme_12_start_address1', 'reg_kme_12_start_address1', RegType.START)
        self._reg_kme_12_end_address1 = MemReg('reg_kme_12_end_address1', 'reg_kme_12_end_address1', RegType.END)
        self._reg_kme_12_line_offset_addr = MemReg('reg_kme_12_line_offset_addr', 'reg_kme_12_line_offset_addr', RegType.OTHER)
        self._reg_kme_12_mode = MemReg('reg_kme_12_mode', 'reg_kme_12_mode', RegType.OTHER)
        self._reg_kme_12_mode.value = 1

    def calc_memory(self):
        KME_12_frame_rate = GV.ME_in_framerate
        KME_12_bits = 1
        KME_12_H_res = GV.MC_H_Hact/GV.LOGO_MC_ratio_H
        KME_12_V_res = GV.MC_H_Vtotal/GV.LOGO_MC_ratio_V
        KME_12_VDE_res = GV.MC_H_Vact/GV.LOGO_MC_ratio_V
        KME_12_CPR_ratio = GV.ME_CPR_ratio
        KME_12_Bandwidth = KME_12_frame_rate*KME_12_bits*KME_12_H_res*KME_12_V_res/KME_12_CPR_ratio/8/1000/1000*GV.MEMC_en*IF(GV.PC_mode, 0, 1)
        KME_12_DDR_size = KME_12_bits*KME_12_H_res*KME_12_VDE_res/KME_12_CPR_ratio/8/1024/1024*GV.MEMC_en*IF(GV.PC_mode, 0, 1)
        return KME_12_DDR_size, KME_12_Bandwidth

    def allocate_memory(self, reg_dict):
        # KME_12  1080*ROUNDUP(ROUNDUP(1920*data_width/CRP_ration,0)/128,0)*128/8
        C13 = 1  # data_width
        D13 = 1920  # H
        E13 = 1080  # V
        F13 = 1  # CPR ratio
        KME_12_LineOffset = DEC2HEX(ROUNDUP(ROUNDUP(D13*C13/F13, 0)/128, 0)*128/8)
        KME_12_Pixel_LOGO = DEC2HEX((HEX2DEC(KME_12_LineOffset) * E13))

        LOGO_VACT = 1080

        reg_kme_12_start_address0 = self.start_addr

        reg_kme_12_start_address1 = reg_kme_12_start_address0

        reg_kme_12_end_address0 = DEC2HEX(HEX2DEC(reg_kme_12_start_address0)+HEX2DEC(KME_12_LineOffset)*LOGO_VACT)
        reg_kme_12_end_address1 = reg_kme_12_end_address0
        reg_kme_12_line_offset_addr = KME_12_LineOffset
        reg_kme_12_mode = 1

        self._reg_kme_12_start_address0.value = reg_kme_12_start_address0
        self._reg_kme_12_end_address0.value = reg_kme_12_end_address0
        self._reg_kme_12_start_address1.value = reg_kme_12_start_address1
        self._reg_kme_12_end_address1.value = reg_kme_12_end_address1
        self._reg_kme_12_line_offset_addr.value = reg_kme_12_line_offset_addr
        self._reg_kme_12_mode.value = reg_kme_12_mode

        regs = [self._reg_kme_12_start_address0,
                self._reg_kme_12_start_address1,
                self._reg_kme_12_end_address0,
                self._reg_kme_12_end_address1
                ]
        for reg in regs:
            reg.value += self.ddr_base_offset

        self.set_memory_range(reg_kme_12_start_address0, reg_kme_12_start_address1 + KME_12_Pixel_LOGO)

    @property
    def registers(self):
        return [self._reg_kme_12_start_address0,
                self._reg_kme_12_start_address1,
                self._reg_kme_12_end_address0,
                self._reg_kme_12_end_address1,
                self._reg_kme_12_line_offset_addr,
                self._reg_kme_12_mode]
