from tkinter import *
from tkinter.filedialog import asksaveasfile
from tkinter import filedialog as fd, messagebox
from tkinter.messagebox import showinfo
from tkinter import simpledialog

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from DiGraph import DiGraph
from draw_graph import DrawGraph


class Gui:
    def __init__(self, graph_algo):
        self.root = Tk()
        self.root.wm_title("Graph")
        self.root.geometry("800x600")
        self.root.state("zoomed")
        self.algo = graph_algo
        self._init_menu()
        self.canvas = None
        self.d_g = DrawGraph(self.algo.get_graph())
        self.fig = self.d_g.draw_graph()

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)  # A tk.DrawingArea.

        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        self.canvas.draw()

        self.root.mainloop()

    def reload_graph(self):
        self.d_g.reload(self.algo.get_graph())
        self.canvas.draw()

    def _init_menu(self):
        my_menu = Menu(self.root)
        self.root.config(menu=my_menu)

        # create a menu
        file_menu = Menu(my_menu, tearoff=0)
        my_menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Load Graph", command=self.load_file)
        file_menu.add_command(label="Save Graph", command=self.save)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

        graph_menu = Menu(my_menu, tearoff=0)
        my_menu.add_cascade(label="Graph", menu=graph_menu)
        graph_menu.add_command(label="Clear Marked Edges", command=self.clear_marked_edges)

        algorithm_menu = Menu(my_menu, tearoff=0)
        my_menu.add_cascade(label="Algorithms", menu=algorithm_menu)
        algorithm_menu.add_command(label="Shortest Path", command=self.shortest_path)
        algorithm_menu.add_command(label="Center", command=self.center)
        algorithm_menu.add_command(label="TSP", command=self.tsp)

    def save(self):
        files = [('Json Files', '*.json')]
        file = asksaveasfile(filetypes=files, defaultextension=files, initialdir='.')

        if file:
            self.algo.save_to_json(file)

    def load_file(self):
        filetypes = [('Json Files', '*.json')]

        file = fd.askopenfilename(
            title='Open a file',
            initialdir='.',
            filetypes=filetypes)

        if file:
            self.algo.load_from_json(file)
            self.d_g.clear_marked()
            self.reload_graph()

    def clear_marked_edges(self):
        self.d_g.clear_marked()
        self.reload_graph()

    def shortest_path(self):
        answer = simpledialog.askstring("Shortest path", "Write the source node and the destination node with one space between them",
                                        parent=self.root)
        if answer:
            l = answer.split(" ")
            if len(l) != 2:
                messagebox.showerror("Wrong input", "Choose source and destination node")
                return
            try:
                src = int(l[0])
                dst = int(l[1])
            except ValueError:
                messagebox.showerror("Wrong input", "Choose source and destination node")
                return

            if self.algo.get_graph().get_all_v().get(src) is None or self.algo.get_graph().get_all_v().get(dst) is None:
                messagebox.showerror("Wrong input", "Nodes don't exist on the graph")
                return
            r = self.algo.shortest_path(src, dst)

            l = []
            for i in range(len(r[1])-1):
                src = r[1][i]
                dst = r[1][i+1]
                l.append((src,dst))

            self.d_g.marked_e = l
            self.reload_graph()

            showinfo(
                title='shorted Path',
                message='The length is: ' + str(r[0])
            )

    def center(self):
        r = self.algo.centerPoint()
        showinfo(
            title='center',
            message=f'The center is: {r[0]} \nlen: {r[1]}'
        )

    def tsp(self):
        answer = simpledialog.askstring("TSP",
                                        "Write the wanted nodes with one space between them",
                                        parent=self.root)
        if answer:
            l = answer.split(" ")
            if len(l) < 2:
                messagebox.showerror("Wrong input", "Choose at least 2 nodes")
                return
            try:
                nodes = [int(v) for v in l]
            except ValueError:
                messagebox.showerror("Wrong input", "Choose source and destination node")
                return

            for n in nodes:
                if self.algo.get_graph().get_all_v().get(n) is None:
                    messagebox.showerror("Wrong input", "Nodes don't exist on the graph")
                    return

            r = self.algo.TSP(nodes)

            l = []
            for i in range(len(r[0]) - 1):
                src = r[0][i]
                dst = r[0][i + 1]
                l.append((src, dst))

            self.d_g.marked_e = l
            self.reload_graph()

            showinfo(
                title='TSP',
                message=f'The length is: {r[1]}'
            )


def main():
    from GraphAlgo import GraphAlgo
    g = DiGraph.load_from_json("../data/A0.json")
    algo = GraphAlgo(g)
    gui = Gui(algo)


if __name__ == "__main__":
    main()


