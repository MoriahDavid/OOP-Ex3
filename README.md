## :wavy_dash: :white_medium_small_square: :white_small_square: Directed Weighted Graphs - Python :white_small_square: :white_medium_small_square: :wavy_dash:


### **This project made for directed weighted graphs algorithms and implements graphic user interface.** <br />
<br />

### 🔶 Main Classes:

#### :black_medium_square: Node
On this class we save for every node: key, location. <br />
We create sets and gets methods. <br />

#### :black_medium_square: Digraph
This class represents our directed weighted graph. <br />
We create two dict in dict and one regular dict: <br />

The first is -edges_src- represents the edges from source to destination. <br />
For every node-key from source, we keep in internal HashMap the node-key from dest and the appropriate edge (from src to dest). <br />
The second is -edges_dest- represents edges from destination to source. <br />
For every node-key from destination, we keep in internal HashMap the node-key from source and the appropriate edge (from dest to source). <br />
We made this method in order to makes some methods easier to implements. <br />
In addition we creats regular HashMap -nodes- that represents the nodes on this graph. <br />
The first one is -nodes- represents our nodes on the graph. <br />

In this class we implement these methods: transpose, getNode, getEdge, addNode, connect, nodeIter, edgeIter, removeNode, removeEdgesForNode, rempveEdge, nodeSize, edgeSize, getMC. <br />
We also made three classes for Iterator: nodeIterator, edgeIterator- for specific node and AllEdgesIterator- for all the nodes on the graph. <br />

#### :black_medium_square: GraphAlgo
In this class we have the main algorithms for graph. <br />
The methods: <br />

**getGraph-** Return the graph. <br />
**Dijkstra-** Dijkstra's algorithm found the shortest path between two given nodes. Dijkstra algorithm- https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm <br />
**shortestPath-** Return list that represents the shortest path between two nodes. In this method we use the Dijkstra algorithm. <br />
**center-** Checks for every node who is the furthest node (with the highest weight) and save its weight. After that it return the node with the smallest weight. <br />
**tsp-** Return a list that represents the shortest path (with the smallest weight)by using greedy algorithm. We reset the nodes tag to zero. It start by choosing random node and every time, we search for the closest node from this node with tag 0. When we find the closest node we change its tag to 1 and add this node to a new list. We will continue to do this as long as there is a node with data 0. If the algorithms cant find a node with tag 0 --> going back one node. Return the new list. <br />
**pathWeight-** Return the total weight of a path (represents with list). <br />
**getRandomNode-** Return node in random. <br />
**closestNode-** Return the closest node to some node by passing all the nodes in the list and calculate the total weight. <br />

 <br />

### 🔶 Algorithms Results:

We run preformes tests to the algorithms. for every algorithm test we define 15 min for timeout. <br />
<br />

Graph          | Load        | Save | Shorted path | Center  | TSP |
-------------- | ------------ | -----|-----------| --------|-----|
   A0          |        1 ms  |       | 1 ms    |    1 ms   |  15 ms |
   A1          |      1 ms    |       |1 ms      |   15 ms  | 1 ms |
   A2          |         1 ms |       |15 ms     | 15 ms    |    31 ms |
   A3          |        1 ms  |       | 1 ms    |    62 ms |  46 ms |
   A4          |        1 ms  |       | 1 ms    |    31 ms |  46 ms |
   A5          |        1 ms  |       | 1 ms    |    62 ms |  62 ms |
   1000 nodes  |       15 ms  |       |234 ms   | 3,078 ms |         |
   10,000 nodes|     393 ms   |       |28,788 ms |Timed Out|Timed Out|
   100,000 nodes|    12,649 ms |      |           |Timed Out|Timed Out|
   1,000,000 nodes| Timed Out|       |Timed Out  |Timed Out| Timed Out |

<br />

### 🔶 GUI: <br />
The user interface has been designed with user experience and convenience in mind in order to allow the use of all the features of the system. 
In this GUI we can see the graph and modified it. every node has its key and every edge has its weight on it. <br />

<br />

**Download-** for downloading clone the repo <br />
**Run-** java -jar Ex2.jar {graph_json_path}. <br />
* Can run example files form folder data (G1\G2\G3): "java -jar Ex2.jar Data/G1.json" <br />

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

