from mem_config import MemConfig
from mem_common import DDRTag
import mem_agents


class MemConfig_1Chip8K120Hz(MemConfig):
    # pylint: disable=invalid-name
    def __init__(self):
        super().__init__("1Chip8K120Hz")
        mm = self._mm

        block = mm.add_block("MEMC_MC_L")
        mm.add_agent(mem_agents.MemAgent_KMC_0(), block)
        mm.add_agent(mem_agents.MemAgent_KMC_1(), block)
        mm.add_agent(mem_agents.MemAgent_RO('KMC_5', 'KMC_0', 'MC_L_YC_HF_DEC_CUR'), block)
        mm.add_agent(mem_agents.MemAgent_RO('KMC_4', 'KMC_0', 'MC_L_YC_HF_DEC_PRE'), block)
        mm.add_agent(mem_agents.MemAgent_RO('KMC_7', 'KMC_1', 'MC_L_YC_LF_DEC_CUR'), block)
        mm.add_agent(mem_agents.MemAgent_RO('KMC_6', 'KMC_1', 'MC_L_YC_LF_DEC_PRE'), block)

        block = mm.add_block("MEMC_MC_R")
        mm.add_agent(mem_agents.MemAgent_KMC_8(), block)
        mm.add_agent(mem_agents.MemAgent_KMC_9(), block)
        mm.add_agent(mem_agents.MemAgent_RO('KMC_11', 'KMC_8', 'MC_R_YC_HF_DEC_CUR'), block)
        mm.add_agent(mem_agents.MemAgent_RO('KMC_10', 'KMC_8', 'MC_R_YC_HF_DEC_PRE'), block)
        mm.add_agent(mem_agents.MemAgent_RO('KMC_13', 'KMC_9', 'MC_R_YC_LF_DEC_CUR'), block)
        mm.add_agent(mem_agents.MemAgent_RO('KMC_12', 'KMC_9', 'MC_R_YC_LF_DEC_PRE'), block)

        block = mm.add_block("MEMC_ME1/2_LOGO")
        mm.add_agent(mem_agents.MemAgent_KME_0(), block)
        mm.add_agent(mem_agents.MemAgent_RO('KME_1', 'KME_0', 'IP_ME1_NR_R'), block)
        mm.add_agent(mem_agents.MemAgent_RO('KME_3', 'KME_0', 'ME1_CUR_R'), block)
        mm.add_agent(mem_agents.MemAgent_RO('KME_2', 'KME_0', 'ME1_PRE_R'), block)
        mm.add_agent(mem_agents.MemAgent_RO('KMV_11', 'KME_0', 'ME2_CUR_R'), block)
        mm.add_agent(mem_agents.MemAgent_RO('KMV_10', 'KME_0', 'ME2_PRE_R'), block)
        mm.add_agent(mem_agents.MemAgent_KME_8(), block)
        mm.add_agent(mem_agents.MemAgent_RO('KME_9', 'KME_8', 'IP_LOG_R'), block)
        mm.add_agent(mem_agents.MemAgent_KME_10(), block)
        mm.add_agent(mem_agents.MemAgent_RO('KME_11', 'KME_10', 'IP_MASK_R'), block)
        mm.add_agent(mem_agents.MemAgent_KME_12(), block)
        mm.add_agent(mem_agents.MemAgent_RO('KME_13', 'KME_12', 'Pixel_LOGO_R'), block)
        mm.add_agent(mem_agents.MemAgent_KME_14(), block)
        mm.add_agent(mem_agents.MemAgent_RO('KME_15', 'KME_14', 'HOG_history_R'), block)

        block = mm.add_block("MEMC_Vector_Logo")
        mm.add_agent(mem_agents.MemAgent_KMV_01(), block)
        mm.add_agent(mem_agents.MemAgent_RO('KMV_07', 'KMV_01', 'ME2_Loop_PH_R'), block)
        mm.add_agent(mem_agents.MemAgent_KMV_02(), block)
        mm.add_agent(mem_agents.MemAgent_RO('KMV_03', 'KMV_02', 'ME1_Loop_PPI_R'), block)

        mm.add_agent(mem_agents.MemAgent_KMV_04(), block)
        mm.add_agent(mem_agents.MemAgent_RO('KMV_08', 'KMV_04', 'ME1_VBUF_PPFV_R'), block)
        mm.add_agent(mem_agents.MemAgent_RO('KMV_09', 'KMV_04', 'ME1_VBUF_PFVPI_R'), block)

        mm.add_agent(mem_agents.MemAgent_KMV_05(), block)
        mm.add_agent(mem_agents.MemAgent_RO('KMV_06', 'KMV_05', 'ME1_Loop_PFVPI_R'), block)

        block = mm.add_block('TOP_TCON_OD_L')
        mm.add_agent(mem_agents.MemAgent_OD_W(), block)
        mm.add_agent(mem_agents.MemAgent_RO('OD_R', 'OD_W', 'TOP_OD_R_L'), block)

        block = mm.add_block('TOP_TCON_OD_R')
        mm.add_agent(mem_agents.MemAgent_TOP_OD_W(), block)
        mm.add_agent(mem_agents.MemAgent_RO('TOP_OD_R', 'TOP_OD_W', 'TOP_OD_R_R'), block)

        block = mm.add_block('TOP_DEMURA')
        mm.add_agent(mem_agents.MemAgent_TOP_DEMURA_R(), block)

        block = mm.add_block('BOT_TCON_OD')
        mm.add_agent(mem_agents.MemAgent_BOT_OD_W(), block)
        mm.add_agent(mem_agents.MemAgent_RO('BOT_OD_R', 'BOT_OD_W', 'BOT_OD_R'), block)

        block = mm.add_block('BOT_DEMURA')
        mm.add_agent(mem_agents.MemAgent_BOT_DEMURA_R(), block)

        block = mm.add_block('OSD')
        mm.add_agent(mem_agents.MemAgent_GFX(mem_agents.GFXType.GFX_IN_1), block)
        mm.add_agent(mem_agents.MemAgent_GFX(mem_agents.GFXType.GFX_IN_2), block)
        mm.add_agent(mem_agents.MemAgent_GFX(mem_agents.GFXType.GFX_ALPHA), block)
        mm.add_agent(mem_agents.MemAgent_GFX(mem_agents.GFXType.GFX_R_1), block)
        mm.add_agent(mem_agents.MemAgent_GFX(mem_agents.GFXType.GFX_R_2), block)
        mm.add_agent(mem_agents.MemAgent_GFX(mem_agents.GFXType.GFX_ALPHA_R), block)

        block = mm.add_block('3D_NR/SR')
        mm.add_agent(mem_agents.MemAgent_VIDEO_IN(mem_agents.VideoInType.VIDEO_IN_1), block)
        mm.add_agent(mem_agents.MemAgent_VIDEO_IN(mem_agents.VideoInType.VIDEO_IN_2), block)
        mm.add_agent(mem_agents.MemAgent_VIDEO_IN(mem_agents.VideoInType.VIDEO_IN_3), block)
        mm.add_agent(mem_agents.MemAgent_VIDEO_IN(mem_agents.VideoInType.VIDEO_IN_4), block)

    def place_memory(self):
        mm = self._mm

        mm.get_agent('KMC_0').start_addr = 0x01000000
        mm.get_agent('KMC_0').ddr_tag = DDRTag.DDR3
        mm.get_agent('KMC_1').ddr_tag = DDRTag.DDR3

        mm.get_agent('KMC_8').start_addr = 0x02000000
        mm.get_agent('KMC_8').ddr_tag = DDRTag.DDR4
        mm.get_agent('KMC_9').ddr_tag = DDRTag.DDR4

        mm.get_agent('KME_0').start_addr = 0x03000000
        mm.get_agent('KME_0').ddr_tag = DDRTag.DDR2
        mm.get_agent('KME_8').ddr_tag = DDRTag.DDR2
        mm.get_agent('KME_10').ddr_tag = DDRTag.DDR2
        mm.get_agent('KME_12').ddr_tag = DDRTag.DDR2
        mm.get_agent('KME_14').ddr_tag = DDRTag.DDR2

        mm.get_agent('KMV_01').start_addr = 0x04000000
        mm.get_agent('KMV_01').ddr_tag = DDRTag.DDR1
        mm.get_agent('KMV_02').ddr_tag = DDRTag.DDR1
        mm.get_agent('KMV_04').ddr_tag = DDRTag.DDR1
        mm.get_agent('KMV_05').ddr_tag = DDRTag.DDR1

        mm.get_agent('OD_W').start_addr = 0x05000000
        mm.get_agent('OD_W').ddr_tag = DDRTag.DDR2

        mm.get_agent('TOP_DEMURA_R').ddr_tag = DDRTag.DDR2

        mm.get_agent('BOT_OD_W').ddr_tag = DDRTag.DDR2

        mm.get_agent('BOT_DEMURA_R').ddr_tag = DDRTag.DDR2


def main():
    config = MemConfig_1Chip8K120Hz()
    regs = config.generate_registers()
    # config.print_mapping()


if __name__ == '__main__':

    main()
