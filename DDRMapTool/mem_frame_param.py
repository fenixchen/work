import tkinter as tk
from tkinter import ttk
from mem_common import *
from mem_global_var import GV


class MemFrameParam(tk.Frame):
    def __init__(self, master, config_list):
        self._master = master
        self._config_list = config_list
        super().__init__(master)
        self._table_param = self._create_table_param(self)
        self._table_param.pack(fill=tk.BOTH, expand=1)

    def _create_table_param(self, master):
        columns = ['NO', 'parameter', 'type']
        for i in range(len(self._config_list)):
            columns.append('system:%d' % i)
        table = ttk.Treeview(master, show='headings', columns=columns)

        table.heading('NO', text='NO')
        table.heading('parameter', text='Parameter')
        table.heading('type', text='Type')

        table.column('NO', width=40, anchor='e', stretch=tk.NO)
        table.column('parameter', width=100, anchor='w')
        table.column('type', width=60, anchor='w', stretch=tk.NO)
        for i in range(len(self._config_list)):
            system = 'system:%d' % i
            table.heading(system, text=self._config_list[i].name)
            table.column(system, width=100, anchor='e')

        index = 0

        row_values = [[str(i), var.name, var.type.name] for i, var in enumerate(GV.var_dict.values())]

        for config in self._config_list:
            assert config.name in GV.config_list
            GV.set_current_config(config.name)
            for i, var in enumerate(GV.var_dict.values()):
                row_values[i].append(var.value_str)

        for row in row_values:
            all_same = len(set(row[3:])) == 1
            tag = 'same' if all_same else 'diff'
            table.insert('', 'end', text=row[0], values=row, tag=tag)

        table.tag_configure('same', foreground='black', background='white')
        table.tag_configure('diff', foreground='black', background='tomato')
        return table
