from mem_common import HEX2DEC, RegType, DEC2HEX, ROUNDUP, DDROp
from mem_reg import MemReg
from mem_agents.mem_agent import MemAgent
from mem_global_var import *


class MemAgent_BOT_OD_W(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self):
        super().__init__('BOT_OD_W', 'BOT_OD_W', DDROp.W)

        self._reg_kod_wdma_00_start_address0 = MemReg('reg_kod_wdma_00_start_address0', 'reg_kod_wdma_00_start_address0', RegType.START)
        self._reg_kod_wdma_00_start_address1 = MemReg('reg_kod_wdma_00_start_address1', 'reg_kod_wdma_00_start_address1', RegType.START)
        self._reg_kod_wdma_00_start_address2 = MemReg('reg_kod_wdma_00_start_address2', 'reg_kod_wdma_00_start_address2', RegType.START)
        self._reg_kod_wdma_00_start_address3 = MemReg('reg_kod_wdma_00_start_address3', 'reg_kod_wdma_00_start_address3', RegType.START)

    def calc_memory(self):
        BOT_OD_W_frame_rate = BOT_OD_framerate
        BOT_OD_W_bits = BOT_OD_bits
        BOT_OD_W_H_res = BOT_OD_Hact
        BOT_OD_W_V_res = BOT_OD_Vtotal
        BOT_OD_W_VDE_res = BOT_OD_Vact
        BOT_OD_W_CPR_ratio = BOT_OD_CPR_ratio
        BOT_OD_W_Bandwidth = BOT_OD_W_frame_rate*BOT_OD_W_bits*BOT_OD_W_H_res*BOT_OD_W_V_res/BOT_OD_W_CPR_ratio/8/1000/1000
        BOT_OD_W_DDR_size = BOT_OD_W_bits*BOT_OD_W_H_res*BOT_OD_W_VDE_res/BOT_OD_W_CPR_ratio/8/1024/1024
        return BOT_OD_W_DDR_size, BOT_OD_W_Bandwidth

    def allocate_memory(self, reg_dict):

        # BOT_OD
        C21 = 8  # data_width
        D21 = 3840  # H
        E21 = 2160  # V
        F21 = 4  # CPR ratio
        G21 = DEC2HEX(ROUNDUP(ROUNDUP(D21*C21/F21, 0)/128, 0)*128/8)
        TOP_OD = DEC2HEX((HEX2DEC(G21) * E21))

        TOP_DEMURA = reg_dict['TOP_DEMURA']
        reg_ptc_04_start_address0 = reg_dict['reg_ptc_04_start_address0']

        reg_kod_wdma_00_start_address0 = DEC2HEX(HEX2DEC(reg_ptc_04_start_address0)+HEX2DEC(TOP_DEMURA))

        reg_kod_wdma_00_start_address1 = reg_kod_wdma_00_start_address0
        reg_kod_wdma_00_start_address2 = reg_kod_wdma_00_start_address0
        reg_kod_wdma_00_start_address3 = reg_kod_wdma_00_start_address0
        reg_dict['reg_kod_wdma_00_start_address3'] = reg_kod_wdma_00_start_address3

        self._reg_kod_wdma_00_start_address0.value = reg_kod_wdma_00_start_address0
        self._reg_kod_wdma_00_start_address1.value = reg_kod_wdma_00_start_address1
        self._reg_kod_wdma_00_start_address2.value = reg_kod_wdma_00_start_address2
        self._reg_kod_wdma_00_start_address3.value = reg_kod_wdma_00_start_address3

        self.set_memory_range(reg_kod_wdma_00_start_address0, reg_kod_wdma_00_start_address0 + TOP_OD)

    @property
    def registers(self):
        return [self._reg_kod_wdma_00_start_address0,
                self._reg_kod_wdma_00_start_address1,
                self._reg_kod_wdma_00_start_address2,
                self._reg_kod_wdma_00_start_address3]
