from mem_common import HEX2DEC, RegType, DEC2HEX, ROUNDUP, DDROp
from mem_reg import MemReg
from mem_agents.mem_agent import MemAgent
from mem_global_var import *


class MemAgent_OD_W(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self):
        super().__init__('OD_W', 'TOP_OD_W_L', DDROp.W)

        self._reg_ptc_00_start_address0 = MemReg('reg_ptc_00_start_address0', 'reg_ptc_00_start_address0', RegType.START)
        self._reg_ptc_00_start_address1 = MemReg('reg_ptc_00_start_address1', 'reg_ptc_00_start_address1', RegType.START)

    def calc_memory(self):
        OD_W_frame_rate = GV.TOP_OD_framerate
        OD_W_bits = GV.TOP_OD_bits
        OD_W_H_res = GV.TOP_OD_Hact / 2
        OD_W_V_res = GV.TOP_OD_Vtotal
        OD_W_VDE_res = GV.TOP_OD_Vact
        OD_W_CPR_ratio = GV.TOP_OD_CPR_ratio
        OD_W_Bandwidth = OD_W_frame_rate*OD_W_bits*OD_W_H_res*OD_W_V_res/OD_W_CPR_ratio/8/1000/1000
        OD_W_DDR_size = OD_W_bits*OD_W_H_res*OD_W_VDE_res/OD_W_CPR_ratio/8/1024/1024
        return OD_W_DDR_size, OD_W_Bandwidth

    def allocate_memory(self, reg_dict):

        # TOP_OD  V*ROUNDUP(ROUNDUP(H*data_width/CRP_ration,0)/128,0)*128/8
        C20 = 24  # data_width
        D20 = 3840  # H
        E20 = 4320  # V
        F20 = 11.66  # CPR ratio
        G20 = DEC2HEX(ROUNDUP(ROUNDUP(D20*C20/F20, 0)/128, 0)*128/8)
        TOP_OD = DEC2HEX((HEX2DEC(G20) * E20))
        reg_dict['TOP_OD'] = TOP_OD

        reg_ptc_00_start_address0 = self.start_addr
        reg_ptc_01_start_address0 = reg_ptc_00_start_address0

        reg_dict['reg_ptc_00_start_address0'] = reg_ptc_00_start_address0

        self._reg_ptc_00_start_address0.value = reg_ptc_00_start_address0
        self._reg_ptc_00_start_address1.value = reg_ptc_01_start_address0

        self.set_memory_range(self.start_addr, None)

    @property
    def registers(self):
        return [self._reg_ptc_00_start_address0, self._reg_ptc_00_start_address1]
