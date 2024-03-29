from mem_common import HEX2DEC, RegType, DEC2HEX, ROUNDUP, DDROp
from mem_reg import MemReg
from mem_agents.mem_agent import MemAgent
from mem_global_var import *


class MemAgent_KMV_02(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self):
        super().__init__('KMV_02', 'ME1_Loop_PPI_W', DDROp.W)

        self._reg_mv02_start_address0 = MemReg('reg_mv02_start_address0', 'reg_mv02_start_address0', RegType.START)
        self._reg_mv02_end_address0 = MemReg('reg_mv02_end_address0', 'reg_mv02_end_address0', RegType.END)
        self._reg_mv02_line_offset_addr = MemReg('reg_mv02_line_offset_addr', 'reg_mv02_line_offset_addr', RegType.OTHER)
        self._reg_mv02_mode = MemReg('reg_mv02_mode', 'reg_mv02_mode', RegType.OTHER)

    def calc_memory(self):
        KMV_02_frame_rate = GV.ME_out_framerate
        KMV_02_bits = 40
        KMV_02_H_res = GV.MC_H_Hact/GV.ME1_block_size_H
        KMV_02_V_res = GV.MC_H_Vtotal/GV.ME1_block_size_V
        KMV_02_VDE_res = GV.MC_H_Vact/GV.ME1_block_size_V
        KMV_02_CPR_ratio = GV.ME_CPR_ratio
        KMV_02_Bandwidth = KMV_02_frame_rate*KMV_02_bits*KMV_02_H_res*KMV_02_V_res/KMV_02_CPR_ratio/8/1000/1000*GV.MEMC_en*IF(GV.PC_mode, 0, 1)
        KMV_02_DDR_size = KMV_02_bits*KMV_02_H_res*KMV_02_VDE_res/KMV_02_CPR_ratio/8/1024/1024*GV.MEMC_en*IF(GV.PC_mode, 0, 1)
        return KMV_02_DDR_size, KMV_02_Bandwidth

    def allocate_memory(self, reg_dict):

        # KMV_02  270*ROUNDUP(ROUNDUP(480*data_width/CRP_ration,0)/128,0)*128/8
        C16 = 40  # data_width
        D16 = 480  # H
        E16 = 270  # V
        F16 = 1  # CPR ratio
        ROW_NUM = 270
        KMV_02_Line_Offset = DEC2HEX(ROUNDUP(ROUNDUP(D16*C16/F16, 0)/128, 0)*128/8)
        KMV_02_MV = DEC2HEX((HEX2DEC(KMV_02_Line_Offset) * E16))

        reg_mv02_start_address0 = self.start_addr
        reg_mv02_end_address0 = DEC2HEX(HEX2DEC(reg_mv02_start_address0)+HEX2DEC(KMV_02_Line_Offset)*ROW_NUM)
        reg_mv02_line_offset_addr = KMV_02_Line_Offset
        reg_mv02_lr_offset_addr = DEC2HEX(HEX2DEC(KMV_02_MV)/2)

        self._reg_mv02_start_address0.value = reg_mv02_start_address0
        self._reg_mv02_end_address0.value = reg_mv02_end_address0
        self._reg_mv02_line_offset_addr.value = reg_mv02_line_offset_addr
        self._reg_mv02_mode.value = 1

        regs = [self._reg_mv02_start_address0, self._reg_mv02_end_address0]
        for reg in regs:
            reg.value += self.ddr_base_offset

        self.set_memory_range(reg_mv02_start_address0, reg_mv02_end_address0)

    @property
    def registers(self):
        return [self._reg_mv02_start_address0,
                self._reg_mv02_end_address0,
                self._reg_mv02_line_offset_addr,
                self._reg_mv02_mode]
