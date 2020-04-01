import enum
import inspect
from collections import OrderedDict
from copy import deepcopy
from mem_common import *


class VarType(enum.Enum):
    DEC = 0
    HEX = 1
    BOOL = 2
    FLOAT = 3
    DEFAULT = 4


# singlton class
class MemGlobalVar:
    instance = None

    def __new__(cls, *args, **kw):
        if cls.instance is None:
            cls.instance = object.__new__(cls, *args, **kw)
        return cls.instance

    def __init__(self):
        self._default_var_dict = OrderedDict()
        self._current_config = 'default'
        self._config_dict = {}
        self._config_dict[self._current_config] = self._default_var_dict

    @property
    def default_var_dict(self):
        return self._default_var_dict

    @property
    def current_config(self):
        return self._current_config

    @property
    def config_list(self):
        return self._config_dict.keys()

    def set_current_config(self, config):
        if config not in self._config_dict:
            p_warn('Add new variable config: <%s>' % config)
            self._config_dict[config] = deepcopy(self._default_var_dict)
        self._current_config = config

    @property
    def var_dict(self):
        return self._config_dict[self._current_config]

    @classmethod
    def add_var(cls, var):
        cls.instance.default_var_dict[var.name] = var

    def print_vars(self, config=None):
        if config is None:
            config = self._current_config
        var_dict = self._config_dict[config]
        for var in var_dict.values():
            p_debug(var)

    def __getattr__(self, name):
        var_dict = self._config_dict[self._current_config]
        if name in var_dict:
            return var_dict[name].value
        else:
            assert False, 'var %s does not exists' % name

    def __getitem__(self, name):
        var_dict = self._config_dict[self._current_config]
        if name in var_dict:
            return var_dict[name]
        else:
            assert False, 'var %s does not exists' % name

    def mod_value(self, name, value):
        current_config = self._current_config
        config_dict = self._config_dict
        var_dict = config_dict[current_config]
        if name in var_dict:
            var_dict[name].value = value
        else:
            raise KeyError()

    def init_vars(self):
        MemVar('DDR_speed', 2133)   # MHz
        MemVar('DDR_total_size', 512)  # M Byte
        MemVar('DDR_count', 4)
        MemVar('DDR_size', lambda: int(GV.DDR_total_size / GV.DDR_count))
        MemVar('DDR_size_byte', lambda: GV.DDR_size * 1024 * 1024, var_type=VarType.HEX, digits=8)
        MemVar('DNN_num', 2)  # 0--3
        MemVar('MEMC_mode', 2)  # 0:bypass 1:PC mode 2:MEMC on
        MemVar('MEMC_vfilp', 1)
        MemVar('Top_OD_en', 1, VarType.BOOL)
        MemVar('Top_demura_en', 1, VarType.BOOL)
        MemVar('BOT_OD_en', 0, VarType.BOOL)
        MemVar('BOT_demura_en', 0)
        MemVar('OSD_en', 1, VarType.BOOL)
        MemVar('LDG_on', 0, VarType.BOOL)
        MemVar('Local_Dimming_en', 1, VarType.BOOL)

        # output parameter
        MemVar('output_Htotal', 8800)
        MemVar('output_Hactive', 7680)
        MemVar('output_Vtotal', 4500)
        MemVar('output_Vactive', 4320)
        MemVar('output_refresh_rate', 120)

        # video_input parameter
        MemVar('video_input_Htotal', 8800)
        MemVar('video_input_Hactive', 7680)
        MemVar('video_input_Vtotal', 4500)
        MemVar('video_input_Vactive', 4320)
        MemVar('video_input_refresh_rate', 60)
        MemVar('video_data_width', 20)
        MemVar('video_comp_ratio', lambda: GV.video_data_width/(IF(GV.video_data_width == 20, 11, (IF(GV.video_data_width == 30, 16, 18)))))

        # OSD_input parameter
        MemVar('OSD_input_Htotal', 2200)
        MemVar('OSD_input_Hactive', 1920)
        MemVar('OSD_input_Vtotal', 1125)
        MemVar('OSD_input_Vactive', 1080)
        MemVar('OSD_output_refresh_rate', 120)
        MemVar('OSD_input_refresh_rate', 30)
        MemVar('OSD_data_width', 30)
        MemVar('OSD_alpha_width', 8)
        MemVar('OSD_data_comp_ratio', 1.875)
        MemVar('OSD_alpha_comp_ratio', 2.67)
        MemVar('OSD_Framedelay', 2)

        # dual_cell parameter
        MemVar('dual_cell_Htotal', 4400)
        MemVar('dual_cell_Hactive', 3840)
        MemVar('dual_cell_Vtotal', 2250)
        MemVar('dual_cell_Vactive', 2160)
        MemVar('dual_cell_refresh_rate', 120)

        # MEMC parameter
        MemVar('MEMC_en', lambda: IF(GV.MEMC_mode == 0, 0, 1))
        MemVar('PC_mode', lambda: IF(GV.MEMC_mode == 1, 1, 0))
        MemVar('MEMC_vflip', lambda: GV.MEMC_vfilp)
        MemVar('MC_single_mode', 1)
        MemVar('ME_H_ratio', 8)
        MemVar('ME_V_ratio', 8)
        MemVar('LOGO_MC_ratio_H', 4)
        MemVar('LOGO_MC_ratio_V', 4)
        MemVar('ME1_block_size_H', 16)
        MemVar('ME1_block_size_V', 16)
        MemVar('ME2_block_size_H', 16)
        MemVar('ME2_block_size_V', 16)

        MemVar('MC_H_bits', lambda: GV.MEMC_en*IF(GV.PC_mode, 33, 22))
        MemVar('MC_H_Hact', lambda: GV.video_input_Hactive)
        MemVar('MC_H_Hoverlap', 16)
        MemVar('MC_H_Vtotal', lambda: GV.video_input_Vtotal)
        MemVar('MC_H_Vact', lambda: GV.video_input_Vactive)
        MemVar('MC_H_in_framerate', lambda: GV.video_input_refresh_rate)
        MemVar('MC_H_out_framerate', lambda: GV.output_refresh_rate)
        MemVar('MC_H_buff_num', lambda: IF(GV.PC_mode, IF(GV.MEMC_vflip, 2, 1), IF(GV.MEMC_vflip, 5, 5)))
        MemVar('MC_H_CPR_ratio', 2.2)

        MemVar('MC_L_bits', lambda: GV.MEMC_en*IF(GV.PC_mode, 30, 20))
        MemVar('MC_L_Hact', lambda: GV.video_input_Hactive)
        MemVar('MC_L_Hoverlap', 16)
        MemVar('MC_L_Vtotal', lambda: GV.video_input_Vtotal)
        MemVar('MC_L_Vact', lambda: GV.video_input_Vactive)
        MemVar('MC_L_in_framerate', lambda: GV.video_input_refresh_rate)
        MemVar('MC_L_out_framerate', lambda: GV.output_refresh_rate)
        MemVar('MC_L_buff_num', lambda: IF(GV.PC_mode, IF(GV.MEMC_vflip, 2, 1), IF(GV.MEMC_vflip, 5, 5)))
        MemVar('MC_L_CPR_ratio', 2.2)

        MemVar('ME_bits', lambda: GV.MEMC_en*8*IF(GV.PC_mode, 0, 1))
        MemVar('ME_Hact', lambda: GV.video_input_Hactive/GV.ME_H_ratio)
        MemVar('ME_Hoverlap', 0)
        MemVar('ME_Vtotal', lambda: GV.video_input_Vtotal/GV.ME_V_ratio)
        MemVar('ME_Vact', lambda: GV.video_input_Vactive/GV.ME_V_ratio)
        MemVar('ME_in_framerate', lambda: GV.video_input_refresh_rate)
        MemVar('ME_out_framerate', lambda: GV.output_refresh_rate)
        MemVar('ME_buff_num', 8)
        MemVar('ME_CPR_ratio', 1)

        # TCON
        MemVar('TOP_OD_en', lambda: GV.Top_OD_en)
        MemVar('TOP_Demura_en', lambda: GV.Top_demura_en)
        MemVar('BOT_OD_en', 1)
        MemVar('BOT_Demura_en', lambda: GV.BOT_demura_en)
        MemVar('Demura_ratio', 8)

        MemVar('TOP_OD_bits', lambda: GV.TOP_OD_en*24)
        MemVar('TOP_OD_Hact', lambda: GV.output_Hactive)
        MemVar('TOP_OD_Vtotal', lambda: GV.output_Vtotal)
        MemVar('TOP_OD_Vact', lambda: GV.output_Vactive)
        MemVar('TOP_OD_framerate', lambda: GV.output_refresh_rate)
        MemVar('TOP_OD_CPR_ratio', 5.83*2)

        MemVar('TOP_Demura_bits', lambda: GV.TOP_OD_en*90)
        MemVar('TOP_Demura_Hact', lambda: GV.output_Hactive/GV.Demura_ratio+1)
        MemVar('TOP_Demura_Vtotal', lambda: GV.output_Vtotal/GV.Demura_ratio)
        MemVar('TOP_Demura_Vact', lambda: GV.output_Vactive/GV.Demura_ratio+1)
        MemVar('TOP_Demura_framerate', lambda: GV.output_refresh_rate)
        MemVar('TOP_Demura_CPR_ratio', 1)

        MemVar('BOT_OD_bits', lambda: GV.BOT_OD_en*8)
        MemVar('BOT_OD_Hact', lambda: GV.dual_cell_Hactive)
        MemVar('BOT_OD_Vtotal', lambda: GV.dual_cell_Vtotal)
        MemVar('BOT_OD_Vact', lambda: GV.dual_cell_Vactive)
        MemVar('BOT_OD_framerate', lambda: GV.dual_cell_refresh_rate)
        MemVar('BOT_OD_CPR_ratio', 5.83*2)

        MemVar('BOT_Demura_bits', lambda: GV.BOT_Demura_en*30)
        MemVar('BOT_Demura_Hact', lambda: GV.dual_cell_Hactive/GV.Demura_ratio)
        MemVar('BOT_Demura_Vtotal', lambda: GV.dual_cell_Vtotal/GV.Demura_ratio)
        MemVar('BOT_Demura_Vact', lambda: GV.dual_cell_Vactive/GV.Demura_ratio)
        MemVar('BOT_Demura_framerate', lambda: GV.dual_cell_refresh_rate)
        MemVar('BOT_Demura_CPR_ratio', 1)

        # 3D NR&SR
        MemVar('IIR_en', 1)
        MemVar('IIR_R_frame', 1)
        MemVar('IIR_buff_num', 1)
        MemVar('FIR_R_frame', 5)
        MemVar('FIR_buff_num', 14)
        MemVar('Cadence_en', 0)
        MemVar('capture_w_en', 0)

        # 2D NR
        MemVar('Detect_common', 1)

        # DNN accelerator
        MemVar('DNN_Addr_Interleave', 2)

        MemVar('DDR_frequence', 2133 * 1024 * 1024)
        MemVar('DDR_bit_width', 32 / 8)
        MemVar('DDR_performance', 0.6)
        MemVar('DDR_bandwidth', lambda: GV.DDR_frequence * GV.DDR_bit_width)
        MemVar('DDR_bandwidth_M', lambda: GV.DDR_bandwidth / 1024 / 1024)


