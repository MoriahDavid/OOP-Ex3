from typing import List
from queue import PriorityQueue

from GraphInterface import GraphInterface
from GraphAlgoInterface import GraphAlgoInterface
from DiGraph import DiGraph

class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph:GraphInterface):
        self._graph = graph

    def get_graph(self) -> GraphInterface:
        """
        :return: the directed graph on which the algorithm works on.
        """
        return self._graph

    def load_from_json(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        """
        g = DiGraph.load_from_json(file_name)
        if g:
            self._graph = g
            return True

        return False

    def save_to_json(self, file_name: str) -> bool:
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, False o.w.
        """
        return DiGraph.save_to_json(self._graph, file_name)

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, a list of the nodes ids that the path goes through
        Example:
#      >>> from GraphAlgo import GraphAlgo
#       >>> g_algo = GraphAlgo()
#        >>> g_algo.addNode(0)
#        >>> g_algo.addNode(1)
#        >>> g_algo.addNode(2)
#        >>> g_algo.addEdge(0,1,1)
#        >>> g_algo.addEdge(1,2,4)
#        >>> g_algo.shortestPath(0,1)
#        (1, [0, 1])
#        >>> g_algo.shortestPath(0,2)
#        (5, [0, 1, 2])
        Notes:
        If there is no path between id1 and id2, or one of them dose not exist the function returns (float('inf'),[])
        More info:
        https://en.wikipedia.org/wiki/Dijkstra's_algorithm
        """
        weights , pre_nodes = self._dijkstra(id1)

        if weights[id2] == float('inf'): # there is no path from id1 to id2
            return float('inf'), []

        # Gets the path nodes
        path = [id2]
        i = id2
        while i != id1:
            i = pre_nodes[i]
            path.insert(0, i)

        return weights[id2], path

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        """
        Finds the shortest path that visits all the nodes in the list
        :param node_lst: A list of nodes id's
        :return: A list of the nodes id's in the path, and the overall distance
        """

    def centerPoint(self) -> (int, float):
        """
        Finds the node that has the shortest distance to it's farthest node.
        :return: The nodes id, min-maximum distance
        """
        nodes_max_w = {}

        for n_src in self._graph.get_all_v().keys():
            max_w = float('-inf')
            weights , pre_nodes = self._dijkstra(n_src)
            for n_dst in self._graph.get_all_v().keys():
                if n_src == n_dst:
                    continue
                if weights[n_dst] == float('inf'): # There is no path from src to dst (graph is not connected)
                    return # TODO: Something
                if weights[n_dst] > max_w:
                    max_w = weights[n_dst]

            nodes_max_w[n_src] = max_w

        min_n = min(nodes_max_w, key=nodes_max_w.get)

        return min_n, nodes_max_w[min_n]

    def _dijkstra(self, src: int) -> (dict, dict):
        q = PriorityQueue()
        weights = {}
        pre_node = {}
        visited = []
        for n in self._graph.get_all_v().keys():
            weights[n] = float('inf')
            pre_node[n] = -1

        q.put((0, src))

        while not q.empty():
            node_w, node = q.get()
            visited.append(node)
            for nei_id, nei_w in self._graph.all_out_edges_of_node(node).items():
                if nei_w not in visited:
                    alt = node_w + nei_w
                    if alt < weights[nei_id]:
                        q.put((alt, nei_id))
                        weights[nei_id] = alt
                        pre_node[nei_id] = node

        return weights, pre_node

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """
        raise NotImplementedError


def main():
    g = DiGraph()
    a = GraphAlgo(g)
    a.load_from_json("../data/A5.json")
    print(a.shortest_path(0,20))
    print(a.centerPoint())


if __name__ == "__main__":
    main()