from mem_common import HEX2DEC, RegType, DEC2HEX, ROUNDUP, DDROp
from mem_reg import MemReg
from mem_global_var import *
from mem_agents.mem_agent import MemAgent


class MemAgent_KMC_9(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self):
        super().__init__('KMC_9', 'IP_R_MC_LF_ENC_YC', DDROp.W)
        # from  reg_kmc_09_start_address0 to reg_kmc_09_start_address7
        self._reg_kmc_09_start_address = [None] * 8
        for i in range(8):
            name = 'reg_kmc_09_start_address%d' % i
            addr = name  # same here, find in global register map later
            self._reg_kmc_09_start_address[i] = MemReg(name, addr, RegType.START)

        self._reg_kmc_09_end_address = [None] * 8
        for i in range(8):
            name = 'reg_kmc_09_end_address%d' % i
            addr = name  # same here, find in global register map later
            self._reg_kmc_09_end_address[i] = MemReg(name, addr, RegType.END)

        self._reg_kmc_09_line_offset_addr = MemReg('reg_kmc_09_line_offset_addr', 'reg_kmc_09_line_offset_addr', RegType.OTHER)

        self._reg_kmc_09_mode = MemReg('reg_kmc_09_mode', 'reg_kmc_09_mode', RegType.OTHER)
        self._reg_kmc_09_mode.value = 1

    def calc_memory(self):
        KMC_9_frame_rate = GV.MC_L_in_framerate
        KMC_9_bits = GV.MC_L_bits
        KMC_9_H_res = GV.MC_L_Hact/2+GV.MC_L_Hoverlap
        KMC_9_V_res = GV.MC_L_Vtotal/2
        KMC_9_VDE_res = GV.MC_L_Vact/2
        KMC_9_CPR_ratio = GV.MC_L_CPR_ratio
        KMC_9_Bandwidth = KMC_9_frame_rate*KMC_9_bits*KMC_9_H_res*KMC_9_V_res/KMC_9_CPR_ratio/8/1000/1000
        KMC_9_DDR_size = KMC_9_bits*KMC_9_H_res*KMC_9_VDE_res/KMC_9_CPR_ratio/8/1024/1024*GV.MC_L_buff_num
        return KMC_9_DDR_size, KMC_9_Bandwidth

    def allocate_memory(self, reg_dict):

        B3 = 3856  # H_act
        C3 = 4320  # V_act
        REAL_HACT = 3840
        REAL_VACT = 4320
        LOGO_VACT = 1080
        ME_VACT = 540
        ROW_NUM = 270
        ROW_NUM2 = 270
        KMC00_start_address = self.start_addr
        KMC08_start_address = 0
        KME_start_address = 0
        KMV_star_address = 0
        Tcon_PQ_address = 0

        #kmc_09  (V_act/2+2)*ROUNDUP(ROUNDUP(H_act*data_width/CRP_ration,0)/128,0)*128/8
        B3 = 3856  # H_act
        C3 = 4320  # V_act
        C7 = 20  # data_width
        D7 = B3  # H
        E7 = C3/2+2  # V
        F7 = 2.2  # CPR ratio
        kmc_09_LineOffset_VD = DEC2HEX(ROUNDUP(ROUNDUP(D7 * C7 / F7, 0) / 128, 0)*128/8)
        kmc_09_MC_LF_VD_CPR = DEC2HEX((HEX2DEC(kmc_09_LineOffset_VD) * E7))

        reg_kmc_09_start_address0 = self.start_addr
        reg_kmc_09_start_address1 = DEC2HEX(HEX2DEC(reg_kmc_09_start_address0) + HEX2DEC(kmc_09_MC_LF_VD_CPR))
        reg_kmc_09_start_address2 = DEC2HEX(HEX2DEC(reg_kmc_09_start_address1) + HEX2DEC(kmc_09_MC_LF_VD_CPR))
        reg_kmc_09_start_address3 = DEC2HEX(HEX2DEC(reg_kmc_09_start_address2) + HEX2DEC(kmc_09_MC_LF_VD_CPR))
        reg_kmc_09_start_address4 = DEC2HEX(HEX2DEC(reg_kmc_09_start_address3) + HEX2DEC(kmc_09_MC_LF_VD_CPR))
        reg_kmc_09_start_address5 = reg_kmc_09_start_address4
        reg_kmc_09_start_address6 = reg_kmc_09_start_address5
        reg_kmc_09_start_address7 = reg_kmc_09_start_address6

        reg_kmc_09_end_address0 = DEC2HEX(HEX2DEC(reg_kmc_09_start_address0) + HEX2DEC(kmc_09_LineOffset_VD)*REAL_VACT/2)
        reg_kmc_09_end_address1 = DEC2HEX(HEX2DEC(reg_kmc_09_start_address1) + HEX2DEC(kmc_09_LineOffset_VD)*REAL_VACT/2)
        reg_kmc_09_end_address2 = DEC2HEX(HEX2DEC(reg_kmc_09_start_address2) + HEX2DEC(kmc_09_LineOffset_VD)*REAL_VACT/2)
        reg_kmc_09_end_address3 = DEC2HEX(HEX2DEC(reg_kmc_09_start_address3) + HEX2DEC(kmc_09_LineOffset_VD)*REAL_VACT/2)
        reg_kmc_09_end_address4 = DEC2HEX(HEX2DEC(reg_kmc_09_start_address4) + HEX2DEC(kmc_09_LineOffset_VD)*REAL_VACT/2)
        reg_kmc_09_end_address5 = DEC2HEX(HEX2DEC(reg_kmc_09_start_address5) + HEX2DEC(kmc_09_LineOffset_VD)*REAL_VACT/2)
        reg_kmc_09_end_address6 = DEC2HEX(HEX2DEC(reg_kmc_09_start_address6) + HEX2DEC(kmc_09_LineOffset_VD)*REAL_VACT/2)
        reg_kmc_09_end_address7 = DEC2HEX(HEX2DEC(reg_kmc_09_start_address7) + HEX2DEC(kmc_09_LineOffset_VD)*REAL_VACT/2)

        reg_kmc_09_line_offset_addr = kmc_09_LineOffset_VD
        reg_kmc_09_mode = 1

        self._reg_kmc_09_start_address[0].value = reg_kmc_09_start_address0
        self._reg_kmc_09_start_address[1].value = reg_kmc_09_start_address1
        self._reg_kmc_09_start_address[2].value = reg_kmc_09_start_address2
        self._reg_kmc_09_start_address[3].value = reg_kmc_09_start_address3
        self._reg_kmc_09_start_address[4].value = reg_kmc_09_start_address4
        self._reg_kmc_09_start_address[5].value = reg_kmc_09_start_address5
        self._reg_kmc_09_start_address[6].value = reg_kmc_09_start_address6
        self._reg_kmc_09_start_address[7].value = reg_kmc_09_start_address7

        self._reg_kmc_09_end_address[0].value = reg_kmc_09_end_address0
        self._reg_kmc_09_end_address[1].value = reg_kmc_09_end_address1
        self._reg_kmc_09_end_address[2].value = reg_kmc_09_end_address2
        self._reg_kmc_09_end_address[3].value = reg_kmc_09_end_address3
        self._reg_kmc_09_end_address[4].value = reg_kmc_09_end_address4
        self._reg_kmc_09_end_address[5].value = reg_kmc_09_end_address5
        self._reg_kmc_09_end_address[6].value = reg_kmc_09_end_address6
        self._reg_kmc_09_end_address[7].value = reg_kmc_09_end_address7

        self._reg_kmc_09_line_offset_addr.value = reg_kmc_09_line_offset_addr

        self._reg_kmc_09_mode.value = reg_kmc_09_mode

        regs = self._reg_kmc_09_start_address + self._reg_kmc_09_end_address
        for reg in regs:
            reg.value += self.ddr_base_offset

        self.set_memory_range(reg_kmc_09_start_address0, reg_kmc_09_end_address7)

    @property
    def registers(self):
        regs = self._reg_kmc_09_start_address + self._reg_kmc_09_end_address
        regs.append(self._reg_kmc_09_line_offset_addr)
        regs.append(self._reg_kmc_09_mode)
        return regs