class MemVar:
    def __init__(self, name, value=0, var_type=VarType.DEFAULT, digits=-1):
        self._name = name
        self._value = value
        self._digits = digits
        self._lambda = callable(value)
        if var_type == VarType.DEFAULT:
            if isinstance(self._value, float):
                self._type = VarType.FLOAT
            else:
                self._type = VarType.DEC
        else:
            self._type = var_type

        if self._type == VarType.BOOL or self._type == VarType.DEC:
            if self._digits == -1:
                format_str = '%d'
            else:
                format_str = '%%%dd' % self._digits
        elif self._type == VarType.HEX:
            if self._digits == -1:
                format_str = '0x%X'
            else:
                format_str = '0x%%0%dX' % self._digits
        elif self._type == VarType.FLOAT:
            if self._digits == -1:
                format_str = '%.2f'
            else:
                format_str = '%%.%df' % self._digits
        self._format_str = format_str
        MemGlobalVar.add_var(self)

    @property
    def name(self):
        return self._name

    @property
    def value_str(self):
        if self._type == VarType.BOOL:
            return 'True' if self.value else 'False'
        else:
            return self._format_str % self.value

    @property
    def value(self):
        if self._lambda:
            return self._value()
        else:
            return self._value

    @property
    def type(self):
        return self._type

    @value.setter
    def value(self, val):
        self._value = val

    def __str__(self):
        if self._lambda:
            return 'name:%-32s, type:%-6s, value:%s, def:%s' % (self._name, self._type.name, self.value_str, inspect.getsource(self._value))
        else:
            return 'name:%-32s, type:%-6s, value:%s' % (self._name, self._type.name, self.value_str)


