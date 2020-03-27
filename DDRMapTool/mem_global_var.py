from mem_common import IF

# pylint: disable=invalid-name
# global parameter
DDR_speed = 2133  # MHz
DDR_size = 1024  # MByte
DNN_num = 2                     # 0--3
MEMC_mode = 2  # 0:bypass 1:PC mode 2:MEMC on
MEMC_vfilp = 1
Top_OD_en = 1
Top_demura_en = 1
BOT_OD_en = 0
BOT_demura_en = 0
OSD_en = 1
LDG_on = 0
Local_Dimming_en = 1

# output parameter
output_Htotal = 8800
output_Hactive = 7680
output_Vtotal = 4500
output_Vactive = 4320
output_refresh_rate = 120

# video_input parameter
video_input_Htotal = 8800
video_input_Hactive = 7680
video_input_Vtotal = 4500
video_input_Vactive = 4320
video_input_refresh_rate = 60
video_data_width = 20
video_comp_ratio = video_data_width/(IF(video_data_width == 20, 11, (IF(video_data_width == 30, 16, 18))))

# OSD_input parameter
OSD_input_Htotal = 2200
OSD_input_Hactive = 1920
OSD_input_Vtotal = 1125
OSD_input_Vactive = 1080
OSD_output_refresh_rate = 120
OSD_input_refresh_rate = 30
OSD_data_width = 30
OSD_alpha_width = 8
OSD_data_comp_ratio = 1.875
OSD_alpha_comp_ratio = 2.67
OSD_Framedelay = 2

# dual_cell parameter
dual_cell_Htotal = 4400
dual_cell_Hactive = 3840
dual_cell_Vtotal = 2250
dual_cell_Vactive = 2160
dual_cell_refresh_rate = 120

# MEMC parameter
MEMC_en = IF(MEMC_mode == 0, 0, 1)
PC_mode = IF(MEMC_mode == 1, 1, 0)
MEMC_vflip = MEMC_vfilp
MC_single_mode = 1
ME_H_ratio = 8
ME_V_ratio = 8
LOGO_MC_ratio_H = 4
LOGO_MC_ratio_V = 4
ME1_block_size_H = 16
ME1_block_size_V = 16
ME2_block_size_H = 16
ME2_block_size_V = 16


MC_H_bits = MEMC_en*IF(PC_mode, 33, 22)
MC_H_Hact = video_input_Hactive
MC_H_Hoverlap = 16
MC_H_Vtotal = video_input_Vtotal
MC_H_Vact = video_input_Vactive
MC_H_in_framerate = video_input_refresh_rate
MC_H_out_framerate = output_refresh_rate
MC_H_buff_num = IF(PC_mode, IF(MEMC_vflip, 2, 1), IF(MEMC_vflip, 5, 5))
MC_H_CPR_ratio = 2.2

MC_L_bits = MEMC_en*IF(PC_mode, 30, 20)
MC_L_Hact = video_input_Hactive
MC_L_Hoverlap = 16
MC_L_Vtotal = video_input_Vtotal
MC_L_Vact = video_input_Vactive
MC_L_in_framerate = video_input_refresh_rate
MC_L_out_framerate = output_refresh_rate
MC_L_buff_num = IF(PC_mode, IF(MEMC_vflip, 2, 1), IF(MEMC_vflip, 5, 5))
MC_L_CPR_ratio = 2.2

ME_bits = MEMC_en*8*IF(PC_mode, 0, 1)
ME_Hact = video_input_Hactive/ME_H_ratio
ME_Hoverlap = 0
ME_Vtotal = video_input_Vtotal/ME_V_ratio
ME_Vact = video_input_Vactive/ME_V_ratio
ME_in_framerate = video_input_refresh_rate
ME_out_framerate = output_refresh_rate
ME_buff_num = 8
ME_CPR_ratio = 1

# TCON
TOP_OD_en = Top_OD_en
TOP_Demura_en = Top_demura_en
BOT_OD_en = BOT_OD_en
BOT_Demura_en = BOT_demura_en
Demura_ratio = 8

TOP_OD_bits = TOP_OD_en*24
TOP_OD_Hact = output_Hactive
TOP_OD_Vtotal = output_Vtotal
TOP_OD_Vact = output_Vactive
TOP_OD_framerate = output_refresh_rate
TOP_OD_CPR_ratio = 5.83*2

TOP_Demura_bits = TOP_OD_en*90
TOP_Demura_Hact = output_Hactive/Demura_ratio+1
TOP_Demura_Vtotal = output_Vtotal/Demura_ratio
TOP_Demura_Vact = output_Vactive/Demura_ratio+1
TOP_Demura_framerate = output_refresh_rate
TOP_Demura_CPR_ratio = 1

BOT_OD_bits = BOT_OD_en*8
BOT_OD_Hact = dual_cell_Hactive
BOT_OD_Vtotal = dual_cell_Vtotal
BOT_OD_Vact = dual_cell_Vactive
BOT_OD_framerate = dual_cell_refresh_rate
BOT_OD_CPR_ratio = 5.83*2

BOT_Demura_bits = BOT_Demura_en*30
BOT_Demura_Hact = dual_cell_Hactive/Demura_ratio
BOT_Demura_Vtotal = dual_cell_Vtotal/Demura_ratio
BOT_Demura_Vact = dual_cell_Vactive/Demura_ratio
BOT_Demura_framerate = dual_cell_refresh_rate
BOT_Demura_CPR_ratio = 1

# 3D NR&SR
IIR_en = 1
IIR_R_frame = 1
IIR_buff_num = 1
FIR_R_frame = 5
FIR_buff_num = 14
Cadence_en = 0
capture_w_en = 0

# 2D NR
Detect_common = 1

# DNN accelerator
DNN_Addr_Interleave = 2

DDR_frequence = 2133 * 1024 * 1024
DDR_bit_width = 32 / 8
DDR_performance = 0.6
DDR_bandwidth = DDR_frequence * DDR_bit_width
