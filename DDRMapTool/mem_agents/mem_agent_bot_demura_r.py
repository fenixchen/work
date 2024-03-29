from mem_common import HEX2DEC, RegType, DEC2HEX, ROUNDUP, DDROp
from mem_reg import MemReg
from mem_agents.mem_agent import MemAgent
from mem_global_var import GV


class MemAgent_BOT_DEMURA_R(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self):
        super().__init__('BOT_DEMURA_R', 'BOT_DEMURA_R', DDROp.W)

        self._reg_ptc_05_start_address0 = MemReg('reg_ptc_05_start_address0', 'reg_ptc_05_start_address0', RegType.START)

    def calc_memory(self):
        BOT_DEMURA_R_frame_rate = GV.BOT_Demura_framerate
        BOT_DEMURA_R_bits = GV.BOT_Demura_bits
        BOT_DEMURA_R_H_res = GV.BOT_Demura_Hact
        BOT_DEMURA_R_V_res = GV.BOT_Demura_Vtotal
        BOT_DEMURA_R_VDE_res = GV.BOT_Demura_Vact
        BOT_DEMURA_R_CPR_ratio = GV.BOT_Demura_CPR_ratio
        BOT_DEMURA_R_Bandwidth = BOT_DEMURA_R_frame_rate*BOT_DEMURA_R_bits*BOT_DEMURA_R_H_res*BOT_DEMURA_R_V_res/BOT_DEMURA_R_CPR_ratio/8/1000/1000
        BOT_DEMURA_R_DDR_size = 0
        return BOT_DEMURA_R_DDR_size, BOT_DEMURA_R_Bandwidth

    def allocate_memory(self, reg_dict):

        # BOT_DEMURA  V*ROUNDUP(ROUNDUP(H*data_width/CRP_ration,0)/128,0)*128/8
        C23 = 30  # data_width
        D23 = 481  # H
        E23 = 271  # V
        F23 = 1  # CPR ratio
        G23 = DEC2HEX(ROUNDUP(ROUNDUP(D23*C23/F23, 0)/128, 0)*128/8)
        BOT_DEMURA = DEC2HEX((HEX2DEC(G23) * E23))

        reg_ptc_05_start_address0 = self.start_addr

        self._reg_ptc_05_start_address0.value = reg_ptc_05_start_address0

        self.set_memory_range(reg_ptc_05_start_address0, reg_ptc_05_start_address0 + BOT_DEMURA)

    @property
    def registers(self):
        return [self._reg_ptc_05_start_address0]
