import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mem_common import *

TREEVIEW_ROW_HEIGHT = 24
DRAW_PADDING = 10


class MemFrameConfig(tk.Frame):
    def __init__(self, master, config):
        self._master = master
        self._config = config
        self._top_agent_item = None
        super().__init__(master)

        self._agent_item_list = []
        self._mapping = config.place_memory()
        self._init_ui(self)

    def _init_ui(self, master):
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()

        self._panel_right = tk.PanedWindow(master, borderwidth=0, orient=tk.VERTICAL)
        self._panel_right.pack(fill=tk.BOTH, expand=1)

        self._panel_top = tk.PanedWindow(self._panel_right, borderwidth=0, orient=tk.HORIZONTAL, handlesize=1)
        self._panel_right.add(self._panel_top, height=screen_height / 5 * 3)

        self._panel_bottom = tk.PanedWindow(self._panel_right, borderwidth=0, orient=tk.HORIZONTAL)
        self._panel_right.add(self._panel_bottom)

        panel_width = screen_width / 8 * 7
        self._table_agent = self._create_table_agent(master)
        self._panel_top.add(self._table_agent, width=panel_width / 8 * 5)
        self._table_agent.bind('<<TreeviewSelect>>', self._on_agent_changed)

        self._canvas = tk.Canvas(self._panel_top, bg='white', borderwidth=0)
        self._panel_top.add(self._canvas, width=panel_width / 8 * 3)

        self._frame_register, self._table_regiser = self._create_table_register(self._panel_bottom)
        self._panel_bottom.add(self._frame_register, width=panel_width / 2)

        self._frame_chart = self._create_chart_frame(self._panel_bottom)
        self._panel_bottom.add(self._frame_chart, width=panel_width / 2)

    def _create_table_agent(self, master):
        table = ttk.Treeview(master, show='headings',
                             columns=['NO', 'name', 'rw', 'ddr', 'ip', 'start_addr', 'end_addr', 'size', 'bandwidth'],
                             yscrollcommand=self._on_y_scroll)
        table.pack(fill=tk.BOTH, expand=1)
        table.heading('NO', text='NO')
        table.heading('name', text='Agent Name')
        table.heading('rw', text='R/W')
        table.heading('ddr', text='DDR')
        table.heading('ip', text='IP')
        table.heading('start_addr', text='Start Address')
        table.heading('end_addr', text='End Address')
        table.heading('size', text='Size(M)')
        table.heading('bandwidth', text='bandwidth(M)')

        table.column('NO', width=5, anchor='e')
        table.column('name', width=100, anchor='w')
        table.column('rw', width=5, anchor='w')
        table.column('ddr', width=5, anchor='w')
        table.column('ip', width=100, anchor='w')
        table.column('start_addr', width=30, anchor='e')
        table.column('end_addr', width=30, anchor='e')
        table.column('size', width=30, anchor='e')
        table.column('bandwidth', width=40, anchor='e')

        return table

    def _on_y_scroll(self, *args):
        top_item = None
        for agent_item in self._agent_item_list:
            bbox = self._table_agent.bbox(agent_item, column=0)
            if bbox:
                top_item = agent_item
                break
        if top_item != self._top_agent_item:
            self._top_agent_item = top_item
            self._draw_agent_memory()

    def _create_table_register(self, master):
        frame = tk.LabelFrame(master, text="Agent Registers")

        table = ttk.Treeview(frame, show='headings', columns=['NO', 'name', 'address', 'value'])
        table.pack(fill=tk.BOTH, expand=1)

        table.heading('NO', text='NO')
        table.heading('name', text='Register Name')
        table.heading('address', text='Address')
        table.heading('value', text='Value')

        table.column('NO', width=1, anchor='e')
        table.column('name', width=80, anchor='w')
        table.column('address', width=80, anchor='e')
        table.column('value', width=80, anchor='e')

        return frame, table

    def _create_chart_frame(self, master):
        frame = ttk.LabelFrame(master, text='Statistics', relief=tk.FLAT)
        return frame

    def on_ddr_changed(self, ddr_tag, show_read_agent, show_right_agent):
        table = self._table_agent
        table.delete(*table.get_children())
        number = 0
        self._agent_item_list = []
        for agent in self._config.agent_list:
            if agent.unused:
                continue
            if ddr_tag == DDRTag.NONE or ddr_tag == agent.ddr_tag:
                if agent.ddr_op == DDROp.W and show_right_agent:
                    assert agent.start_addr is not None
                    iid = table.insert('', 'end', text=agent.name, values=(
                        str(number), agent.name, agent.op_str, agent.ddr_tag.name, agent.block_name,
                        '0x%08X' % agent.start_addr,
                        '0x%08X' % agent.end_addr,
                        '%.2fM' % agent.size_m,
                        '%.2fM' % agent.bandwidth_m))
                    number += 1
                    self._agent_item_list.append(iid)
                elif agent.ddr_op == DDROp.R and show_read_agent:
                    iid = table.insert('', 'end', text=agent.name, values=(
                        str(number), agent.name, agent.op_str, agent.ddr_tag.name, agent.block_name,
                        '',
                        '',
                        '',
                        '%.2fM' % agent.bandwidth_m))
                    number += 1
                    self._agent_item_list.append(iid)
        if self._agent_item_list:
            self._top_agent_item = self._agent_item_list[0]
        else:
            self._top_agent_item = None
        table.update()
        self._draw_agent_memory()
        self._plot_chart(ddr_tag)

    def _draw_agent_memory(self):

        canvas = self._canvas
        canvas.delete("all")
        canvas_width = canvas.winfo_width()
        canvas_height = canvas.winfo_height()
        canvas.create_text(canvas_width / 2, TREEVIEW_ROW_HEIGHT / 2,
                           justify=tk.CENTER,
                           text='DDR_SIZE:%dM' % DDR_SIZE)
        for agent_item in self._agent_item_list:
            if agent_item < self._top_agent_item:
                continue
            bbox = self._table_agent.bbox(agent_item, column=0)
            if not bbox:
                continue
            agent = self._config.get_agent(self._table_agent.item(agent_item)['text'])
            if agent.ddr_op == DDROp.R:
                continue
            left = DRAW_PADDING
            top = bbox[1] + 2
            right = canvas_width - DRAW_PADDING
            bottom = bbox[1] + bbox[3] - 2
            if bottom < canvas_height:
                canvas.create_rectangle(left, top, right, bottom)
            else:
                break
            width_total = right - left
            fill_left = int(agent.start_addr / float(DDR_SIZE_BYTE) * width_total)
            fill_right = int(agent.end_addr / float(DDR_SIZE_BYTE) * width_total)
            ddr_color = ['red', 'green', 'blue', 'yellow']
            canvas.create_rectangle(fill_left + DRAW_PADDING, top, fill_right + DRAW_PADDING,
                                    bottom, fill=ddr_color[agent.ddr_tag.value])

    def _plot_chart(self, ddr_tag):
        for widget in self._frame_chart.winfo_children():
            widget.destroy()

        fig = Figure(figsize=(5, 5), dpi=100)

        labels = 'Used', 'Unused'
        usage = self._config.calc_memory_usage(ddr_tag)
        explode = (0.1, 0)
        plt = fig.add_subplot(121)
        plt.set_title('%s Memory' % ('TOTAL' if ddr_tag == DDRTag.NONE else ddr_tag.name))
        plt.pie(usage, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)

        labels = 'Used', 'Unused'
        usage = self._config.calc_bandwidth_usage(ddr_tag)
        explode = (0.1, 0)
        plt = fig.add_subplot(122)
        plt.set_title('%s Bandwidth' % ('TOTAL' if ddr_tag == DDRTag.NONE else ddr_tag.name))
        plt.pie(usage, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)

        canvas = FigureCanvasTkAgg(fig, self._frame_chart)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def _on_agent_changed(self, event):
        selection = None
        for item in self._table_agent.selection():
            selection = self._table_agent.item(item, 'text')
            break
        if selection is None:
            return
        agent = self._config.get_agent(selection)

        assert agent is not None
        table = self._table_regiser
        table.delete(*table.get_children())
        number = 1
        for reg in agent.registers:
            table.insert('', 'end', text=reg.name, values=(
                str(number),
                reg.name,
                reg.addr_str,
                '0x%08X' % reg.value))
            number += 1
