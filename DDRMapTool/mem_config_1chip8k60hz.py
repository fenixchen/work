from mem_config import MemConfig
from mem_common import DDRTag
from mem_global_var import GV


class MemConfig_1Chip8K60Hz(MemConfig):
    # pylint: disable=invalid-name
    def __init__(self):
        super().__init__("1Chip8K60Hz")
        GV.mod_value('output_refresh_rate', 60)
        GV.mod_value('MEMC_mode', 1)

    def pre_place_memory(self):
        mm = self._mm

        mm.get_agent('KMC_0').init_memory(DDRTag.DDR3)
        mm.get_agent('KMC_1').init_memory(DDRTag.DDR3)

        mm.get_agent('KMC_8').init_memory(DDRTag.DDR4)
        mm.get_agent('KMC_9').init_memory(DDRTag.DDR4)

        mm.get_agent('KME_0').init_memory(DDRTag.DDR2)
        mm.get_agent('KME_8').init_memory(DDRTag.DDR2)
        mm.get_agent('KME_10').init_memory(DDRTag.DDR2)
        mm.get_agent('KME_12').init_memory(DDRTag.DDR2)
        mm.get_agent('KME_14').init_memory(DDRTag.DDR2)

        mm.get_agent('KMV_01').init_memory(DDRTag.DDR1)
        mm.get_agent('KMV_02').init_memory(DDRTag.DDR1)
        mm.get_agent('KMV_04').init_memory(DDRTag.DDR1)
        mm.get_agent('KMV_05').init_memory(DDRTag.DDR1)

        mm.get_agent('OD_W').init_memory(DDRTag.DDR2)
        mm.get_agent('TOP_DEMURA_R').init_memory(DDRTag.DDR2)
        mm.get_agent('BOT_OD_W').init_memory(DDRTag.DDR2)
        mm.get_agent('BOT_DEMURA_R').init_memory(DDRTag.DDR2)

        mm.get_agent('GFX_IN_1').init_memory(DDRTag.DDR3)
        mm.get_agent('GFX_IN_2').init_memory(DDRTag.DDR4)
        mm.get_agent('GFX_R_1').init_memory(DDRTag.DDR3)
        mm.get_agent('GFX_R_2').init_memory(DDRTag.DDR4)
        mm.get_agent('GFX_ALPHA_R').init_memory(DDRTag.DDR1)

        mm.get_agent('VIDEO_IN_1').init_memory(DDRTag.NONE)
        mm.get_agent('VIDEO_IN_2').init_memory(DDRTag.NONE)
        mm.get_agent('VIDEO_IN_3').init_memory(DDRTag.NONE)
        mm.get_agent('VIDEO_IN_4').init_memory(DDRTag.NONE)

        mm.get_agent('SRP_READ_1').init_memory(DDRTag.DDR1)
        mm.get_agent('SRP_READ_2').init_memory(DDRTag.DDR1)
        mm.get_agent('SRP_READ_3').init_memory(DDRTag.DDR2)
        mm.get_agent('SRP_READ_4').init_memory(DDRTag.DDR2)

        mm.get_agent('SRP_FIR_WRITE_1').init_memory(DDRTag.DDR1)
        mm.get_agent('SRP_FIR_WRITE_2').init_memory(DDRTag.DDR1)
        mm.get_agent('SRP_FIR_WRITE_3').init_memory(DDRTag.DDR2)
        mm.get_agent('SRP_FIR_WRITE_4').init_memory(DDRTag.DDR2)

        mm.get_agent('SRP_NR_OUT_WRITE_1').init_memory(DDRTag.DDR1)
        mm.get_agent('SRP_NR_OUT_WRITE_2').init_memory(DDRTag.DDR1)
        mm.get_agent('SRP_NR_OUT_WRITE_3').init_memory(DDRTag.DDR2)
        mm.get_agent('SRP_NR_OUT_WRITE_4').init_memory(DDRTag.DDR2)

        mm.get_agent('MV_W_3DRS').init_memory(DDRTag.DDR2)
        mm.get_agent('MV_R_3DRS').init_memory(DDRTag.DDR2)
        mm.get_agent('CNT_W_3DRS').init_memory(DDRTag.DDR2)
        mm.get_agent('CNT_R_3DRS').init_memory(DDRTag.DDR2)

        mm.get_agent('AISR_R').init_memory(DDRTag.NONE)
        mm.get_agent('AISR_W_1').init_memory(DDRTag.NONE)
        mm.get_agent('AISR_W_2').init_memory(DDRTag.NONE)

        mm.get_agent('AISR_MAP').init_memory(DDRTag.DDR1)
        mm.get_agent('LOCAL_AI_W').init_memory(DDRTag.DDR1)
        mm.get_agent('LOCAL_AI_R').init_memory(DDRTag.DDR1)

        mm.get_agent('2D_NR_DECONTOUR_W').init_memory(DDRTag.DDR1)
        mm.get_agent('2D_NR_DECONTOUR_R').init_memory(DDRTag.DDR1)

        mm.get_agent('2D_NR_BMNR_W').init_memory(DDRTag.NONE)
        mm.get_agent('2D_NR_BMNR_R').init_memory(DDRTag.NONE)

        mm.get_agent('LOCAL_CONTRAST_1_W').init_memory(DDRTag.DDR1)
        mm.get_agent('LOCAL_CONTRAST_1_R').init_memory(DDRTag.DDR1)
        mm.get_agent('LOCAL_CONTRAST_2_W').init_memory(DDRTag.DDR1)
        mm.get_agent('LOCAL_CONTRAST_2_R').init_memory(DDRTag.DDR1)

        mm.get_agent('DNN_IN_1').init_memory(DDRTag.DDR1)
        mm.get_agent('DNN_IN_2').init_memory(DDRTag.DDR2)
        mm.get_agent('DNN_IN_3').init_memory(DDRTag.DDR3)
        mm.get_agent('DNN_IN_4').init_memory(DDRTag.DDR4)

        mm.get_agent('PLDD_W').init_memory(DDRTag.NONE)
        mm.get_agent('PLDD_R').init_memory(DDRTag.NONE)

        mm.get_agent('SRP_OUT_W_1').init_memory(DDRTag.DDR1)
        mm.get_agent('SRP_OUT_W_2').init_memory(DDRTag.DDR2)
        mm.get_agent('SRP_OUT_W_3').init_memory(DDRTag.DDR3)
        mm.get_agent('SRP_OUT_W_4').init_memory(DDRTag.DDR4)

        mm.get_agent('LOCAL_DIMMING_W').init_memory(DDRTag.DDR1)
        mm.get_agent('LOCAL_DIMMING_R').init_memory(DDRTag.DDR1)

        mm.get_agent('LDR_R1').init_memory(DDRTag.DDR1)
        mm.get_agent('LDR_R2').init_memory(DDRTag.DDR1)
        mm.get_agent('LDR_R3').init_memory(DDRTag.DDR1)
        mm.get_agent('LDR_R4').init_memory(DDRTag.DDR1)

        mm.get_agent('CPU').init_memory(DDRTag.DDR4)


def main():
    config = MemConfig_1Chip8K60Hz()
    mapping = config.place_memory()
    config.print_mapping(mapping, False)
    # config.print_registers(mapping)


if __name__ == '__main__':

    main()
