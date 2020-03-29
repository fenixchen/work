import tkinter as tk
from tkinter import ttk
from mem_frame_config import MemFrameConfig, TREEVIEW_ROW_HEIGHT
from mem_config_1chip8k120hz import MemConfig_1Chip8K120Hz
from mem_config_1chip4k120hz import MemConfig_1Chip4K120Hz
from mem_common import *


def donothing():
    pass


class MemMainWindow(tk.Frame):
    def __init__(self, master, config_list):
        self.master = master
        self._config_list = config_list

        super().__init__(master)
        ttk.Style().configure('Treeview', rowheight=TREEVIEW_ROW_HEIGHT)

        self._var_show_read_agent = tk.IntVar()
        self._var_show_read_agent.set(0)
        self._var_show_write_agent = tk.IntVar()
        self._var_show_write_agent.set(1)

        self._menu = self._create_menu(master)

        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()

        self._panel_content = tk.PanedWindow(master, borderwidth=0, orient=tk.HORIZONTAL)
        self._panel_content.pack(fill=tk.BOTH, expand=1)

        self._tree = self._create_treeview(self._panel_content)
        self._panel_content.add(self._tree, width=screen_width / 10)
        self._tree.bind('<<TreeviewSelect>>', self._on_ddr_tree_select)

        self._notebook = ttk.Notebook(master, padding=0)
        self._panel_content.add(self._notebook)

        self._notebook.bind('<<NotebookTabChanged>>', self._on_config_table_changed)

        self._config_frame_list = []
        for config in self._config_list:
            frame = MemFrameConfig(self._notebook, config)
            self._notebook.add(frame, text=config.name)
            self._config_frame_list.append(frame)

        self._current_config_frame = self._config_frame_list[0]

        # focus at root node 'Memory'
        if self._tree is not None:
            child_id = self._tree.get_children()[0]
            self._tree.selection_set(child_id)
            self._tree.focus(child_id)

        self.pack()

    def _create_treeview(self, master):
        tree = ttk.Treeview(master, show='tree', selectmode='browse')
        tree.insert('', 'end', 'Memory', text='Memory')

        tree.insert('Memory', 'end', 'DDR1', text='DDR1')
        tree.insert('Memory', 'end', 'DDR2', text='DDR2')
        tree.insert('Memory', 'end', 'DDR3', text='DDR3')
        tree.insert('Memory', 'end', 'DDR4', text='DDR4')
        tree.item('Memory', open=True)
        return tree

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
        self._current_config_frame.on_ddr_changed(ddr_tag,
                                                  self._var_show_read_agent.get() == 1,
                                                  self._var_show_write_agent.get() == 1)

    def _on_config_table_changed(self, event):
        self._current_config_frame = self._config_frame_list[self._notebook.index("current")]
        self._on_ddr_tree_select(None)

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


def main():
    root = tk.Tk()
    root.state('zoomed')
    root.title('Memory Mapping Tool')
    MemMainWindow(root, [
        MemConfig_1Chip8K120Hz(),
        MemConfig_1Chip4K120Hz()])
    root.mainloop()


if __name__ == '__main__':
    main()
