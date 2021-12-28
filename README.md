## :wavy_dash: :white_medium_small_square: :white_small_square: Directed Weighted Graphs - Python :white_small_square: :white_medium_small_square: :wavy_dash:


### **This project made for directed weighted graphs algorithms and implements graphic user interface.** <br />
<br />

### 🔶 Main Classes:

#### :black_medium_square: Node
On this class we save for every node: key, location. <br />

#### :black_medium_square: Digraph
This class represents our directed weighted graph. <br />
We create two dict in dict and one regular dict: <br />

The first is -edges_src- represents the edges from source to destination. <br />
For every node-key from source, we keep in internal dict the node-key from dest and the appropriate edge (from src to dest). <br />
The second is -edges_dest- represents edges from destination to source. <br />
For every node-key from destination, we keep in internal dict the node-key from source and the appropriate edge (from dest to source). <br />
We made this method in order to makes some methods easier to implements. <br />
In addition we creats regular dict -nodes- that represents the nodes on this graph. <br />
The first one is -nodes- represents our nodes on the graph. <br />

In this class we implement these methods: get_edge, add_node, add_egde, remove_node, remove_edge, size_v, size_e, get_mc. <br />

#### :black_medium_square: GraphAlgo
In this class we have the main algorithms for graph. <br />
The methods: <br />

**get_graph-** Return the graph. <br />
**Dijkstra-** Dijkstra's algorithm found the shortest path between two given nodes. Dijkstra algorithm- https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm <br />
**shortestPath-** Return list that represents the shortest path between two nodes and the path lenght. In this method we use the Dijkstra algorithm. <br />
**center-** Checks for every node who is the furthest node (with the highest weight) and save its weight. After that it return the node with the smallest weight and the weight. <br />
**tsp-** Return a list that represents the shortest path (with the smallest weight)by using greedy algorithm. It start by choosing random node and every time, we search for the closest node from this node that not visited yet. When we find the closest node we add this node to a new list. We will continue to do this as long as there is a node that not visited. Return the new list. and the lenght <br />

 <br />

### 🔶 Algorithms Results:

We run preformes tests to the algorithms. for every algorithm test we define 15 min for timeout. <br />
<br />

Graph          | Load        | Save | Shorted path | Center  | TSP |
-------------- | ------------ | -----|-----------| --------|-----|
   A0          |          ms  |       | 1 ms    |    1 ms   |  15 ms |
   A1          |        ms    |       |1 ms      |   15 ms  | 1 ms |
   A2          |           ms |       |15 ms     | 15 ms    |    31 ms |
   A3          |          ms  |       | 1 ms    |    62 ms |  46 ms |
   A4          |          ms  |       | 1 ms    |    31 ms |  46 ms |
   A5          |          ms  |       | 1 ms     |    62 ms |  62 ms |
   1000 nodes  |          ms  |       |234 ms    | 3,078 ms |Timed Out|
   10,000 nodes|         ms   |       |28,788 ms |Timed Out|Timed Out|
   100,000 nodes|          ms |       |Timed Out  |Timed Out|Timed Out|
   1,000,000 nodes|           |       |Timed Out  |Timed Out| Timed Out |

<br />

### 🔶 GUI: <br />
The user interface has been designed with user experience and convenience in mind in order to allow the use of all the features of the system. 
In this GUI we can see the graph and modified it. every node has its key and every edge has its weight on it. <br />

<br />

**Download-** for downloading clone the repo <br />
**Run-** python3 Ex3.py {graph_json_path}. (if the input is empty it's open the graph A0.json)<br />
* Can run graph example files from folder data: "python3 Ex3.py ../data/G1.json" <br />

**Use-** explain about the menu on the GUI: <br />

**File Menu**      | Explain      |
-------------- | ------------ |                               
   Load Graph  |      load graph from json file      | 
   Save Graph  |     save this graph to json file    | 
   Exit        |        close the program            |



**Graph Menu**     | Explain                                   | 
-------------- | -------------------------------------------|                               
   Clear Marked Edges       |                               |

   
   
   **Algorithms Menu**      | Explain                       |
-------------- | -------------------------------------------|
   Shortest Path  |    Run the algorithm between two chosen nodes in the graph and displays this path      |
   Center       |     Run the algorithm and displays the center node                       |
   TSP          |    Run the algorithm in order to find the shortest path for all the nodes        |
   

<br />

### 🔶 Tests:
The project has been checked by unittests, manual GUI test and preformance tests. <br />
<br />

