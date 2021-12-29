from GraphAlgo import GraphAlgo
from DiGraph import DiGraph
from Gui import Gui
import sys
import os


def main():
    path = "../data/A0.json"
    if len(sys.argv) > 1:
        path = sys.argv[1]
        if not os.path.exists(path):
            print("Error: Path not exist")
            return

    g = DiGraph.load_from_json(path)
    algo = GraphAlgo(g)
    gui = Gui(algo)


if __name__ == "__main__":
    main()