GV = MemGlobalVar()
GV.init_vars()


def main():
    MemVar('video_input_Htotal', 8800)
    MemVar('video_input_Hactive', 7680)
    MemVar('video_input_Vtotal', 4500)
    MemVar('video_input_Vactive', 4320)
    MemVar('video_input_refresh_rate', 60)
    MemVar('video_data_width', 20)
    MemVar('video_comp_ratio', lambda: GV.video_data_width/(IF(GV.video_data_width == 20, 11, (IF(GV.video_data_width == 30, 16, 18)))))
    GV.print_vars()
    p_warn('[%s]GV.video_input_refresh_rate: %d' % (GV.current_config, GV.video_input_refresh_rate))

    GV.init_vars()

    GV.set_current_config('1chip2k120hz')
    GV.mod_value('video_input_refresh_rate', 120)
    p_warn('[%s]GV.video_input_refresh_rate: %d' % (GV.current_config, GV.video_input_refresh_rate))
    p_warn('[%s]GV.MC_H_in_framerate:%d' % (GV.current_config, GV.MC_H_in_framerate))

    GV.set_current_config('default')
    p_warn('[%s]GV.MC_H_in_framerate:%d' % (GV.current_config, GV.MC_H_in_framerate))
    p_warn('[%s]GV.video_input_refresh_rate: %d' % (GV.current_config, GV.video_input_refresh_rate))

    GV.set_current_config('1chip2k120hz')
    p_warn('[%s]GV.video_input_refresh_rate: %d' % (GV.current_config, GV.video_input_refresh_rate))
    p_warn('[%s]GV.MC_H_in_framerate:%d' % (GV.current_config, GV.MC_H_in_framerate))


if __name__ == '__main__':
    main()
