import math
import random
import tkinter

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.patches import ConnectionPatch, ConnectionStyle

def get_center_between_points(c1, c2):
    return ((c1[0] + c2[0])/2, (c1[1] + c2[1])/2)

def get_point_on_line(x1, y1, angle, len):
    return x1 + len * math.cos(angle), y1 + len * math.sin(angle)

def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

class DrawGraph:
    SIZE_H = 1000
    SIZE_W = 2000

    # https://matplotlib.org/stable/gallery/color/named_colors.html
    COLOR_V = "lightblue"
    COLOR_V_MARK = "lightcoral"
    COLOR_E = "black"
    COLOR_E_MARK = "red"

    def __init__(self, g):
        self._graph = g
        self._vertices = list(g.get_all_v().values())
        self.have_pos = self.check_have_pos()

        if not self.have_pos:
            self.random_pos()

        self._init_min_max()

        self.marked_e = []
        self.marked_v = []
        self.fig = Figure()

    def random_pos(self):
        if not self.have_pos:
            for v in self._graph.get_all_v().values():
                new_x = random.random()
                new_y = random.random()
                v.pos = (new_x, new_y)

    def check_have_pos(self):
        for n in self._graph.get_all_v().values():
            if not n.pos:
                return False

        return True

    def clear_marked(self):
        self.marked_e = []
        self.marked_v = []

    def reload(self, g=None):
        if g:
            self._graph = g

        self._vertices = list(g.get_all_v().values())
        self._init_min_max()

        self.draw_graph()

    @staticmethod
    def _angle_trunc(a):
        while a < 0.0:
            a += math.pi * 2
        return a

    @staticmethod
    def _get_angle_between_points(c1, c2):
        deltaY = c2[1] - c1[1]
        deltaX = c2[0] - c1[0]
        return math.degrees(DrawGraph._angle_trunc(math.atan2(deltaY, deltaX)))

    @staticmethod
    def _get_edge_text_pos(c1, c2):
        x1, y1 = c1
        x2, y2 = c2
        x12, y12 = (x1 + x2) / 2., (y1 + y2) / 2.
        dx, dy = x2 - x1, y2 - y1

        f = -0.08

        return x12 + f * dy, y12 - f * dx

    def _init_min_max(self):
        self.max_x = max(self._vertices, key=lambda v: v.pos[0]).pos[0]
        self.min_x = min(self._vertices, key=lambda v: v.pos[0]).pos[0]
        self.max_y = max(self._vertices, key=lambda v: v.pos[1]).pos[1]
        self.min_y = min(self._vertices, key=lambda v: v.pos[1]).pos[1]

    def get_scaled_value(self, x_y):
        new_x = map(x_y[0], self.min_x, self.max_x, 50, self.SIZE_W-50)
        new_y = map(x_y[1], self.min_y, self.max_y, 50, self.SIZE_H-50)
        return new_x, new_y

    def draw_graph(self):

        fig = self.fig

        fig.clear()

        ax = fig.add_subplot()
        ax.axis('scaled')
        ax.set_xlim(0, self.SIZE_W)
        ax.set_ylim(0, self.SIZE_H)
        ax.axis('off')

        pos_x = []
        pos_y = []
        marked_pos_x = []
        marked_pos_y = []
        for v in self._vertices:

            new_x, new_y = self.get_scaled_value(v.pos)

            if v.n_id in self.marked_v:
                marked_pos_x.append(new_x)
                marked_pos_y.append(new_y)
            else:
                pos_x.append(new_x)
                pos_y.append(new_y)

        # Draw Nodes
        ax.scatter(pos_x, pos_y, s=400, c=self.COLOR_V)
        ax.scatter(marked_pos_x, marked_pos_y, s=400, c=self.COLOR_V_MARK)

        # Draw Nodes id
        for v in self._vertices:
            ax.annotate(v.n_id, self.get_scaled_value(v.pos), ha='center', va='center')

        con_style = ConnectionStyle("Arc3", rad=-0.08)

        # for each node draw the edges
        for v in self._vertices:
            for v_dst_id, w in self._graph.all_out_edges_of_node(v.n_id).items():
                v_dst = self._graph.get_all_v()[v_dst_id]
                pos_src = self.get_scaled_value(v.pos)
                pos_dst = self.get_scaled_value(v_dst.pos)

                color = self.COLOR_E_MARK if (v.n_id, v_dst.n_id) in self.marked_e else self.COLOR_E

                con = ConnectionPatch(pos_src, pos_dst, "data", "data", arrowstyle="-|>", shrinkA=20, shrinkB=18,
                                      connectionstyle=con_style, mutation_scale=20, fc="w", edgecolor=color)
                ax.add_artist(con)

                angle = self._get_angle_between_points(pos_src, pos_dst)
                text_x, text_y = self._get_edge_text_pos(pos_src, pos_dst)
                text = "{:.2f}".format(w)
                t = ax.text(text_x, text_y, text, ha="center", va="center", rotation=angle, size=8)

        return fig


def main():
    root = tkinter.Tk()
    root.wm_title("Embedding in Tk")
    root.state("zoomed")

    from GraphAlgo import GraphAlgo
    algo = GraphAlgo()
    algo.load_from_json("../data/A0.json")

    d_g = DrawGraph(algo.get_graph())
    fig = d_g.draw_graph()

    canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    tkinter.mainloop()


if __name__ == "__main__":
    main()
