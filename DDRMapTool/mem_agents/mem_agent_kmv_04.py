from mem_common import HEX2DEC, RegType, DEC2HEX, ROUNDUP, DDROp
from mem_reg import MemReg
from mem_agents.mem_agent import MemAgent
from mem_global_var import *


class MemAgent_KMV_04(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self):
        super().__init__('KMV_04', 'ME1_VBUF_PPFV_W', DDROp.W)

        self._reg_mv04_start_address0 = MemReg('reg_mv04_start_address0', 'reg_mv04_start_address0', RegType.START)
        self._reg_mv04_start_address1 = MemReg('reg_mv04_start_address1', 'reg_mv04_start_address1', RegType.START)
        self._reg_mv04_start_address2 = MemReg('reg_mv04_start_address2', 'reg_mv04_start_address2', RegType.START)
        self._reg_mv04_end_address0 = MemReg('reg_mv04_end_address0', 'reg_mv04_end_address0', RegType.START)
        self._reg_mv04_end_address1 = MemReg('reg_mv04_end_address1', 'reg_mv04_end_address1', RegType.START)
        self._reg_mv04_end_address2 = MemReg('reg_mv04_end_address2', 'reg_mv04_end_address2', RegType.START)
        self._reg_mv04_line_offset_addr = MemReg('reg_mv04_line_offset_addr', 'reg_mv04_line_offset_addr', RegType.OTHER)
        self._reg_mv04_mode = MemReg('reg_mv04_mode', 'reg_mv04_mode', RegType.OTHER)

    def calc_memory(self):
        KMV_04_frame_rate = ME_out_framerate
        KMV_04_bits = 33
        KMV_04_H_res = MC_H_Hact/ME1_block_size_H
        KMV_04_V_res = MC_H_Vtotal/ME1_block_size_V
        KMV_04_VDE_res = MC_H_Vact/ME1_block_size_V
        KMV_04_CPR_ratio = ME_CPR_ratio
        KMV_04_Bandwidth = KMV_04_frame_rate*KMV_04_bits*KMV_04_H_res*KMV_04_V_res/KMV_04_CPR_ratio/8/1000/1000*MEMC_en*IF(PC_mode, 0, 1)
        KMV_04_DDR_size = KMV_04_bits*KMV_04_H_res*KMV_04_VDE_res/KMV_04_CPR_ratio/8/1024/1024*MEMC_en*IF(PC_mode, 0, 1)
        return KMV_04_DDR_size, KMV_04_Bandwidth

    def allocate_memory(self, reg_dict):

        # KMV_04  270*ROUNDUP(ROUNDUP(480*data_width/CRP_ration,0)/128,0)*128/8
        C17 = 33  # data_width
        D17 = 480  # H
        E17 = 270  # V
        F17 = 1  # CPR ratio
        ROW_NUM = 270
        KMV_04_Line_Offset = DEC2HEX(ROUNDUP(ROUNDUP(D17*C17/F17, 0)/128, 0)*128/8)
        KMV_04_MV = DEC2HEX((HEX2DEC(KMV_04_Line_Offset) * E17))
        reg_dict['KMV_04_MV'] = KMV_04_MV
        reg_mv02_start_address0 = reg_dict['reg_mv02_start_address0']
        KMV_02_MV = reg_dict['KMV_02_MV']

        reg_mv04_start_address0 = DEC2HEX(HEX2DEC(reg_mv02_start_address0)+HEX2DEC(KMV_02_MV))
        reg_mv04_start_address1 = DEC2HEX(HEX2DEC(reg_mv04_start_address0)+HEX2DEC(KMV_04_MV))
        reg_mv04_start_address2 = DEC2HEX(HEX2DEC(reg_mv04_start_address1)+HEX2DEC(KMV_04_MV))
        reg_dict['reg_mv04_start_address2'] = reg_mv04_start_address2

        reg_mv04_end_address0 = DEC2HEX(HEX2DEC(reg_mv04_start_address0)+HEX2DEC(KMV_04_Line_Offset)*ROW_NUM)
        reg_mv04_end_address1 = DEC2HEX(HEX2DEC(reg_mv04_start_address1)+HEX2DEC(KMV_04_Line_Offset)*ROW_NUM)
        reg_mv04_end_address2 = DEC2HEX(HEX2DEC(reg_mv04_start_address2)+HEX2DEC(KMV_04_Line_Offset)*ROW_NUM)
        reg_mv04_line_offset_addr = KMV_04_Line_Offset
        reg_mv04_lr_offset_addr = DEC2HEX(HEX2DEC(KMV_04_MV)/2)

        self._reg_mv04_start_address0.value = reg_mv04_start_address0
        self._reg_mv04_start_address1.value = reg_mv04_start_address1
        self._reg_mv04_start_address2.value = reg_mv04_start_address2
        self._reg_mv04_end_address0.value = reg_mv04_end_address0
        self._reg_mv04_end_address1.value = reg_mv04_end_address1
        self._reg_mv04_end_address2.value = reg_mv04_end_address2
        self._reg_mv04_line_offset_addr.value = reg_mv04_line_offset_addr
        self._reg_mv04_mode.value = 1

        regs = [self._reg_mv04_start_address0,
                self._reg_mv04_start_address1,
                self._reg_mv04_start_address2,
                self._reg_mv04_end_address0,
                self._reg_mv04_end_address1,
                self._reg_mv04_end_address2]
        for reg in regs:
            reg.value += self.ddr_base_offset

        self.set_memory_range(reg_mv04_start_address0, reg_mv04_end_address2)

    @property
    def registers(self):
        return [self._reg_mv04_start_address0,
                self._reg_mv04_start_address1,
                self._reg_mv04_start_address2,
                self._reg_mv04_end_address0,
                self._reg_mv04_end_address1,
                self._reg_mv04_end_address2,
                self._reg_mv04_line_offset_addr,
                self._reg_mv04_mode]
