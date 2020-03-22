from mem_common import HEX2DEC, RegType, DEC2HEX, ROUNDUP, DDROp
from mem_reg import MemReg
from mem_agents.mem_agent import MemAgent

class MemAgent_KME_14(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self, mem_size, bandwidth):
        super().__init__('KME_14', mem_size, bandwidth, DDROp.W)

        self._reg_kme_14_start_address0 = MemReg('reg_kme_14_start_address0', 'reg_kme_14_start_address0', RegType.START)
        self._reg_kme_14_start_address1 = MemReg('reg_kme_14_start_address1', 'reg_kme_14_start_address1', RegType.START)        
        self._reg_kme_14_line_offset_addr = MemReg('reg_kme_14_line_offset_addr', 'reg_kme_14_line_offset_addr', RegType.OTHER)
        self._reg_kme_14_mode = MemReg('reg_kme_14_mode', 'reg_kme_14_mode', RegType.OTHER)
        self._reg_kme_14_mode.value = 1

    def get_regs(self, reg_dict):

        #KME_14  270*ROUNDUP(ROUNDUP(480*data_width/CRP_ration,0)/128,0)*128/8
        C14 = 4   #data_width
        D14 = 480   #H
        E14 = 270   #V
        F14 = 1  # CPR ratio
        KME_14_LineOffset = DEC2HEX(ROUNDUP(ROUNDUP(D14*C14/F14, 0)/128, 0)*128/8)
        KME_14_HOG_history = DEC2HEX((HEX2DEC(KME_14_LineOffset) * E14))

        reg_kme_12_start_address1 = reg_dict['reg_kme_12_start_address1']
        KME_12_Pixel_LOGO = reg_dict['KME_12_Pixel_LOGO']

        reg_kme_14_start_address0 = DEC2HEX(HEX2DEC(reg_kme_12_start_address1)+HEX2DEC(KME_12_Pixel_LOGO))
        self._start_addr = reg_kme_14_start_address0
        
        reg_kme_14_start_address1 = reg_kme_14_start_address0
        reg_kme_14_line_offset_addr = KME_14_LineOffset
        reg_kme_14_mode = 1

        self._reg_kme_14_start_address0.value = reg_kme_14_start_address0
        self._reg_kme_14_start_address1.value = reg_kme_14_start_address1
        self._reg_kme_14_line_offset_addr.value = reg_kme_14_line_offset_addr
        self._reg_kme_14_mode.value = reg_kme_14_mode
        
        
        return  [self._reg_kme_14_start_address0,
                 self._reg_kme_14_start_address1,
                 self._reg_kme_14_line_offset_addr,
                 self._reg_kme_14_mode]
