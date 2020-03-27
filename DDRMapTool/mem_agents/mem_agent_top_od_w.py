from mem_common import HEX2DEC, RegType, DEC2HEX, ROUNDUP, DDROp
from mem_reg import MemReg
from mem_agents.mem_agent import MemAgent
from mem_global_var import *


class MemAgent_TOP_OD_W(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self):
        super().__init__('TOP_OD_W', 'TOP_OD_W_L', DDROp.W)

    def calc_memory(self):
        TOP_OD_W_frame_rate = TOP_OD_framerate
        TOP_OD_W_bits = TOP_OD_bits
        TOP_OD_W_H_res = TOP_OD_Hact / 2
        TOP_OD_W_V_res = TOP_OD_Vtotal
        TOP_OD_W_VDE_res = TOP_OD_Vact
        TOP_OD_W_CPR_ratio = TOP_OD_CPR_ratio
        TOP_OD_W_Bandwidth = TOP_OD_W_frame_rate*TOP_OD_W_bits*TOP_OD_W_H_res*TOP_OD_W_V_res/TOP_OD_W_CPR_ratio/8/1000/1000
        TOP_OD_W_DDR_size = TOP_OD_W_bits*TOP_OD_W_H_res*TOP_OD_W_VDE_res/TOP_OD_W_CPR_ratio/8/1024/1024
        return TOP_OD_W_DDR_size, TOP_OD_W_Bandwidth
