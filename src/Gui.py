from tkinter import *
from tkinter.filedialog import asksaveasfile
from tkinter import filedialog as fd, messagebox
from tkinter.messagebox import showinfo
from tkinter import simpledialog

from GraphAlgoInterface import GraphAlgoInterface
from GraphAlgo import GraphAlgo


class Gui:
    def __init__(self, graph_algo: GraphAlgo):
        self.root = Tk()
        self.root.geometry("400x400")
        self.algo = graph_algo
        self._init_menu()

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
        graph_menu.add_command(label="Add Node", command=self.add_node)
        graph_menu.add_command(label="Add Edge", command=self.add_edge)
        graph_menu.add_separator()
        graph_menu.add_command(label="Clear Marked Edges", command=self.clear_marked_edges)
        graph_menu.add_command(label="Clear Marked Nodes", command=self.clear_marked_nodes)
        graph_menu.add_separator()
        graph_menu.add_command(label="Add all for TSP", command=self.add_all_for_tsp)
        graph_menu.add_command(label="Remove all for TSP", command=self.remove_all_for_tsp)

        algorithm_menu = Menu(my_menu, tearoff=0)
        my_menu.add_cascade(label="Algorithms", menu=algorithm_menu)
        algorithm_menu.add_command(label="Shortest Path", command=self.shortest_path)
        algorithm_menu.add_command(label="Center", command=self.center)
        algorithm_menu.add_command(label="TSP", command=self.tsp)

        self.root.mainloop()

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

    def add_node(self):
        pass

    def add_edge(self):
        pass

    def clear_marked_edges(self):
        pass

    def clear_marked_nodes(self):
        pass

    def add_all_for_tsp(self):
        pass

    def remove_all_for_tsp(self):
        pass

    def shortest_path(self):
        answer = simpledialog.askstring("Shortest path", "Write the source node and the destination node with one space between them",
                                        parent=self.root)
        if answer:
            l = answer.split(" ")
            if len(l) != 2:
                messagebox.showerror("Wrong input", "Choose source and destination node")
                return

            src = int(l[0])
            dst = int(l[1])
            if self.algo.get_graph().get_all_v().get(src) is None or self.algo.get_graph().get_all_v().get(dst) is None:
                messagebox.showerror("Wrong input", "Nodes don't exist on the graph")
                return
            r = self.algo.shortest_path(src, dst)

            # TODO: mark the edges on r[1]

            showinfo(
                title='shorted Path',
                message='The length is: ' + str(r[0])
            )


    def center(self):
        r = self.algo.centerPoint()
        showinfo(
            title='center',
            message='The center is: ' + r
        )

    def tsp(self):
        showinfo(
            title='TSP',
            message='The length is: '
        )


def main():
    algo = GraphAlgo()
    gui = Gui(algo)


if __name__ == "__main__":
    main()

