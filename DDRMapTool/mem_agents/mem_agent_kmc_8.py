from mem_common import HEX2DEC, RegType, DEC2HEX, ROUNDUP, DDROp
from mem_reg import MemReg
from mem_global_var import *
from mem_agents.mem_agent import MemAgent


class MemAgent_KMC_8(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self):
        super().__init__('KMC_8', 'IP_R_MC_HF_ENC_YC', DDROp.W)
        # from  reg_kmc_08_start_address0 to reg_kmc_08_start_address7
        self._reg_kmc_08_start_address = [None] * 8
        for i in range(8):
            name = 'reg_kmc_08_start_address%d' % i
            addr = name  # same here, find in global register map later
            self._reg_kmc_08_start_address[i] = MemReg(name, addr, RegType.START)

        self._reg_kmc_08_end_address = [None] * 8
        for i in range(8):
            name = 'reg_kmc_08_end_address%d' % i
            addr = name  # same here, find in global register map later
            self._reg_kmc_08_end_address[i] = MemReg(name, addr, RegType.END)

        self._reg_kmc_08_line_offset_addr = MemReg('reg_kmc_08_line_offset_addr', 'reg_kmc_08_line_offset_addr', RegType.OTHER)

        self._reg_kmc_08_mode = MemReg('reg_kmc_08_mode', 'reg_kmc_08_mode', RegType.OTHER)
        self._reg_kmc_08_mode.value = 1

    def calc_memory(self):
        KMC_0_frame_rate = GV.MC_H_in_framerate
        KMC_0_bits = GV.MC_H_bits
        KMC_0_H_res = GV.MC_H_Hact/2+GV.MC_H_Hoverlap
        KMC_0_V_res = GV.MC_H_Vtotal/2
        KMC_0_VDE_res = GV.MC_H_Vact/2
        KMC_0_CPR_ratio = GV.MC_H_CPR_ratio
        KMC_0_Bandwidth = KMC_0_frame_rate*KMC_0_bits*KMC_0_H_res*KMC_0_V_res/KMC_0_CPR_ratio/8/1000/1000
        KMC_0_DDR_size = KMC_0_bits*KMC_0_H_res*KMC_0_VDE_res/KMC_0_CPR_ratio/8/1024/1024*GV.MC_H_buff_num
        return KMC_0_DDR_size, KMC_0_Bandwidth

    def allocate_memory(self, reg_dict):

        B3 = 3856  # H_act
        C3 = 4320  # V_act
        REAL_HACT = 3840
        REAL_VACT = 4320
        LOGO_VACT = 1080
        ME_VACT = 540
        ROW_NUM = 270
        ROW_NUM2 = 270
        KMC00_start_address = 0
        KMC08_start_address = self.start_addr
        KME_start_address = 0
        KMV_star_address = 0
        Tcon_PQ_address = 0

        #kmc_08  (V_act/2+2)*ROUNDUP(ROUNDUP(H_act*data_width/CRP_ration,0)/128,0)*128/8
        C6 = 22  # data_width
        D6 = B3  # H
        E6 = C3/2+2  # V
        F6 = 2.2  # CPR ratio
        kmc_08_LineOffset_VD = DEC2HEX(ROUNDUP(ROUNDUP(D6 * C6 / F6, 0) / 128, 0)*128/8)
        kmc_08_MC_HF_VD_CPR = DEC2HEX((HEX2DEC(kmc_08_LineOffset_VD) * E6))

        reg_kmc_08_start_address0 = KMC08_start_address
        reg_kmc_08_start_address1 = DEC2HEX(HEX2DEC(reg_kmc_08_start_address0) + HEX2DEC(kmc_08_MC_HF_VD_CPR))
        reg_kmc_08_start_address2 = DEC2HEX(HEX2DEC(reg_kmc_08_start_address1) + HEX2DEC(kmc_08_MC_HF_VD_CPR))
        reg_kmc_08_start_address3 = DEC2HEX(HEX2DEC(reg_kmc_08_start_address2) + HEX2DEC(kmc_08_MC_HF_VD_CPR))
        reg_kmc_08_start_address4 = DEC2HEX(HEX2DEC(reg_kmc_08_start_address3) + HEX2DEC(kmc_08_MC_HF_VD_CPR))
        reg_kmc_08_start_address5 = reg_kmc_08_start_address4
        reg_kmc_08_start_address6 = reg_kmc_08_start_address5
        reg_kmc_08_start_address7 = reg_kmc_08_start_address6

        reg_kmc_08_end_address0 = DEC2HEX(HEX2DEC(reg_kmc_08_start_address0) + HEX2DEC(kmc_08_LineOffset_VD)*REAL_VACT/2)
        reg_kmc_08_end_address1 = DEC2HEX(HEX2DEC(reg_kmc_08_start_address1) + HEX2DEC(kmc_08_LineOffset_VD)*REAL_VACT/2)
        reg_kmc_08_end_address2 = DEC2HEX(HEX2DEC(reg_kmc_08_start_address2) + HEX2DEC(kmc_08_LineOffset_VD)*REAL_VACT/2)
        reg_kmc_08_end_address3 = DEC2HEX(HEX2DEC(reg_kmc_08_start_address3) + HEX2DEC(kmc_08_LineOffset_VD)*REAL_VACT/2)
        reg_kmc_08_end_address4 = DEC2HEX(HEX2DEC(reg_kmc_08_start_address4) + HEX2DEC(kmc_08_LineOffset_VD)*REAL_VACT/2)
        reg_kmc_08_end_address5 = DEC2HEX(HEX2DEC(reg_kmc_08_start_address5) + HEX2DEC(kmc_08_LineOffset_VD)*REAL_VACT/2)
        reg_kmc_08_end_address6 = DEC2HEX(HEX2DEC(reg_kmc_08_start_address6) + HEX2DEC(kmc_08_LineOffset_VD)*REAL_VACT/2)
        reg_kmc_08_end_address7 = DEC2HEX(HEX2DEC(reg_kmc_08_start_address7) + HEX2DEC(kmc_08_LineOffset_VD)*REAL_VACT/2)

        reg_kmc_08_line_offset_addr = kmc_08_LineOffset_VD
        reg_kmc_08_mode = 1

        self._reg_kmc_08_start_address[0].value = reg_kmc_08_start_address0
        self._reg_kmc_08_start_address[1].value = reg_kmc_08_start_address1
        self._reg_kmc_08_start_address[2].value = reg_kmc_08_start_address2
        self._reg_kmc_08_start_address[3].value = reg_kmc_08_start_address3
        self._reg_kmc_08_start_address[4].value = reg_kmc_08_start_address4
        self._reg_kmc_08_start_address[5].value = reg_kmc_08_start_address5
        self._reg_kmc_08_start_address[6].value = reg_kmc_08_start_address6
        self._reg_kmc_08_start_address[7].value = reg_kmc_08_start_address7

        self._reg_kmc_08_end_address[0].value = reg_kmc_08_end_address0
        self._reg_kmc_08_end_address[1].value = reg_kmc_08_end_address1
        self._reg_kmc_08_end_address[2].value = reg_kmc_08_end_address2
        self._reg_kmc_08_end_address[3].value = reg_kmc_08_end_address3
        self._reg_kmc_08_end_address[4].value = reg_kmc_08_end_address4
        self._reg_kmc_08_end_address[5].value = reg_kmc_08_end_address5
        self._reg_kmc_08_end_address[6].value = reg_kmc_08_end_address6
        self._reg_kmc_08_end_address[7].value = reg_kmc_08_end_address7

        self._reg_kmc_08_line_offset_addr.value = reg_kmc_08_line_offset_addr

        self._reg_kmc_08_mode.value = reg_kmc_08_mode

        # save address for KMC_09
        reg_dict['reg_kmc_08_start_address7'] = reg_kmc_08_start_address7
        reg_dict['kmc_08_MC_HF_VD_CPR'] = kmc_08_MC_HF_VD_CPR

        regs = self._reg_kmc_08_start_address + self._reg_kmc_08_end_address
        for reg in regs:
            reg.value += self.ddr_base_offset

        self.set_memory_range(self.start_addr, self.end_addr)

    @property
    def registers(self):
        regs = self._reg_kmc_08_start_address + self._reg_kmc_08_end_address
        regs.append(self._reg_kmc_08_line_offset_addr)
        regs.append(self._reg_kmc_08_mode)
        return regs
