from mem_common import HEX2DEC, RegType, DEC2HEX, ROUNDUP, DDROp
from mem_reg import MemReg
from mem_agents.mem_agent import MemAgent

class MemAgent_KME_12(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self, mem_size, bandwidth):
        super().__init__('KME_12', mem_size, bandwidth, DDROp.W)

        self._reg_kme_12_start_address0 = MemReg('reg_kme_12_start_address0', 'reg_kme_12_start_address0', RegType.START)
        self._reg_kme_12_end_address0 = MemReg('reg_kme_12_end_address0', 'reg_kme_12_end_address0', RegType.END)
        self._reg_kme_12_start_address1 = MemReg('reg_kme_12_start_address1', 'reg_kme_12_start_address1', RegType.START)
        self._reg_kme_12_end_address1 = MemReg('reg_kme_12_end_address1', 'reg_kme_12_end_address1', RegType.END)
        self._reg_kme_12_line_offset_addr = MemReg('reg_kme_12_line_offset_addr', 'reg_kme_12_line_offset_addr', RegType.OTHER)
        self._reg_kme_12_mode = MemReg('reg_kme_12_mode', 'reg_kme_12_mode', RegType.OTHER)
        self._reg_kme_12_mode.value = 1

    def get_regs(self, reg_dict):
        #KME_12  1080*ROUNDUP(ROUNDUP(1920*data_width/CRP_ration,0)/128,0)*128/8
        C13 = 1   #data_width
        D13 = 1920  #H 
        E13 = 1080  #V
        F13 = 1  # CPR ratio
        KME_12_LineOffset = DEC2HEX(ROUNDUP(ROUNDUP(D13*C13/F13, 0)/128, 0)*128/8)
        KME_12_Pixel_LOGO = DEC2HEX((HEX2DEC(KME_12_LineOffset) * E13))
        reg_dict['KME_12_Pixel_LOGO'] = KME_12_Pixel_LOGO
        
        LOGO_VACT = 1080

        KME_10_LOGO_MASK = reg_dict['KME_10_LOGO_MASK']
        reg_kme_10_start_address1 = reg_dict['reg_kme_10_start_address1']

        reg_kme_12_start_address0 = DEC2HEX(HEX2DEC(reg_kme_10_start_address1)+HEX2DEC(KME_10_LOGO_MASK))
        self._start_addr = reg_kme_12_start_address0

        reg_kme_12_start_address1 = reg_kme_12_start_address0
        reg_dict['reg_kme_12_start_address1'] = reg_kme_12_start_address1

        reg_kme_12_end_address0 = DEC2HEX(HEX2DEC(reg_kme_12_start_address0)+HEX2DEC(KME_12_LineOffset)*LOGO_VACT)
        reg_kme_12_end_address1 = reg_kme_12_end_address0
        reg_kme_12_line_offset_addr = KME_12_LineOffset
        reg_kme_12_mode = 1

        self._reg_kme_12_start_address0.value = reg_kme_12_start_address0
        self._reg_kme_12_end_address0.value = reg_kme_12_end_address0
        self._reg_kme_12_start_address1.value = reg_kme_12_start_address1
        self._reg_kme_12_end_address1.value = reg_kme_12_end_address1
        self._reg_kme_12_line_offset_addr.value = reg_kme_12_line_offset_addr
        self._reg_kme_12_mode.value = reg_kme_12_mode
        

        return  [self._reg_kme_12_start_address0,
                 self._reg_kme_12_start_address1,
                 self._reg_kme_12_end_address0,                 
                 self._reg_kme_12_end_address1,
                 self._reg_kme_12_line_offset_addr,
                 self._reg_kme_12_mode]
