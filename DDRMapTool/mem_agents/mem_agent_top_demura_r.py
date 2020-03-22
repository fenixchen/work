from mem_common import HEX2DEC, RegType, DEC2HEX, ROUNDUP, DDROp
from mem_reg import MemReg
from mem_agents.mem_agent import MemAgent

class MemAgent_TOP_DEMURA_R(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self, mem_size, bandwidth):
        super().__init__('TOP_DEMURA_R', mem_size, bandwidth, DDROp.W)

        self._reg_ptc_04_start_address0 = MemReg('reg_ptc_04_start_address0', 'reg_ptc_04_start_address0', RegType.START)

    def get_regs(self, reg_dict):

        #TOP_DEMURA  V*ROUNDUP(ROUNDUP(H*data_width/CRP_ration,0)/128,0)*128/8
        C22 = 90   #data_width
        D22 = 961  #H 
        E22 = 541  #V
        F22 = 1  # CPR ratio
        C21 = 8   #data_width
        D21 = 3840  #H 
        E21 = 2160  #V
        F21 = 4  # CPR ratio
        G21 = DEC2HEX(ROUNDUP(ROUNDUP(D21*C21/F21, 0)/128, 0)*128/8)
        G22 = DEC2HEX(ROUNDUP(ROUNDUP(D22*C22/F22, 0)/128, 0)*128/8)
        #TOP_DEMURA = DEC2HEX((HEX2DEC(G21) * E21))
        TOP_DEMURA = DEC2HEX((HEX2DEC(G22) * E22))

        reg_dict['TOP_DEMURA'] = TOP_DEMURA
        reg_ptc_00_start_address0 = reg_dict['reg_ptc_00_start_address0']
        TOP_OD = reg_dict['TOP_OD']

        reg_ptc_02_start_address0 = DEC2HEX(HEX2DEC(reg_ptc_00_start_address0)+HEX2DEC(TOP_OD))
        
        reg_ptc_04_start_address0 = DEC2HEX(HEX2DEC(reg_ptc_00_start_address0)+HEX2DEC(TOP_OD))

        self._reg_ptc_04_start_address0.value = reg_ptc_04_start_address0
        reg_dict['reg_ptc_04_start_address0'] = reg_ptc_04_start_address0

        return  [self._reg_ptc_04_start_address0]
