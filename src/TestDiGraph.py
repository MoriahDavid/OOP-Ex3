from unittest import TestCase
from DiGraph import DiGraph


class TestDiGraph(TestCase):

    def setUp(self):
        self.g1 = DiGraph()
        for id in range(1, 6):
            self.g1.add_node(id)

        self.g1.add_edge(1,3, 0.2)
        self.g1.add_edge(5, 1, 1)
        self.g1.add_edge(2, 5, 0.8)

    def test_v_size(self):
        self.assertEqual(5, self.g1.v_size())

    def test_e_size(self):
        self.assertEqual(3, self.g1.e_size())

    def test_get_all_v(self):
        all_v = self.g1.get_all_v()
        for id in range(1,5):
            self.assertTrue(all_v.get(id) is not None)

    def test_all_in_edges_of_node(self):
        self.assertEqual(1, len(self.g1.all_in_edges_of_node(1)))
        self.assertEqual(1, len(self.g1.all_in_edges_of_node(3)))

    def test_all_out_edges_of_node(self):
        self.assertEqual(1, len(self.g1.all_out_edges_of_node(1)))
        self.assertEqual(0, len(self.g1.all_out_edges_of_node(3)))

    def test_get_mc(self):
        g1 = DiGraph()
        for id in range(1, 6):
            g1.add_node(id)

        self.assertTrue(g1.add_edge(1, 3, 0.2))
        self.assertFalse(g1.add_edge(9, 1, 1))
        self.assertEqual(6, g1.get_mc())
        self.assertTrue(g1.remove_edge(1, 3))
        self.assertEqual(7, g1.get_mc())
        self.assertTrue(g1.remove_node(1))
        self.assertEqual(8, g1.get_mc())

    def test_add_edge(self):
        g1 = DiGraph()
        for id in range(1, 6):
            g1.add_node(id)

        self.assertTrue(g1.add_edge(1, 3, 0.2))
        self.assertFalse(g1.add_edge(9, 1, 1))
        self.assertEqual(1, g1.e_size())

    def test_add_node(self):
        g1 = DiGraph()
        for id in range(1, 6):
            g1.add_node(id)

        self.assertEqual(5, g1.v_size())

    def test_remove_node(self):
        g1 = DiGraph()
        for id in range(1, 6):
            g1.add_node(id)

        self.assertEqual(5, g1.v_size())
        self.assertTrue(g1.remove_node(1))
        self.assertEqual(4, g1.v_size())
        self.assertFalse(g1.remove_node(10))
        self.assertEqual(4, g1.v_size())

    def test_remove_edge(self):
        g1 = DiGraph()
        for id in range(1, 6):
            g1.add_node(id)

        g1.add_edge(1, 3, 0.2)
        g1.add_edge(5, 1, 1)
        g1.add_edge(2, 5, 0.8)

        self.assertEqual(3, g1.e_size())
        self.assertTrue(g1.remove_edge(1, 3))
        self.assertEqual(2, g1.e_size())
        self.assertFalse(g1.remove_edge(1, 10))
        self.assertEqual(2, g1.e_size())

    def test_save_to_json(self):
        g = DiGraph.load_from_json("../data/A0.json")
        self.assertIsNotNone(g)
        self.assertEqual(11, g.v_size())
        self.assertEqual(22, g.e_size())
        g.remove_node(1)
        self.assertEqual(10, g.v_size())
        self.assertEqual(18, g.e_size())

        self.assertTrue(DiGraph.save_to_json(g, "../data/A0_MOD.json"))

        g2 = DiGraph.load_from_json("../data/A0_MOD.json")
        self.assertIsNotNone(g2)
        self.assertEqual(10, g2.v_size())
        self.assertEqual(18, g2.e_size())

    def test_load_from_json(self):
        g = DiGraph().load_from_json("../data/A0.json")
        self.assertIsNotNone(g)
        self.assertEqual(11, g.v_size())
        self.assertEqual(22, g.e_size())
