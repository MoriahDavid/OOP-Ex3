import os
from unittest import TestCase

from GraphAlgo import GraphAlgo
from DiGraph import DiGraph

class TestGraphAlgo(TestCase):
    base_folder = os.path.join("..", "data")
    graphs = ["G1.json", "G2.json", "G3.json",
              "A0.json", "A1.json", "A2.json", "A3.json", "A4.json", "A5.json",
              #os.path.join("LCG", "1000.json"), os.path.join("LCG", "10000.json"),
              ]

    # All knows centers (id, weight) (None for unknown)
    centers = [(8, None), (0, None), (40, None),
               (7, 6.80), (8, 9.92), (0, 7.81), (2, 8.18), (6, 8.07), (40, 9.29),
               (362, None), (3846, None)]

    def setUp(self):
        self.algo0 = GraphAlgo()
        self.algo0.load_from_json("../data/A0.json")
        self.algo1 = GraphAlgo()
        self.algo1.load_from_json("../data/A1.json")

    def test_get_graph(self):
        self.assertTrue(isinstance(self.algo0.get_graph(), DiGraph))

    def test_load_from_json(self):
        algo = GraphAlgo()
        self.assertTrue(algo.load_from_json("../data/A0.json"))
        self.assertEqual(11, algo.get_graph().v_size())
        self.assertEqual(22, algo.get_graph().e_size())

    def test_save_to_json(self):
        algo = GraphAlgo()
        self.assertTrue(algo.load_from_json("../data/A0.json"))
        self.assertEqual(11, algo.get_graph().v_size())
        self.assertEqual(22, algo.get_graph().e_size())
        algo.get_graph().remove_node(1)
        self.assertEqual(10, algo.get_graph().v_size())
        self.assertEqual(18, algo.get_graph().e_size())

        self.assertTrue(algo.save_to_json("../data/A0_MOD.json"))

        algo2 = GraphAlgo()
        self.assertTrue(algo2.load_from_json("../data/A0_MOD.json"))
        self.assertEqual(10, algo2.get_graph().v_size())
        self.assertEqual(18, algo2.get_graph().e_size())

    def test_shortest_path(self):
        algo = GraphAlgo()
        algo.get_graph().add_node(1)
        algo.get_graph().add_node(2)
        algo.get_graph().add_edge(1, 2, 20)

        r = algo.shortest_path(1, 2)

        self.assertEqual(20, r[0])
        self.assertEqual(2, len(r[1]))

        algo.get_graph().add_node(3)
        algo.get_graph().add_edge(3, 1, 7)
        algo.get_graph().add_edge(3, 2, 50)
        r = algo.shortest_path(3, 2)
        self.assertEqual(27, r[0])

        self.assertEqual(3, len(r[1]))
        self.assertEqual(3, r[1][0])
        self.assertEqual(1, r[1][1])
        self.assertEqual(2, r[1][2])

    def test_tsp(self):
        for i, p in enumerate(self.graphs[:3]):
            algo = GraphAlgo()
            algo.load_from_json(os.path.join(self.base_folder, p))

            l = [1, 5, 10]

            r = algo.TSP(l)
            for n in r[0] :
                print(f"{n} -> ",end="")
            print("")
            self.assertTrue(len(r[0]) >= 3)

            for n in l:
                self.assertTrue(n in r[0])

    def test_tsp_nc(self):
        algo = GraphAlgo()
        algo.get_graph().add_node(1)
        algo.get_graph().add_node(2)
        algo.get_graph().add_node(3)
        algo.get_graph().add_edge(1, 2, 20)

        r = algo.TSP([1,2,3])
        self.assertEqual(0, len(r[0]))
        self.assertEqual(float('inf'), r[1])

    def test_center_point(self):
            for i, p in enumerate(self.graphs):
                algo = GraphAlgo()
                algo.load_from_json(os.path.join(self.base_folder, p))
                c = algo.centerPoint()
                print(f"Finish {p}")
                if i < len(self.centers):
                    self.assertEqual(c[0], self.centers[i][0])
                    if self.centers[i][1] is not None:
                        self.assertAlmostEqual(c[1], self.centers[i][1], places=1)
                    else:
                        self.assertNotEqual(c[1], float('inf'))

    def test_center_nc(self):
        algo = GraphAlgo()
        algo.get_graph().add_node(1)
        algo.get_graph().add_node(2)
        algo.get_graph().add_node(3)
        algo.get_graph().add_edge(1, 2, 20)

        r = algo.centerPoint()
        self.assertEqual(-1, r[0])
        self.assertEqual(float('inf'), r[1])
