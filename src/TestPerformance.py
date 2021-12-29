from GraphAlgo import GraphAlgo
import unittest
import time
import os


class MyTestCase(unittest.TestCase):
    base_folder = os.path.join("..", "data")
    graphs = ["G1.json", "G2.json", "G3.json" ,
              "A0.json", "A1.json","A2.json", "A3.json", "A4.json", "A5.json",
              os.path.join("LCG", "1000.json"), os.path.join("LCG", "10000.json"),
              os.path.join("LCG", "100000.json")]

    def test_shortest_path(self):
        for i, p in enumerate(self.graphs):
            algo = GraphAlgo()
            algo.load_from_json(os.path.join(self.base_folder, p))
            start_t = time.time_ns()
            c = algo.shortest_path(1, 10)
            stop_t = time.time_ns()
            t = (stop_t - start_t) / 1e+6
            print(f"Shortest path - '{p}' : {t} ms")

            self.assertNotEqual(c[0], float('inf'))
            self.assertNotEqual(len(c[1]), 0)

    def test_center(self):
        for p in self.graphs:
            algo = GraphAlgo()
            algo.load_from_json(os.path.join(self.base_folder, p))

            start_t = time.time_ns()
            algo.centerPoint()
            stop_t = time.time_ns()
            t = (stop_t - start_t)/1e+6
            print(f"Center - '{p}' : {t} ms")

    def test_tsp(self):
        for p in self.graphs:
            algo = GraphAlgo()
            algo.load_from_json(os.path.join(self.base_folder, p))

            start_t = time.time_ns()
            algo.TSP(list(algo.get_graph().get_all_v().keys()))
            stop_t = time.time_ns()
            t = (stop_t - start_t)/1e+6
            print(f"TSP - '{p}' : {t} ms")

    def test_load_sava(self):
        for p in self.graphs:
            algo = GraphAlgo()

            start_t = time.time_ns()
            self.assertTrue(algo.load_from_json(os.path.join(self.base_folder, p)))
            stop_t = time.time_ns()
            t = (stop_t - start_t)/1e+6
            print(f"load - '{p}' : {t} ms")

            start_t = time.time_ns()

            self.assertTrue(algo.save_to_json(os.path.join(self.base_folder, "tests", p)))
            stop_t = time.time_ns()
            t = (stop_t - start_t) / 1e+6
            print(f"save - '{p}' : {t} ms")

