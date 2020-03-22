from mem_common import HEX2DEC, RegType, DEC2HEX, ROUNDUP, DDROp
from mem_reg import MemReg
from mem_agents.mem_agent import MemAgent

class MemAgent_KME_10(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self, mem_size, bandwidth):
        super().__init__('KME_10', mem_size, bandwidth, DDROp.W)

        self._reg_kme_10_start_address0 = MemReg('reg_kme_10_start_address0', 'reg_kme_10_start_address0', RegType.START)
        self._reg_kme_10_start_address1 = MemReg('reg_kme_10_start_address1', 'reg_kme_10_start_address1', RegType.START)
        self._reg_kme_10_line_offset_addr = MemReg('reg_kme_10_line_offset_addr', 'reg_kme_10_line_offset_addr', RegType.OTHER)
        self._reg_kme_10_mode = MemReg('reg_kme_10_mode', 'reg_kme_10_mode', RegType.OTHER)
        self._reg_kme_10_mode.value = 1

    def get_regs(self, reg_dict):
        #KME_10  1080*ROUNDUP(ROUNDUP(1920*data_width/CRP_ration,0)/128,0)*128/8
        C12 = 4   #data_width
        D12 = 1920  #H 
        E12 = 1080  #V
        F12 = 1  # CPR ratio
        KME_10_LineOffset = DEC2HEX(ROUNDUP(ROUNDUP(D12*C12/F12, 0)/128, 0)*128/8)
        KME_10_LOGO_MASK = DEC2HEX((HEX2DEC(KME_10_LineOffset) * E12))
        reg_dict['KME_10_LOGO_MASK'] = KME_10_LOGO_MASK

        reg_kme_08_start_address1 = reg_dict['reg_kme_08_start_address1']
        KME_08_IP_LOGO = reg_dict['KME_08_IP_LOGO']

        reg_kme_10_start_address0 = DEC2HEX(HEX2DEC(reg_kme_08_start_address1)+HEX2DEC(KME_08_IP_LOGO))
        self._start_addr = reg_kme_10_start_address0
        
        reg_kme_10_start_address1 = reg_kme_10_start_address0
        reg_dict['reg_kme_10_start_address1'] = reg_kme_10_start_address1

        reg_kme_10_line_offset_addr = KME_10_LineOffset
        reg_kme_10_mode = 1

        self._reg_kme_10_start_address0.value = reg_kme_10_start_address0
        self._reg_kme_10_start_address1.value = reg_kme_10_start_address1
        self._reg_kme_10_line_offset_addr.value = reg_kme_10_line_offset_addr
        self._reg_kme_10_mode.value = reg_kme_10_mode

        return  [self._reg_kme_10_start_address0,
                 self._reg_kme_10_start_address1,
                 self._reg_kme_10_line_offset_addr,
                 self._reg_kme_10_mode]
