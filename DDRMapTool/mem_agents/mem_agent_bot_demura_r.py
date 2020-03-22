from mem_common import HEX2DEC, RegType, DEC2HEX, ROUNDUP, DDROp
from mem_reg import MemReg
from mem_agents.mem_agent import MemAgent

class MemAgent_BOT_DEMURA_R(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self, mem_size, bandwidth):
        super().__init__('BOT_DEMURA_R', mem_size, bandwidth, DDROp.W)

        self._reg_ptc_05_start_address0 = MemReg('reg_ptc_05_start_address0', 'reg_ptc_05_start_address0', RegType.START)

    def get_regs(self, reg_dict):

        #BOT_DEMURA  V*ROUNDUP(ROUNDUP(H*data_width/CRP_ration,0)/128,0)*128/8
        C23 = 30   #data_width
        D23 = 481  #H 
        E23 = 271  #V
        F23 = 1  # CPR ratio
        G23 = DEC2HEX(ROUNDUP(ROUNDUP(D23*C23/F23, 0)/128, 0)*128/8)
        BOT_DEMURA = DEC2HEX((HEX2DEC(G23) * E23))

        reg_kod_wdma_00_start_address3 = reg_dict['reg_kod_wdma_00_start_address3']
        TOP_OD = reg_dict['TOP_OD']

        reg_ptc_05_start_address0 = DEC2HEX(HEX2DEC(reg_kod_wdma_00_start_address3)+HEX2DEC(TOP_OD))    

        self._reg_ptc_05_start_address0.value = reg_ptc_05_start_address0

        return  [self._reg_ptc_05_start_address0]
