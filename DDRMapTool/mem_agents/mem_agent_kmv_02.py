from mem_common import HEX2DEC, RegType, DEC2HEX, ROUNDUP, DDROp
from mem_reg import MemReg
from mem_agents.mem_agent import MemAgent

class MemAgent_KMV_02(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self, mem_size, bandwidth):
        super().__init__('KMV_02', mem_size, bandwidth, DDROp.W)

        self._reg_mv02_start_address0 = MemReg('reg_mv02_start_address0', 'reg_mv02_start_address0', RegType.START)
        self._reg_mv02_end_address0 = MemReg('reg_mv02_end_address0', 'reg_mv02_end_address0', RegType.END)        
        self._reg_mv02_line_offset_addr = MemReg('reg_mv02_line_offset_addr', 'reg_mv02_line_offset_addr', RegType.OTHER)
        self._reg_mv02_mode = MemReg('reg_mv02_mode', 'reg_mv02_mode', RegType.OTHER)

    def get_regs(self, reg_dict):

        #KMV_02  270*ROUNDUP(ROUNDUP(480*data_width/CRP_ration,0)/128,0)*128/8
        C16 = 40   #data_width
        D16 = 480  #H 
        E16 = 270  #V
        F16 = 1  # CPR ratio
        ROW_NUM = 270
        KMV_02_Line_Offset = DEC2HEX(ROUNDUP(ROUNDUP(D16*C16/F16, 0)/128, 0)*128/8)
        KMV_02_MV = DEC2HEX((HEX2DEC(KMV_02_Line_Offset) * E16))
        reg_dict['KMV_02_MV'] = KMV_02_MV

        reg_mv01_start_address0 = reg_dict['KMV_01_start_addr']
        KMV_00_MV = reg_dict['KMV_00_MV']

        reg_mv02_start_address0 = DEC2HEX(HEX2DEC(reg_mv01_start_address0)+HEX2DEC(KMV_00_MV))
        reg_dict['reg_mv02_start_address0'] = reg_mv02_start_address0
        self._start_addr = reg_mv02_start_address0
        
        reg_mv02_end_address0 = DEC2HEX(HEX2DEC(reg_mv02_start_address0)+HEX2DEC(KMV_02_Line_Offset)*ROW_NUM)
        reg_mv02_line_offset_addr = KMV_02_Line_Offset
        reg_mv02_lr_offset_addr = DEC2HEX(HEX2DEC(KMV_02_MV)/2)

        self._reg_mv02_start_address0.value = reg_mv02_start_address0
        self._reg_mv02_end_address0.value = reg_mv02_end_address0
        self._reg_mv02_line_offset_addr.value = reg_mv02_line_offset_addr
        self._reg_mv02_mode.value = 1
                
        return  [self._reg_mv02_start_address0,
                 self._reg_mv02_end_address0,
                 self._reg_mv02_line_offset_addr,
                 self._reg_mv02_mode]
