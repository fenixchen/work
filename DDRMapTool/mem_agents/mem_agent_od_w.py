from mem_common import HEX2DEC, RegType, DEC2HEX, ROUNDUP, DDROp
from mem_reg import MemReg
from mem_agents.mem_agent import MemAgent

class MemAgent_OD_W(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self, mem_size, bandwidth):
        super().__init__('OD_W', mem_size, bandwidth, DDROp.W)

        self._reg_ptc_00_start_address0 = MemReg('reg_ptc_00_start_address0', 'reg_ptc_00_start_address0', RegType.START)
        self._reg_ptc_00_start_address1 = MemReg('reg_ptc_00_start_address1', 'reg_ptc_00_start_address1', RegType.START)

    def get_regs(self, reg_dict):

        #TOP_OD  V*ROUNDUP(ROUNDUP(H*data_width/CRP_ration,0)/128,0)*128/8
        C20 = 24   #data_width
        D20 = 3840  #H 
        E20 = 4320  #V
        F20 = 11.66  # CPR ratio
        G20 = DEC2HEX(ROUNDUP(ROUNDUP(D20*C20/F20, 0)/128, 0)*128/8)
        TOP_OD = DEC2HEX((HEX2DEC(G20) * E20))
        reg_dict['TOP_OD'] = TOP_OD
        
        reg_ptc_00_start_address0 = self.start_addr
        reg_ptc_01_start_address0 = reg_ptc_00_start_address0
        
        reg_dict['reg_ptc_00_start_address0'] = reg_ptc_00_start_address0

        self._reg_ptc_00_start_address0.value = reg_ptc_00_start_address0
        self._reg_ptc_00_start_address1.value = reg_ptc_01_start_address0

        return  [self._reg_ptc_00_start_address0, self._reg_ptc_00_start_address1]
