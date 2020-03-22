from mem_common import HEX2DEC, RegType, DEC2HEX, ROUNDUP, DDROp
from mem_reg import MemReg
from mem_agents.mem_agent import MemAgent

class MemAgent_KMV_05(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self, mem_size, bandwidth):
        super().__init__('KMV_05', mem_size, bandwidth, DDROp.W)

        self._reg_mv05_start_address0 = MemReg('reg_mv05_start_address0', 'reg_mv05_start_address0', RegType.START)
        self._reg_mv05_start_address1 = MemReg('reg_mv05_start_address1', 'reg_mv05_start_address1', RegType.START)
        self._reg_mv05_end_address0 = MemReg('reg_mv05_end_address0', 'reg_mv05_end_address0', RegType.END)        
        self._reg_mv05_end_address1 = MemReg('reg_mv05_end_address1', 'reg_mv05_end_address1', RegType.END)            
        self._reg_mv05_line_offset_addr = MemReg('reg_mv05_line_offset_addr', 'reg_mv05_line_offset_addr', RegType.OTHER)
        self._reg_mv05_mode = MemReg('reg_mv05_mode', 'reg_mv05_mode', RegType.OTHER)

    def get_regs(self, reg_dict):

        #KMV_05  270*ROUNDUP(ROUNDUP(480*data_width/CRP_ration,0)/128,0)*128/8
        C18 = 64   #data_width
        D18 = 480  #H 
        E18 = 270  #V
        F18 = 1  # CPR ratio
        ROW_NUM = 270
        KMV_05_Line_Offset = DEC2HEX(ROUNDUP(ROUNDUP(D18*C18/F18, 0)/128, 0)*128/8)
        KMV_05_MV = DEC2HEX((HEX2DEC(KMV_05_Line_Offset) * E18))

        reg_mv04_start_address2 = reg_dict['reg_mv04_start_address2']
        KMV_04_MV = reg_dict['KMV_04_MV']
        reg_mv05_start_address0 = DEC2HEX(HEX2DEC(reg_mv04_start_address2)+HEX2DEC(KMV_04_MV))
        self.start_addr = reg_mv05_start_address0

        reg_mv05_start_address1 = DEC2HEX(HEX2DEC(reg_mv05_start_address0)+HEX2DEC(KMV_05_MV))
        reg_mv05_end_address0 = DEC2HEX(HEX2DEC(reg_mv05_start_address0)+HEX2DEC(KMV_05_Line_Offset)*ROW_NUM)
        reg_mv05_end_address1 = DEC2HEX(HEX2DEC(reg_mv05_start_address1)+HEX2DEC(KMV_05_Line_Offset)*ROW_NUM)
        reg_mv05_line_offset_addr = KMV_05_Line_Offset
        reg_mv05_lr_offset_addr = DEC2HEX(HEX2DEC(KMV_05_MV)/2)

        self._reg_mv05_start_address0.value = reg_mv05_start_address0
        self._reg_mv05_start_address1.value = reg_mv05_start_address1        
        self._reg_mv05_end_address0.value = reg_mv05_end_address0
        self._reg_mv05_end_address1.value = reg_mv05_end_address1        
        self._reg_mv05_line_offset_addr.value = reg_mv05_line_offset_addr
        self._reg_mv05_mode.value = 1
        
        
        return  [self._reg_mv05_start_address0,
                 self._reg_mv05_start_address1,                 
                 self._reg_mv05_end_address0,
                 self._reg_mv05_end_address1,                 
                 self._reg_mv05_line_offset_addr,
                 self._reg_mv05_mode]
