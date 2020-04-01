from mem_common import HEX2DEC, RegType, DEC2HEX, ROUNDUP, DDROp
from mem_reg import MemReg
from mem_agents.mem_agent import MemAgent
from mem_global_var import GV


class MemAgent_TOP_DEMURA_R(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self):
        super().__init__('TOP_DEMURA_R', 'TOP_DEMURA_R', DDROp.W)
        self._reg_ptc_04_start_address0 = MemReg('reg_ptc_04_start_address0', 'reg_ptc_04_start_address0', RegType.START)

    def calc_memory(self):
        TOP_DEMURA_R_frame_rate = GV.TOP_Demura_framerate
        TOP_DEMURA_R_bits = GV.TOP_Demura_bits
        TOP_DEMURA_R_H_res = GV.TOP_Demura_Hact
        TOP_DEMURA_R_V_res = GV.TOP_Demura_Vtotal
        TOP_DEMURA_R_VDE_res = GV.TOP_Demura_Vact
        TOP_DEMURA_R_CPR_ratio = GV.TOP_Demura_CPR_ratio
        TOP_DEMURA_R_Bandwidth = TOP_DEMURA_R_frame_rate*TOP_DEMURA_R_bits*TOP_DEMURA_R_H_res*TOP_DEMURA_R_V_res/TOP_DEMURA_R_CPR_ratio/8/1000/1000
        TOP_DEMURA_R_DDR_size = 0
        return TOP_DEMURA_R_DDR_size, TOP_DEMURA_R_Bandwidth

    def allocate_memory(self, reg_dict):

        # TOP_DEMURA  V*ROUNDUP(ROUNDUP(H*data_width/CRP_ration,0)/128,0)*128/8
        C22 = 90  # data_width
        D22 = 961  # H
        E22 = 541  # V
        F22 = 1  # CPR ratio
        C21 = 8  # data_width
        D21 = 3840  # H
        E21 = 2160  # V
        F21 = 4  # CPR ratio
        G21 = DEC2HEX(ROUNDUP(ROUNDUP(D21*C21/F21, 0)/128, 0)*128/8)
        G22 = DEC2HEX(ROUNDUP(ROUNDUP(D22*C22/F22, 0)/128, 0)*128/8)
        #TOP_DEMURA = DEC2HEX((HEX2DEC(G21) * E21))
        TOP_DEMURA = DEC2HEX((HEX2DEC(G22) * E22))

        reg_dict['TOP_DEMURA'] = TOP_DEMURA

        reg_ptc_02_start_address0 = self.start_addr

        reg_ptc_04_start_address0 = self.start_addr

        self._reg_ptc_04_start_address0.value = reg_ptc_04_start_address0

        self.set_memory_range(reg_ptc_04_start_address0, reg_ptc_04_start_address0 + TOP_DEMURA)

    @property
    def registers(self):
        return [self._reg_ptc_04_start_address0]
