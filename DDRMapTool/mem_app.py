import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
import matplotlib
from mem_config_1chip8k120hz import MemConfig_1Chip8K120Hz

matplotlib.use("TkAgg")


def donothing():
    pass


class MainWindow(tk.Frame):
    def __init__(self, master, config):
        self.master = master
        self._config = config
        super().__init__(master)
        self._menu = self.create_menu()
        self._mapping = config.place_memory()
        self._init_ui()
        self.pack()

    def _init_ui(self):
        master = self.master

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

        self._canvas = tk.Canvas(master, width=600, bg="white")
        self._canvas.pack(side=tk.RIGHT, fill=tk.Y)

        self._panel_content = tk.PanedWindow(master, borderwidth=0)
        self._panel_content.pack(fill=tk.BOTH, expand=1)

        self._tree = self._create_treeview(self._panel_content)

        self._notebook = self._create_notebook(self._panel_content)

    def _on_agent_tree_select(self, event):
        for item in self._tree.selection():
            item_text = self._tree.item(item, "text")
            print(item_text)

    def _create_treeview(self, master):
        tree = ttk.Treeview(master, show="tree", selectmode="browse")
        master.add(tree)
        tree.insert('', 'end', 'Memory', text='Memory')

        tree.insert('Memory', 'end', 'DDR1', text='DDR1')
        tree.insert('Memory', 'end', 'DDR2', text='DDR2')
        tree.insert('Memory', 'end', 'DDR3', text='DDR3')
        tree.insert('Memory', 'end', 'DDR4', text='DDR4')

        for i, agents in enumerate(self._mapping):
            node = "DDR%d" % (i+1)
            for agent in agents:
                if agent.unused:
                    continue
                tree.insert(node, 'end', agent.name, text=agent.name)

        tree.item("Memory", open=True)

        tree.bind('<<TreeviewSelect>>', self._on_agent_tree_select)
        #tree.item("DDR1", open=True)
        #tree.item("DDR2", open=True)
        #tree.item("DDR3", open=True)
        #tree.item("DDR4", open=True)
        return tree

    def _create_notebook(self, master):

        notebook = ttk.Notebook(master)
        master.add(notebook)

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
                                   columns=['name', "start_addr", "end_addr", "size"])
        table_agent.pack(fill=tk.BOTH, expand=1)
        table_agent.heading('name', text='Agent Name')
        table_agent.heading('start_addr', text='Start Address')
        table_agent.heading('end_addr', text='End Address')
        table_agent.heading('size', text='Size(M)')

        table_agent.column('name', width=50, anchor='w')
        table_agent.column('start_addr', width=50, anchor='e')
        table_agent.column('end_addr', width=50, anchor='e')
        table_agent.column('size', width=50, anchor='e')

        table_agent.insert('', 'end', text='KMC_0', values=('KMC_0', '0x10000000', '0x10004000', '0.64M'), tag='gray')
        table_agent.insert('', 'end', text='KMC_1', values=('KMC_1', '0x10000000', '0x10004000', '0.64M'), tag='white')
        table_agent.insert('', 'end', text='KMC_2', values=('KMC_0', '0x10000000', '0x10004000', '0.64M'), tag='gray')
        table_agent.insert('', 'end', text='KMC_3', values=('KMC_1', '0x10000000', '0x10004000', '0.64M'), tag='white')
        table_agent.tag_configure('gray', background='#cccccc')
        table_agent.tag_configure('white', background='#ffffff')
        return frame

    def _create_chart_frame(self, master):
        frame = ttk.Frame(master, relief=tk.FLAT)
        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 1, 3, 8, 9, 3, 5])
        canvas = FigureCanvasTkAgg(f, frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        return frame

    def _create_regiser_frame(self, master):
        frame = ttk.Frame(master, relief=tk.FLAT)
        return frame

    def create_menu(self):
        menubar = tk.Menu(self)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=donothing)
        filemenu.add_command(label="Open", command=donothing)
        filemenu.add_command(label="Save", command=donothing)
        filemenu.add_command(label="Save as...", command=donothing)
        filemenu.add_command(label="Close", command=donothing)
        filemenu.add_separator()

        filemenu.add_command(label="Exit", command=self.master.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=donothing)
        helpmenu.add_command(label="About...", command=donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)

        self.master.config(menu=menubar)
        return menubar

    def run(self):
        pass


def main():
    root = tk.Tk()
    config = MemConfig_1Chip8K120Hz()
    root.state('zoomed')
    root.title("Memory Mapping Tool")
    MainWindow(root, config)
    root.mainloop()


if __name__ == '__main__':
    main()
