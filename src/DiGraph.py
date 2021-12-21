from GraphInterface import GraphInterface
from Node import Node
import json


class DiGraph(GraphInterface):

    def __init__(self):
        self._mc = 0
        self._edges_src = {}
        self._edges_dest = {}
        self._nodes = {}
        self._edges_counter = 0

    def v_size(self) -> int:
        """
        Returns the number of vertices in this graph
        @return: The number of vertices in this graph
        """
        return len(self._nodes)

    def e_size(self) -> int:
        """
        Returns the number of edges in this graph
        @return: The number of edges in this graph
        """
        return self._edges_counter

    def get_all_v(self) -> dict:
        """return a dictionary of all the nodes in the Graph, each node is represented using a pair
         (node_id, node_data)
        """
        return self._nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (other_node_id, weight)
         """
        return self._edges_dest.get(id1, {})

    def all_out_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected from node_id , each node is represented using a pair
        (other_node_id, weight)
        """
        return self._edges_src.get(id1, {})

    def get_mc(self) -> int:
        """
        Returns the current version of this graph,
        on every change in the graph state - the MC should be increased
        @return: The current version of this graph.
        """
        return self._mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        Adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.
        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
        """
        if self._nodes.get(id1) is None or self._nodes.get(id2) is None:
            return False

        if self._edges_src.get(id1).get(id2) is not None:
            return False

        self._edges_src[id1][id2] = weight
        self._edges_dest[id2][id1] = weight
        self._edges_counter += 1
        self._mc += 1
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        Adds a node to the graph.
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.
        Note: if the node id already exists the node will not be added
        """
        if not self._nodes.get(node_id) is None:
            return False

        self._nodes[node_id] = Node(node_id, pos)
        self._mc += 1
        self._edges_src[node_id] = {}
        self._edges_dest[node_id] = {}
        return True

    def remove_node(self, node_id: int) -> bool:
        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.
        Note: if the node id does not exists the function will do nothing
        """
        if self._nodes.get(node_id) is None:
            return False

        self._nodes.pop(node_id)
        self._edges_counter -= len(self._edges_src.pop(node_id, {}))
        self._edges_counter -= len(self._edges_dest.pop(node_id, {}))
        self._mc = self._mc + 1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.
        Note: If such an edge does not exists the function will do nothing
        """
        if self._edges_src.get(node_id1, {}).get(node_id2) is None:
            return False
        self._edges_src.get(node_id1).pop(node_id2)
        self._edges_dest.get(node_id2).pop(node_id1)
        self._mc += 1
        self._edges_counter -= 1
        return True

    @staticmethod
    def save_to_json(graph: GraphInterface, file_name: str) -> bool:
        """

        """
        try:
            with open(file_name, "w") as f:
                nodes = []
                edges = []
                for n_id, n_obj in enumerate(graph.get_all_v()):
                    nodes.append({"id": n_id, "pos": ",".join(n_obj.pos)})

                    for dest_id, w in graph.all_out_edges_of_node(n_id).items():
                        edges.append({"src": n_id, "dest": dest_id, "w": w})

                j = {"Edges": edges, "Nodes": nodes}

                json.dump(j, f, indent=4)
                return True

        except (FileNotFoundError, TypeError):
            return False

    @staticmethod
    def load_from_json(file_name: str):
        """

        """
        try:
            with open(file_name, "r") as f:
                d = json.load(f)
                graph = DiGraph()
                for node in d["Nodes"]:
                    pos = node.get('pos')
                    pos = tuple(pos.split(',')) if pos else None
                    graph.add_node(node["id"], pos)

                for edge in d["Edges"]:
                    graph.add_edge(edge["src"], edge["dest"], edge["w"])

                return graph

        except (FileNotFoundError, json.decoder.JSONDecodeError) as e:
            print(e)
            return None
