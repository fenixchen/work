from mem_config import MemConfig
from mem_common import DDRTag
import mem_agents

class MemConfig_1Chip8K120Hz(MemConfig):
    # pylint: disable=invalid-name
    def __init__(self):
        super().__init__("1Chip8K120Hz")

        self._mm.add_agent(mem_agents.MemAgent_KMC_0(49.64, 650.70))            # IP_L_MC_HF_ENC_YC
        self._mm.add_agent(mem_agents.MemAgent_KMC_1(45.13, 591.55))            # IP_L_MC_LF_ENC_YC

        self._mm.add_agent(mem_agents.MemAgent_RO('KMC_5', 591.55, 'KMC_0'))    # MC_L_YC_HF_DEC_CUR
        self._mm.add_agent(mem_agents.MemAgent_RO('KMC_4', 0, 'KMC_0'))         # MC_L_YC_HF_DEC_PRE

        self._mm.add_agent(mem_agents.MemAgent_RO('KMC_7', 1183.09, 'KMC_1'))   # MC_L_YC_LF_DEC_CUR
        self._mm.add_agent(mem_agents.MemAgent_RO('KMC_6', 1183.09, 'KMC_1'))   # MC_L_YC_LF_DEC_PRE

        self._mm.add_agent(mem_agents.MemAgent_KMC_8(49.64, 650.70))            # IP_R_MC_HF_ENC_YC
        self._mm.add_agent(mem_agents.MemAgent_KMC_9(45.13, 591.55))            # IP_R_MC_LF_ENC_YC

        self._mm.add_agent(mem_agents.MemAgent_RO('KMC_11', 1301.40, 'KMC_8'))  # MC_R_YC_HF_DEC_CUR
        self._mm.add_agent(mem_agents.MemAgent_RO('KMC_10', 0, 'KMC_8'))        # MC_R_YC_HF_DEC_PRE

        self._mm.add_agent(mem_agents.MemAgent_RO('KMC_13', 1183.09, 'KMC_9'))  # MC_R_YC_LF_DEC_CUR
        self._mm.add_agent(mem_agents.MemAgent_RO('KMC_12', 1183.09, 'KMC_9'))  # MC_R_YC_LF_DEC_PRE

        self._mm.add_agent(mem_agents.MemAgent_KME_0(3.96, 32.4))               # IP_ME1_NR_W
        self._mm.add_agent(mem_agents.MemAgent_RO('KME_1', 32.40, 'KME_0'))     # IP_ME1_NR_R
        self._mm.add_agent(mem_agents.MemAgent_RO('KME_3', 64.80, 'KME_0'))     # ME1_CUR_R
        self._mm.add_agent(mem_agents.MemAgent_RO('KME_2', 64.80, 'KME_0'))     # ME1_PRE_R
        self._mm.add_agent(mem_agents.MemAgent_RO('KMV_11', 64.80, 'KME_0'))    # ME2_CUR_R
        self._mm.add_agent(mem_agents.MemAgent_RO('KMV_10', 64.80, 'KME_0'))    # ME2_PRE_R

        self._mm.add_agent(mem_agents.MemAgent_KME_8(1.98, 129.60))             # IP_LOG_W
        self._mm.add_agent(mem_agents.MemAgent_RO('KME_9', 129.60, 'KME_8'))    # IP_LOG_R

        self._mm.add_agent(mem_agents.MemAgent_KME_10(0.99, 64.80))             # IP_MASK_W
        self._mm.add_agent(mem_agents.MemAgent_RO('KME_11', 64.80, 'KME_10'))   # IP_MASK_R

        self._mm.add_agent(mem_agents.MemAgent_KME_12(0.25, 16.20))             # Pixel_LOGO_W
        self._mm.add_agent(mem_agents.MemAgent_RO('KME_13', 32.40, 'KME_12'))   # Pixel_LOGO_R     

        self._mm.add_agent(mem_agents.MemAgent_KME_14(0.06, 4.05))              # HOG_history_W
        self._mm.add_agent(mem_agents.MemAgent_RO('KME_15', 4.05, 'KME_14'))    # HOG_history_R    

        self._mm.add_agent(mem_agents.MemAgent_KMV_01(0.32, 42.63))             # ME2_Loop_PH_W
        self._mm.add_agent(mem_agents.MemAgent_RO('KMV_07', 4.05, 'KMV_01'))    # ME2_Loop_PH_R
        
        self._mm.add_agent(mem_agents.MemAgent_KMV_02(0.62, 81))                # ME1_Loop_PPI_W
        self._mm.add_agent(mem_agents.MemAgent_RO('KMV_03', 81, 'KMV_02'))      # ME1_Loop_PPI_R
        
        self._mm.add_agent(mem_agents.MemAgent_KMV_04(1.53, 66.83))             # ME1_VBUF_PPFV_W
        self._mm.add_agent(mem_agents.MemAgent_RO('KMV_08', 66.83, 'KMV_04'))   # ME1_VBUF_PPFV_R
        self._mm.add_agent(mem_agents.MemAgent_RO('KMV_09', 129.60, 'KMV_04'))  # ME1_VBUF_PFVPI_R
                
        self._mm.add_agent(mem_agents.MemAgent_KMV_05(1.98, 129.60))             # ME1_Loop_PFVPI_W
        self._mm.add_agent(mem_agents.MemAgent_RO('KMV_06', 129.60, 'KMV_05'))   # ME1_Loop_PFVPI_R        

        self._mm.add_agent(mem_agents.MemAgent_OD_W(4.07, 533.52))               # TOP_OD_W_L
        self._mm.add_agent(mem_agents.MemAgent_RO('OD_R', 129.60, 'OD_W'))       # TOP_OD_R_L

        self._mm.add_agent(mem_agents.MemAgent_TOP_DEMURA_R(5.58, 729.76))       # TOP_DEMURA_R

        self._mm.add_agent(mem_agents.MemAgent_BOT_OD_W(0, 0))                   # BOT_OD_W
        self._mm.add_agent(mem_agents.MemAgent_RO('BOT_OD_R', 0, 'BOT_OD_W'))    # TOP_OD_R_L

        self._mm.add_agent(mem_agents.MemAgent_BOT_DEMURA_R(0, 0))               # BOT_DEMURA_R

    def place_memory(self):

        self._mm.get_agent('KMC_0').start_addr = 0x01000000
        self._mm.get_agent('KMC_0').ddr_tag = DDRTag.DDR3
        self._mm.get_agent('KMC_1').ddr_tag = DDRTag.DDR3

        self._mm.get_agent('KMC_8').start_addr = 0x02000000
        self._mm.get_agent('KMC_8').ddr_tag = DDRTag.DDR4
        self._mm.get_agent('KMC_9').ddr_tag = DDRTag.DDR4

        self._mm.get_agent('KME_0').start_addr = 0x03000000
        self._mm.get_agent('KME_0').ddr_tag = DDRTag.DDR2
        self._mm.get_agent('KME_8').ddr_tag = DDRTag.DDR2
        self._mm.get_agent('KME_10').ddr_tag = DDRTag.DDR2
        self._mm.get_agent('KME_12').ddr_tag = DDRTag.DDR2
        self._mm.get_agent('KME_14').ddr_tag = DDRTag.DDR2

        self._mm.get_agent('KMV_01').start_addr = 0x04000000
        self._mm.get_agent('KMV_01').ddr_tag = DDRTag.DDR1
        self._mm.get_agent('KMV_02').ddr_tag = DDRTag.DDR1
        self._mm.get_agent('KMV_04').ddr_tag = DDRTag.DDR1
        self._mm.get_agent('KMV_05').ddr_tag = DDRTag.DDR1

        self._mm.get_agent('OD_W').start_addr = 0x05000000
        self._mm.get_agent('OD_W').ddr_tag = DDRTag.DDR2 #TODO TOP_OD_L or TOP_OD_W, DDR?

        self._mm.get_agent('TOP_DEMURA_R').ddr_tag = DDRTag.DDR2

        self._mm.get_agent('BOT_OD_W').ddr_tag = DDRTag.DDR2

        self._mm.get_agent('BOT_DEMURA_R').ddr_tag = DDRTag.DDR2
        

def main():
    config = MemConfig_1Chip8K120Hz()
    regs = config.generate_registers()
    config.print_mapping()
    
if __name__ == '__main__':
    main()
