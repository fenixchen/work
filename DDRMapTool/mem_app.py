import tkinter as tk
from tkinter import ttk
from mem_frame_config import MemFrameConfig, TREEVIEW_ROW_HEIGHT, DRAW_PADDING
from mem_config_1chip8k120hz import MemConfig_1Chip8K120Hz
from mem_config_1chip8k60hz import MemConfig_1Chip8K60Hz
from mem_common import *
from random_color import RandomColor
from mem_frame_param import MemFrameParam
from mem_global_var import GV


def donothing():
    pass


class MemMainWindow(tk.Frame):
    def __init__(self, master, config_list):
        self.master = master
        self._config_list = config_list

        super().__init__(master)
        ttk.Style().configure('Treeview', rowheight=TREEVIEW_ROW_HEIGHT)
        self._current_agent = None

        self._var_show_read_agent = tk.IntVar()
        self._var_show_read_agent.set(0)
        self._var_show_write_agent = tk.IntVar()
        self._var_show_write_agent.set(1)

        self._menu = self._create_menu(master)

        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()

        self._canvas = tk.Canvas(master, bg='white', borderwidth=0, height=50)
        self._canvas.pack(expand=False, fill=tk.X, side='bottom')
        self._canvas.bind('<Button-1>', self._on_canvas_click)

        self._panel_content = tk.PanedWindow(master, borderwidth=0, orient=tk.HORIZONTAL)
        self._panel_content.pack(fill=tk.BOTH, expand=1)

        self._tree = self._create_treeview(self._panel_content)
        self._panel_content.add(self._tree, width=screen_width / 8)
        self._tree.bind('<<TreeviewSelect>>', self._on_ddr_tree_select)

        self._notebook = ttk.Notebook(master, padding=0)
        self._panel_content.add(self._notebook)

        self._notebook.bind('<<NotebookTabChanged>>', self._on_config_table_changed)

        self._config_frame_list = []

        self._frame_param = MemFrameParam(self._notebook, config_list)
        self._notebook.add(self._frame_param, text='System Parameters')

        for config in self._config_list:
            frame = MemFrameConfig(self._notebook, self, config)
            self._notebook.add(frame, text=config.name)
            self._config_frame_list.append(frame)

        self._current_config_frame = None

        # focus at root node 'Memory'
        if self._tree is not None:
            child_id = self._tree.get_children()[0]
            self._tree.selection_set(child_id)
            self._tree.focus(child_id)

        self._canvas.bind("<Configure>", self._on_canvas_resize)
        self.pack()
        master.update()

    def _on_canvas_click(self, event):
        if not self._current_config_frame:
            return
        canvas = self._canvas
        canvas_width = canvas.winfo_width()
        canvas_height = canvas.winfo_height()
        left = DRAW_PADDING
        top = 20
        right = canvas_width - DRAW_PADDING
        bottom = canvas_height - 10
        width_total = right - left
        config = self._current_config_frame.config
        for agent in config.agent_list:
            if not agent.allocated or agent.ddr_op == DDROp.R:
                continue
            fill_left = int(agent.absolute_start_addr / float(GV.DDR_size_byte * GV.DDR_count) * width_total)
            fill_right = int(agent.absolute_end_addr / float(GV.DDR_size_byte * GV.DDR_count) * width_total)
            if fill_left + DRAW_PADDING <= event.x <= fill_right + DRAW_PADDING and top <= event.y <= bottom:
                self._current_config_frame.select_agent(agent)

    def _on_canvas_resize(self, event):
        canvas = self._canvas
        canvas.delete("all")
        canvas_width = canvas.winfo_width()
        canvas_height = canvas.winfo_height()
        left = DRAW_PADDING
        top = 20
        right = canvas_width - DRAW_PADDING
        bottom = canvas_height - 10
        canvas.create_rectangle(left, top, right, bottom, fill='white')

        if not self._current_config_frame:
            return

        config = self._current_config_frame.config
        write_agent_count = config.write_agent_count
        color = RandomColor(write_agent_count)

        width_total = right - left
        index = 0
        for agent in config.agent_list:
            if not agent.allocated or agent.ddr_op == DDROp.R:
                continue
            fill_left = int(agent.absolute_start_addr / float(GV.DDR_size_byte * GV.DDR_count) * width_total)
            fill_right = int(agent.absolute_end_addr / float(GV.DDR_size_byte * GV.DDR_count) * width_total)
            if agent == self._current_agent:
                fill_color = 'red'
            else:
                fill_color = color.get_color(index)
            canvas.create_rectangle(fill_left + DRAW_PADDING, top, fill_right + DRAW_PADDING, bottom, fill=fill_color)
            index += 1

        memory_unit = 64
        for i in range(0, GV.DDR_size * GV.DDR_count + 1, memory_unit):
            draw_line_x = int(i / float(GV.DDR_size * GV.DDR_count) * width_total)
            canvas.create_line(draw_line_x + DRAW_PADDING, 0, draw_line_x + DRAW_PADDING, canvas_height, dash=(1, 1))
            canvas.create_text(draw_line_x + DRAW_PADDING, 0, text='%dM' % i, font=("arial", 8), anchor='n')

    def _create_treeview(self, master):
        tree = ttk.Treeview(master, show='tree', selectmode='browse')
        tree.insert('', 'end', 'Memory', text='Memory')

        tree.insert('Memory', 'end', 'DDR1', text='DDR1')
        tree.insert('Memory', 'end', 'DDR2', text='DDR2')
        tree.insert('Memory', 'end', 'DDR3', text='DDR3')
        tree.insert('Memory', 'end', 'DDR4', text='DDR4')
        tree.item('Memory', open=True)
        return tree

    def on_agent_select(self, agent):
        self._current_agent = agent
        self._on_canvas_resize(None)

    def _on_ddr_tree_select(self, event):
        tree = self._tree
        selection = None
        ddr_tag = DDRTag.NONE
        for item in tree.selection():
            selection = tree.item(item, 'text')
            break
        if selection is None:
            return
        if selection == 'Memory':
            ddr_tag = DDRTag.NONE
        elif selection in ['DDR1', 'DDR2', 'DDR3', 'DDR4']:
            ddr_tag = DDRTag(int(selection[-1]) - 1)
        else:
            assert False
        if self._current_config_frame:
            self._current_config_frame.on_ddr_changed(ddr_tag,
                                                      self._var_show_read_agent.get() == 1,
                                                      self._var_show_write_agent.get() == 1)

    def _on_config_table_changed(self, event):
        self._current_agent = None
        index = self._notebook.index("current")
        if index > 0:
            self._current_config_frame = self._config_frame_list[index - 1]
            self._on_ddr_tree_select(None)
        else:
            self._current_config_frame = None
        self._on_canvas_resize(None)

    def _create_menu(self, master):
        menubar = tk.Menu(master)
        filemenu = tk.Menu(menubar, tearoff=0)
        # filemenu.add_command(label='New', command=donothing)
        # filemenu.add_command(label='Open', command=donothing)
        # filemenu.add_command(label='Save', command=donothing)
        # filemenu.add_command(label='Save as...', command=donothing)
        # filemenu.add_command(label='Close', command=donothing)
        filemenu.add_separator()

        filemenu.add_command(label='Exit', command=self.master.quit)
        menubar.add_cascade(label='File', menu=filemenu)

        viewmenu = tk.Menu(menubar, tearoff=0)
        viewmenu.add_checkbutton(label='Show read agent', var=self._var_show_read_agent,
                                 command=lambda: self._on_ddr_tree_select(None))
        viewmenu.add_checkbutton(label='Show write agent', var=self._var_show_write_agent,
                                 command=lambda: self._on_ddr_tree_select(None))
        menubar.add_cascade(label='View', menu=viewmenu)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label='Help Index', command=donothing)
        helpmenu.add_command(label='About...', command=donothing)
        menubar.add_cascade(label='Help', menu=helpmenu)

        self.master.config(menu=menubar)
        return menubar


GLOBAL_STYLE = None


def main():
    root = tk.Tk()
    root.state('zoomed')
    root.title('Memory Mapping Tool')

    global GLOBAL_STYLE
    GLOBAL_STYLE = ttk.Style()
    GLOBAL_STYLE.map('Treeview', foreground=fixed_map('foreground'), background=fixed_map('background'))

    MemMainWindow(root, [
        MemConfig_1Chip8K120Hz(),
        MemConfig_1Chip8K60Hz()])
    root.mainloop()


def fixed_map(option):
    # Fix for setting text colour for Tkinter 8.6.9
    # From: https://core.tcl.tk/tk/info/509cafafae
    #
    # Returns the style map for 'option' with any styles starting with
    # ('!disabled', '!selected', ...) filtered out.

    # style.map() returns an empty list for missing options, so this
    # should be future-safe.
    return [elm for elm in GLOBAL_STYLE.map('Treeview', query_opt=option) if
            elm[:2] != ('!disabled', '!selected')]


if __name__ == '__main__':

    main()
