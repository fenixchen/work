import tkinter as tk
from tkinter import ttk


def donothing():
    pass


class MainWindow(tk.Frame):
    def __init__(self, master):
        self.master = master
        tk.Frame.__init__(self, master)
        self.pack()

        self.tree = ttk.Treeview(self)
        self.tree.pack(side=tk.LEFT, fill=tk.Y)

        self.notebk = ttk.Notebook(self)
        self.notebk.pack(side='top', fill='y', expand=True)

        self.frame1 = ttk.Frame(self.notebk, relief=tk.SUNKEN)
        self.frame2 = ttk.Frame(self.notebk, relief=tk.SUNKEN)
        self.frame3 = ttk.Frame(self.notebk, relief=tk.SUNKEN)

        self.notebk.add(self.frame1, text='Memory Size')
        self.notebk.add(self.frame2, text='Write Bandwidth')
        self.notebk.add(self.frame3, text='Read Bandwidth')
        self.create_menu()

    def create_menu(self):
        menubar = tk.Menu(self)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=donothing)
        filemenu.add_command(label="Open", command=donothing)
        filemenu.add_command(label="Save", command=donothing)
        filemenu.add_command(label="Save as...", command=donothing)
        filemenu.add_command(label="Close", command=donothing)
        filemenu.add_separator()

        filemenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=donothing)
        helpmenu.add_command(label="About...", command=donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)

        self.master.config(menu=menubar)


def main():
    root = tk.Tk()
    root.state('zoomed')
    root.title("Memory Mapping Tool")
    MainWindow(root)
    root.mainloop()


if __name__ == '__main__':
    main()
