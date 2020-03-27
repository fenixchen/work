import enum
from mem_common import *
from mem_reg import MemReg
from mem_agents.mem_agent import MemAgent
from mem_global_var import *


class VideoInType(enum.Enum):
    VIDEO_IN_1 = 0
    VIDEO_IN_2 = 1
    VIDEO_IN_3 = 2
    VIDEO_IN_4 = 3


class MemAgent_VIDEO_IN(MemAgent):
    # pylint: disable=invalid-name
    def __init__(self, video_in_type):
        self._video_in_type = video_in_type
        super().__init__(video_in_type.name, video_in_type.name, DDROp.W)

    def calc_memory(self):
        video_in_type = self._video_in_type
        if video_in_type == VideoInType.VIDEO_IN_1:
            Video_IN1_W_frame_rate = video_input_refresh_rate
            Video_IN1_W_bits = video_data_width
            Video_IN1_W_H_res = video_input_Hactive/4
            Video_IN1_W_V_res = video_input_Vtotal
            Video_IN1_W_VDE_res = video_input_Vactive
            Video_IN1_W_CPR_ratio = video_comp_ratio
            Video_IN1_W_Bandwidth = Video_IN1_W_frame_rate*Video_IN1_W_bits*Video_IN1_W_H_res*Video_IN1_W_V_res/Video_IN1_W_CPR_ratio/8/1000/1000*(IF(capture_w_en == 1, 1, 0))
            Video_IN1_W_DDR_size = ROUNDUP(Video_IN1_W_H_res/1024, 0)*1024*Video_IN1_W_bits*Video_IN1_W_VDE_res/Video_IN1_W_CPR_ratio/8/1024/1024*(IF(capture_w_en == 1, 1, 0))
            return Video_IN1_W_DDR_size, Video_IN1_W_Bandwidth
        elif video_in_type == VideoInType.VIDEO_IN_2:
            Video_IN2_W_frame_rate = video_input_refresh_rate
            Video_IN2_W_bits = video_data_width
            Video_IN2_W_H_res = video_input_Hactive/4
            Video_IN2_W_V_res = video_input_Vtotal
            Video_IN2_W_VDE_res = video_input_Vactive
            Video_IN2_W_CPR_ratio = video_comp_ratio
            Video_IN2_W_Bandwidth = Video_IN2_W_frame_rate*Video_IN2_W_bits*Video_IN2_W_H_res*Video_IN2_W_V_res/Video_IN2_W_CPR_ratio/8/1000/1000*(IF(capture_w_en == 1, 1, 0))
            Video_IN2_W_DDR_size = ROUNDUP(Video_IN2_W_H_res/1024, 0)*1024*Video_IN2_W_bits*Video_IN2_W_VDE_res/Video_IN2_W_CPR_ratio/8/1024/1024*(IF(capture_w_en == 1, 1, 0))
            return Video_IN2_W_DDR_size, Video_IN2_W_Bandwidth
        elif video_in_type == VideoInType.VIDEO_IN_3:
            Video_IN3_W_frame_rate = video_input_refresh_rate
            Video_IN3_W_bits = video_data_width
            Video_IN3_W_H_res = video_input_Hactive/4
            Video_IN3_W_V_res = video_input_Vtotal
            Video_IN3_W_VDE_res = video_input_Vactive
            Video_IN3_W_CPR_ratio = video_comp_ratio
            Video_IN3_W_Bandwidth = Video_IN3_W_frame_rate*Video_IN3_W_bits*Video_IN3_W_H_res*Video_IN3_W_V_res/Video_IN3_W_CPR_ratio/8/1000/1000*(IF(capture_w_en==1, 1, 0))
            Video_IN3_W_DDR_size = ROUNDUP(Video_IN3_W_H_res/1024, 0)*1024*Video_IN3_W_bits*Video_IN3_W_VDE_res/Video_IN3_W_CPR_ratio/8/1024/1024*(IF(capture_w_en==1, 1, 0))
            return Video_IN3_W_DDR_size, Video_IN3_W_Bandwidth
        elif video_in_type == VideoInType.VIDEO_IN_4:
            Video_IN4_W_frame_rate = video_input_refresh_rate
            Video_IN4_W_bits = video_data_width
            Video_IN4_W_H_res = video_input_Hactive/4
            Video_IN4_W_V_res = video_input_Vtotal
            Video_IN4_W_VDE_res = video_input_Vactive
            Video_IN4_W_CPR_ratio = video_comp_ratio
            Video_IN4_W_Bandwidth = Video_IN4_W_frame_rate*Video_IN4_W_bits*Video_IN4_W_H_res*Video_IN4_W_V_res/Video_IN4_W_CPR_ratio/8/1000/1000*(IF(capture_w_en==1, 1, 0))
            Video_IN4_W_DDR_size = ROUNDUP(Video_IN4_W_H_res/1024, 0)*1024*Video_IN4_W_bits*Video_IN4_W_VDE_res/Video_IN4_W_CPR_ratio/8/1024/1024*(IF(capture_w_en==1, 1, 0))
            return Video_IN4_W_DDR_size, Video_IN4_W_Bandwidth
        else:
            assert False, "Unknown type"
