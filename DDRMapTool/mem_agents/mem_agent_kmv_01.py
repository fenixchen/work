from mem_common import HEX2DEC, RegType, DEC2HEX, ROUNDUP, DDROp
from mem_reg import MemReg
from mem_agents.mem_agent import MemAgent

class MemAgent_KMV_01(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self, mem_size, bandwidth):
        super().__init__('KMV_01', mem_size, bandwidth, DDROp.W)

        self._reg_mv01_start_address0 = MemReg('reg_mv01_start_address0', 'reg_mv01_start_address0', RegType.START)
        self._reg_mv01_end_address0 = MemReg('reg_mv01_end_address0', 'reg_mv01_end_address0', RegType.END)        
        self._reg_mv01_line_offset_addr = MemReg('reg_mv01_line_offset_addr', 'reg_mv01_line_offset_addr', RegType.OTHER)
        self._reg_mv01_mode = MemReg('reg_mv01_mode', 'reg_mv01_mode', RegType.OTHER)

    def get_regs(self, reg_dict):

        #Kmv01  270*ROUNDUP(ROUNDUP(480*data_width/CRP_ration,0)/128,0)*128/8
        C15 = 21   #data_width
        D15 = 480  #H 
        E15 = 270  #V
        F15 = 1  # CPR ratio
        ROW_NUM2 = 270
        Kmv01_Line_Offset = DEC2HEX(ROUNDUP(ROUNDUP(D15*C15/F15, 0)/128, 0)*128/8)
        KMV_00_MV = DEC2HEX((HEX2DEC(Kmv01_Line_Offset) * E15))

        reg_dict['KMV_00_MV'] = KMV_00_MV

        reg_mv01_start_address0 = self.start_addr
        reg_mv01_end_address0 = DEC2HEX(HEX2DEC(reg_mv01_start_address0)+HEX2DEC(Kmv01_Line_Offset) * ROW_NUM2)
        reg_mv01_line_offset_addr = Kmv01_Line_Offset
        reg_mv01_lr_offset_addr = DEC2HEX(HEX2DEC(KMV_00_MV)/2)

        self._reg_mv01_start_address0.value = reg_mv01_start_address0
        self._reg_mv01_end_address0.value = reg_mv01_end_address0
        self._reg_mv01_line_offset_addr.value = reg_mv01_line_offset_addr
        self._reg_mv01_mode.value = 1
        
        
        return  [self._reg_mv01_start_address0,
                 self._reg_mv01_end_address0,
                 self._reg_mv01_line_offset_addr,
                 self._reg_mv01_mode]
