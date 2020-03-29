import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mem_config_1chip8k120hz import MemConfig_1Chip8K120Hz
from mem_common import *


def donothing():
    pass


class MainWindow(tk.Frame):
    def __init__(self, master, config):
        self.master = master
        self._config = config
        super().__init__(master)

        self._var_show_read_agent = tk.IntVar()
        self._var_show_read_agent.set(0)
        self._var_show_write_agent = tk.IntVar()
        self._var_show_write_agent.set(1)

        self._mapping = config.place_memory()
        self._init_ui()

        # focus at root node 'Memory'
        if self._tree is not None:
            child_id = self._tree.get_children()[0]
            self._tree.selection_set(child_id)
            self._tree.focus(child_id)
        self.pack()

    def _init_ui(self):
        master = self.master
        self._menu = self._create_menu(master)
        '''
        self._toolbar = tk.Frame(master, bd=1, relief=tk.RAISED)
        self._toolbar.pack(side=tk.TOP, fill=tk.X)
        self._btn_run = tk.Button(self._toolbar, text='run', relief=tk.FLAT, command=self.run)
        self._btn_run.pack(side=tk.LEFT, padx=2, pady=2)

        self._btn_exit = tk.Button(self._toolbar, text='exit', relief=tk.FLAT, command=self.quit)
        self._btn_exit.pack(side=tk.LEFT, padx=2, pady=2)

        self._statusbar = tk.Frame(master, bd=1, relief=tk.RAISED)
        self._statusbar.pack(side=tk.BOTTOM, fill=tk.X)

        self._btn_status = tk.Label(self._statusbar, text='status')
        self._btn_status.pack(side=tk.LEFT, padx=2)
        '''
        self._table_agent = None
        self._screen_width = master.winfo_screenwidth()
        self._screen_height = master.winfo_screenheight()

        self._panel_content = tk.PanedWindow(master, borderwidth=0, orient=tk.HORIZONTAL)
        self._panel_content.pack(fill=tk.BOTH, expand=1)

        self._tree = self._create_treeview(self._panel_content)
        self._panel_content.add(self._tree, width=self._screen_width / 8)

        self._panel_right = tk.PanedWindow(self._panel_content, borderwidth=0, orient=tk.VERTICAL)
        self._panel_content.add(self._panel_right)

        """
        self._panel_top = tk.PanedWindow(self._panel_content, borderwidth=0, orient=tk.HORIZONTAL)
        self._panel_content.add(self._panel_top, height=self._screen_height / 4 * 3)

        self._panel_bottom = tk.PanedWindow(self._panel_content, borderwidth=0, orient=tk.HORIZONTAL)
        self._panel_content.add(self._panel_top, height=self._screen_height / 4)

        # self._panel_top = self._create_panel_top()
        
        self._notebook = self._create_notebook(self._panel_content)
        self._panel_content.add(self._notebook, width=self._screen_width / 8 * 4)

        self._canvas = tk.Canvas(self._panel_content, bg='grey')
        self._panel_content.add(self._canvas, width=self._screen_width / 8 * 3)
        """

    def _create_treeview(self, master):
        tree = ttk.Treeview(master, show='tree', selectmode='browse')
        tree.insert('', 'end', 'Memory', text='Memory')

        tree.insert('Memory', 'end', 'DDR1', text='DDR1')
        tree.insert('Memory', 'end', 'DDR2', text='DDR2')
        tree.insert('Memory', 'end', 'DDR3', text='DDR3')
        tree.insert('Memory', 'end', 'DDR4', text='DDR4')

        for i, agents in enumerate(self._mapping):
            node = 'DDR%d' % (i+1)
            for agent in agents:
                if agent.unused:
                    continue
                tree.insert(node, 'end', agent.name, text=agent.name)

        tree.item('Memory', open=True)

        tree.bind('<<TreeviewSelect>>', self._on_agent_tree_select)

        return tree

    def _create_notebook(self, master):
        notebook = ttk.Notebook(master)

        frame = self._create_table_frame(notebook)
        notebook.add(frame, text='Memory Layour')

        frame = self._create_chart_frame(notebook)
        notebook.add(frame, text='Bandwidth Usage')

        frame = self._create_regiser_frame(notebook)
        notebook.add(frame, text='Registers')

        return notebook

    def _create_table_frame(self, master):
        frame = ttk.Frame(master, relief=tk.FLAT)

        table_agent = ttk.Treeview(frame, show='headings',
                                   columns=['NO', 'name', 'rw', 'ip', 'start_addr', 'end_addr', 'size', 'bandwidth'])
        self._table_agent = table_agent
        table_agent.pack(fill=tk.BOTH, expand=1)
        table_agent.heading('NO', text='NO')
        table_agent.heading('name', text='Agent Name')
        table_agent.heading('rw', text='R/W')
        table_agent.heading('ip', text='IP')
        table_agent.heading('start_addr', text='Start Address')
        table_agent.heading('end_addr', text='End Address')
        table_agent.heading('size', text='Size(M)')
        table_agent.heading('bandwidth', text='bandwidth(M)')

        table_agent.column('NO', width=1, anchor='e')
        table_agent.column('name', width=80, anchor='w')
        table_agent.column('ip', width=80, anchor='w')
        table_agent.column('rw', width=1, anchor='w')
        table_agent.column('start_addr', width=40, anchor='e')
        table_agent.column('end_addr', width=40, anchor='e')
        table_agent.column('size', width=40, anchor='e')
        table_agent.column('bandwidth', width=40, anchor='e')

        table_agent.insert('', 'end', text='KMC_0', values=('1', 'KMC_0', 'TCON', 'W', '0x10000000', '0x10004000', '0.64M', '1.5M'))
        return frame, table_agent

    def _create_chart_frame(self, master):
        frame = ttk.Frame(master, relief=tk.FLAT)
        fig = Figure(figsize=(5, 5), dpi=100)
        plt = fig.add_subplot(111)
        plt.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 1, 3, 8, 9, 3, 5])
        canvas = FigureCanvasTkAgg(fig, frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        return frame

    def _create_regiser_frame(self, master):
        frame = ttk.Frame(master, relief=tk.FLAT)
        return frame

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
                                 command=lambda: self._on_agent_tree_select(None))
        viewmenu.add_checkbutton(label='Show write agent', var=self._var_show_write_agent,
                                 command=lambda: self._on_agent_tree_select(None))
        menubar.add_cascade(label='View', menu=viewmenu)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label='Help Index', command=donothing)
        helpmenu.add_command(label='About...', command=donothing)
        menubar.add_cascade(label='Help', menu=helpmenu)

        self.master.config(menu=menubar)
        return menubar

    def _on_agent_tree_select(self, event):
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
            agent = self._config.get_agent(selection)
            assert agent is not None
        table = self._table_agent

        table.delete(*table.get_children())
        number = 0
        for agent in self._config.agent_list:
            if agent.unused:
                continue
            if ddr_tag == DDRTag.NONE or ddr_tag == agent.ddr_tag:
                if agent.ddr_op == DDROp.W and self._var_show_write_agent.get() == 1:
                    assert agent.start_addr is not None
                    table.insert('', 'end', text=agent.name, values=(
                        str(number), agent.name, agent.op_str, agent.block_name,
                        '0x%08X' % agent.start_addr,
                        '0x%08X' % agent.end_addr,
                        '%.2fM' % agent.size_m,
                        '%.2fM' % agent.bandwidth_m))
                    number += 1
                elif agent.ddr_op == DDROp.R and self._var_show_read_agent.get() == 1:
                    table.insert('', 'end', text=agent.name, values=(
                        str(number), agent.name, agent.op_str, agent.block_name,
                        '',
                        '',
                        '',
                        '%.2fM' % agent.bandwidth_m))
                    number += 1

    def run(self):
        pass


def main():
    root = tk.Tk()
    config = MemConfig_1Chip8K120Hz()
    root.state('zoomed')
    root.title('Memory Mapping Tool')
    MainWindow(root, config)
    root.mainloop()


if __name__ == '__main__':
    main()
