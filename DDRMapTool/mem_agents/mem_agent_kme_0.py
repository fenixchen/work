from mem_common import HEX2DEC, RegType, DEC2HEX, ROUNDUP, DDROp
from mem_reg import MemReg

from mem_agents.mem_agent import MemAgent

class MemAgent_KME_0(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self, mem_size, bandwidth):
        super().__init__('KME_0', mem_size, bandwidth, DDROp.W)
        # from  reg_kme_00_start_address0 to reg_kme_00_start_address7
        self._reg_kme_00_start_address = [None] * 8
        for i in range(8):
            name = 'reg_kme_00_start_address%d' % i
            addr = name # same here, find in global register map later
            self._reg_kme_00_start_address[i] = MemReg(name, addr, RegType.START)

        self._reg_kme_00_end_address = [None] * 8
        for i in range(8):
            name = 'reg_kme_00_end_address%d' % i
            addr = name # same here, find in global register map later
            self._reg_kme_00_end_address[i] = MemReg(name, addr, RegType.END)

        self._reg_kme_00_line_offset_addr = MemReg('reg_kme_00_line_offset_addr', 'reg_kme_00_line_offset_addr', RegType.OTHER)

        self._reg_kme_00_mode = MemReg('reg_kme_00_mode', 'reg_kme_00_mode', RegType.OTHER)
        self._reg_kme_00_mode.value = 1

    def get_regs(self, reg_dict):

        B3 = 3856 #H_act
        C3 = 4320 #V_act
        REAL_HACT = 3840
        REAL_VACT = 4320
        LOGO_VACT = 1080
        ME_VACT = 540
        ROW_NUM = 270
        ROW_NUM2 = 270
        KMC00_start_address = self._start_addr
        KMC08_start_address = 0
        KME_start_address = 0
        KMV_star_address = 0
        Tcon_PQ_address = 0


        #KME_00  540*ROUNDUP(ROUNDUP(960*data_width/CRP_ration,0)/128,0)*128/8
        C8 = 8   #data_width
        D8 = 960   #H
        E8 = 540   #V
        F8 = 1  # CPR ratio
        KME_00_LineOffset = DEC2HEX(ROUNDUP(ROUNDUP(D8*C8 /F8, 0)/128, 0)*128/8)
        KME_00_IPME = DEC2HEX((HEX2DEC(KME_00_LineOffset) * E8))

        reg_kme_00_start_address0 = KME_start_address
        reg_kme_00_start_address1 = DEC2HEX(HEX2DEC(reg_kme_00_start_address0) + HEX2DEC(KME_00_IPME))
        reg_kme_00_start_address2 = DEC2HEX(HEX2DEC(reg_kme_00_start_address1) + HEX2DEC(KME_00_IPME))
        reg_kme_00_start_address3 = DEC2HEX(HEX2DEC(reg_kme_00_start_address2) + HEX2DEC(KME_00_IPME))
        reg_kme_00_start_address4 = DEC2HEX(HEX2DEC(reg_kme_00_start_address3) + HEX2DEC(KME_00_IPME))
        reg_kme_00_start_address5 = DEC2HEX(HEX2DEC(reg_kme_00_start_address4) + HEX2DEC(KME_00_IPME))
        reg_kme_00_start_address6 = reg_kme_00_start_address5
        reg_kme_00_start_address7 = reg_kme_00_start_address6
        reg_kme_00_end_address0 = DEC2HEX(HEX2DEC(reg_kme_00_start_address0)+HEX2DEC(KME_00_LineOffset)*ME_VACT)
        reg_kme_00_end_address1 = DEC2HEX(HEX2DEC(reg_kme_00_start_address1)+HEX2DEC(KME_00_LineOffset)*ME_VACT)
        reg_kme_00_end_address2 = DEC2HEX(HEX2DEC(reg_kme_00_start_address2)+HEX2DEC(KME_00_LineOffset)*ME_VACT)
        reg_kme_00_end_address3 = DEC2HEX(HEX2DEC(reg_kme_00_start_address3)+HEX2DEC(KME_00_LineOffset)*ME_VACT)
        reg_kme_00_end_address4 = DEC2HEX(HEX2DEC(reg_kme_00_start_address4)+HEX2DEC(KME_00_LineOffset)*ME_VACT)
        reg_kme_00_end_address5 = DEC2HEX(HEX2DEC(reg_kme_00_start_address5)+HEX2DEC(KME_00_LineOffset)*ME_VACT)
        reg_kme_00_end_address6 = DEC2HEX(HEX2DEC(reg_kme_00_start_address6)+HEX2DEC(KME_00_LineOffset)*ME_VACT)
        reg_kme_00_end_address7 = DEC2HEX(HEX2DEC(reg_kme_00_start_address7)+HEX2DEC(KME_00_LineOffset)*ME_VACT)
        reg_kme_00_lr_offset_addr = DEC2HEX(HEX2DEC(KME_00_IPME)/2)
        reg_kme_00_line_offset_addr = KME_00_LineOffset
        reg_kme_00_mode = 1

        self._reg_kme_00_start_address[0].value = reg_kme_00_start_address0
        self._reg_kme_00_start_address[1].value = reg_kme_00_start_address1
        self._reg_kme_00_start_address[2].value = reg_kme_00_start_address2
        self._reg_kme_00_start_address[3].value = reg_kme_00_start_address3
        self._reg_kme_00_start_address[4].value = reg_kme_00_start_address4
        self._reg_kme_00_start_address[5].value = reg_kme_00_start_address5
        self._reg_kme_00_start_address[6].value = reg_kme_00_start_address6
        self._reg_kme_00_start_address[7].value = reg_kme_00_start_address7

        self._reg_kme_00_end_address[0].value = reg_kme_00_end_address0
        self._reg_kme_00_end_address[1].value = reg_kme_00_end_address1
        self._reg_kme_00_end_address[2].value = reg_kme_00_end_address2
        self._reg_kme_00_end_address[3].value = reg_kme_00_end_address3
        self._reg_kme_00_end_address[4].value = reg_kme_00_end_address4
        self._reg_kme_00_end_address[5].value = reg_kme_00_end_address5
        self._reg_kme_00_end_address[6].value = reg_kme_00_end_address6
        self._reg_kme_00_end_address[7].value = reg_kme_00_end_address7

        regs = self._reg_kme_00_start_address + self._reg_kme_00_end_address

        self._reg_kme_00_line_offset_addr.value = reg_kme_00_line_offset_addr
        regs.append(self._reg_kme_00_line_offset_addr)

        self._reg_kme_00_mode.value = reg_kme_00_mode
        regs.append(self._reg_kme_00_mode)

        # save address for KME_08
        reg_dict['reg_kme_00_start_address7'] = reg_kme_00_start_address7

        return  regs
