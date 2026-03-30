Maze Generator and Solver (Python)
Overview

This project is a complete implementation of maze generation and pathfinding algorithms using Python. It is designed both as a functional system and as an educational resource for understanding how classical algorithms behave in constrained environments such as grid-based spaces.

The system combines two main areas:

Procedural generation — constructing mazes using deterministic and randomized algorithms
Graph traversal and search — solving mazes using optimal and heuristic-based approaches

The maze is modeled as a graph embedded in a two-dimensional grid, where each free cell represents a node and connections between cells represent edges. All solving algorithms operate on this abstraction.

The primary goal of this project is not only to produce a working maze solver, but also to demonstrate how different algorithms explore search space, how optimal paths are discovered, and how algorithmic strategies differ in behavior and efficiency. The visualization component allows direct observation of algorithm execution in real time.

Table of Contents
Maze Representation
Maze Generation Algorithms
Recursive Backtracking
Prim’s Algorithm
Maze Solving Algorithms
Breadth-First Search (BFS)
Wall Follower
A* Search
Visualization System
Project Structure
Usage
Possible Future Improvements
Maze Representation

The maze is stored as a two-dimensional NumPy array and accessed using row-column indexing:

maze[row][col] → maze[y][x]

Each cell is encoded numerically:

0 represents a wall
1 represents a free cell
START marks the starting position
END marks the goal
VISITED marks explored cells
PATH marks the final solution

This representation allows efficient computation and integrates well with visualization libraries such as OpenCV.

Maze Generation Algorithms
Recursive Backtracking
Concept

Recursive Backtracking is a depth-first search based algorithm used to generate perfect mazes. A perfect maze has exactly one path between any two points and contains no cycles.

Algorithm Behavior

The algorithm begins from a random cell, marks it as visited, and repeatedly moves to a randomly selected unvisited neighbor. When it moves, it removes the wall between the current cell and the chosen neighbor. This process continues recursively until no unvisited neighbors remain, at which point the algorithm backtracks to the previous cell and continues exploration.

Pseudocode
function generate(cell):
    mark cell as visited
    directions = shuffled directions

    for each direction:
        next_cell = cell + direction * 2
        if next_cell is valid and unvisited:
            remove wall between current and next_cell
            generate(next_cell)
Application in This Project

Cells are spaced in steps of two to preserve walls between them. The algorithm removes intermediate cells to carve passages. Recursion drives deep exploration before branching.

Characteristics
Produces long corridors
Low branching factor
Always fully connected
Efficient and simple
Prim’s Algorithm
Concept

Prim’s algorithm generates a maze by growing a spanning tree from an initial cell. Instead of going deep like DFS, it expands outward using a frontier of candidate cells.

Algorithm Behavior

The algorithm starts from a random cell, marks it as free, and adds its neighbors to a frontier list. It then repeatedly selects a random frontier cell, connects it to an already visited neighbor, removes the wall between them, and adds new neighboring cells to the frontier. This continues until no frontier cells remain.

Pseudocode
initialize maze with walls
pick starting cell
mark it as free
add neighbors to frontier

while frontier not empty:
    select random frontier cell
    find visited neighbors
    if neighbors exist:
        connect to one neighbor
        remove wall
        mark current as free
        add neighbors to frontier
Application in This Project

The frontier stores candidate cells rather than visited ones. Each step ensures the maze remains connected. Duplicate frontier entries are avoided for efficiency.

Characteristics
Produces denser and more complex mazes
Higher branching factor
Guarantees full connectivity
Maze Solving Algorithms
Breadth-First Search (BFS)
Concept

Breadth-First Search explores the maze level by level and guarantees the shortest path in an unweighted grid.

Algorithm Behavior

The algorithm uses a queue to explore nodes in layers. Starting from the initial position, it visits all neighboring cells before moving deeper. It records parent relationships to reconstruct the final path once the goal is reached.

Pseudocode
enqueue start
mark start visited

while queue not empty:
    current = dequeue
    if current equals end:
        break

    for each neighbor:
        if valid and not visited:
            enqueue neighbor
            record parent
Path Reconstruction
current = end

while current in parent:
    add current to path
    current = parent[current]
Application in This Project

The algorithm yields intermediate steps for animation and guarantees that the resulting path is the shortest possible.

Characteristics
Finds optimal path
Explores entire reachable space
Requires more memory than other approaches
Wall Follower
Concept

The Wall Follower algorithm simulates a simple navigation strategy: always keep one hand in contact with a wall.

Algorithm Behavior

At each step, the algorithm attempts to turn left. If that is not possible, it moves forward. If forward is blocked, it tries turning right. If all directions are blocked, it turns back.

Pseudocode
while not at goal:
    if left is free:
        turn left
    else if forward is free:
        move forward
    else if right is free:
        turn right
    else:
        turn back
Application in This Project

The algorithm maintains an orientation and updates movement relative to its current direction. It records visited cells but does not guarantee optimal paths.

Characteristics
Does not guarantee shortest path
Requires minimal memory
Works best on simply connected mazes
A* Search
Concept

A* is a heuristic-based search algorithm that balances exploration and efficiency by estimating the distance to the goal.

Evaluation Function
f(n) = g(n) + h(n)

Where:

g(n) is the cost from the start to the current node
h(n) is the estimated distance to the goal
Algorithm Behavior

The algorithm uses a priority queue to always expand the most promising node. It updates costs and parent relationships whenever a better path is found.

Pseudocode
initialize open set
add start

while open set not empty:
    current = node with lowest score

    if current equals goal:
        reconstruct path

    for each neighbor:
        calculate tentative cost
        if better path:
            update parent and scores
            add to open set
Application in This Project

A* uses a heuristic such as Manhattan distance to guide search efficiently and produce an optimal solution.

Characteristics
Finds optimal path
Faster than BFS in most cases
Balances performance and accuracy
Visualization System

The project includes a visualization system using OpenCV to display algorithm execution in real time.

Color Mapping
Wall: black
Free cell: white
Visited: blue
Path: green
Start: yellow
End: red
Execution Flow
solver → animate() → render() → display window

Each solving algorithm yields intermediate steps, allowing dynamic visualization of both exploration and final path.

Project Structure
maze-solver/

backtracking.py
prims.py
maze_gen.py
maze_solve.py
renderer.py
constants.py
class_maze.py
_main.py
Usage

Run the main script:

python _main.py
Typical Workflow
Generate a maze using a selected algorithm
Choose start and end positions
Select a solving algorithm
Visualize the solving process
Possible Future Improvements
Implementation of Dijkstra’s algorithm
Bidirectional search techniques
Support for weighted mazes
Interactive user interface for selecting algorithms
Step-by-step visualization of maze generation
Performance comparison between algorithms
Export of animations as video or GIF