from mem_common import HEX2DEC, RegType, DEC2HEX, ROUNDUP, DDROp
from mem_reg import MemReg
from mem_agents.mem_agent import MemAgent

class MemAgent_KME_8(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self, mem_size, bandwidth):
        super().__init__('KME_8', mem_size, bandwidth, DDROp.W)

        self._reg_kme_08_start_address0 = MemReg('reg_kme_08_start_address0', 'reg_kme_08_start_address0', RegType.START)
        self._reg_kme_08_start_address1 = MemReg('reg_kme_08_start_address1', 'reg_kme_08_start_address1', RegType.START)
        self._reg_kme_08_line_offset_addr = MemReg('reg_kme_08_line_offset_addr', 'reg_kme_08_line_offset_addr', RegType.OTHER)
        self._reg_kme_08_mode = MemReg('reg_kme_08_mode', 'reg_kme_08_mode', RegType.OTHER)
        self._reg_kme_08_mode.value = 1

    def get_regs(self, reg_dict):
        C11 = 8   #data_width
        D11 = 1920  #H
        E11 = 1080  #V
        F11 = 1  # CPR ratio
        E8 = 540 # V
        D8 = 960 # H
        C8 = 8 # Data width
        F8 = 1 # CPR ratio
        KME_08_LineOffset = DEC2HEX(ROUNDUP(ROUNDUP(D11*C11/F11, 0)/128, 0)*128/8)
        KME_08_IP_LOGO = DEC2HEX((HEX2DEC(KME_08_LineOffset) * E11))    

        KME_00_LineOffset = DEC2HEX(ROUNDUP(ROUNDUP(D8*C8/F8, 0)/128, 0)*128/8)

        KME_00_IPME = DEC2HEX(HEX2DEC(KME_00_LineOffset) * E8)

        assert 'reg_kme_00_start_address7' in reg_dict
        reg_kme_00_start_address7 = reg_dict['reg_kme_00_start_address7']        

        reg_kme_08_start_address0 = DEC2HEX(HEX2DEC(reg_kme_00_start_address7)+HEX2DEC(KME_00_IPME))
        reg_kme_08_start_address1 = reg_kme_08_start_address0
        reg_kme_08_line_offset_addr = KME_08_LineOffset
        reg_kme_08_mode = 1

        self.start_addr = reg_kme_08_start_address0

        self._reg_kme_08_start_address0.value = reg_kme_08_start_address0
        self._reg_kme_08_start_address1.value = reg_kme_08_start_address1
        self._reg_kme_08_line_offset_addr.value = reg_kme_08_line_offset_addr
        self._reg_kme_08_mode.value = reg_kme_08_mode

        reg_dict['reg_kme_08_start_address1'] = reg_kme_08_start_address1
        reg_dict['KME_08_IP_LOGO'] = KME_08_IP_LOGO

        return  [self._reg_kme_08_start_address0,
                 self._reg_kme_08_start_address1,
                 self._reg_kme_08_line_offset_addr,
                 self._reg_kme_08_mode]
