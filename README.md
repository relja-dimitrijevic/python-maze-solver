# Python Maze Generator & Solver

## Overview

This project generates random mazes and visualizes how different algorithms solve them.
It includes maze generation using a **recursive backtracking algorithm** and a visualization system that animates the exploration and the final shortest path.

The program renders the maze and the solving process using **OpenCV**, allowing you to see how the algorithm searches through the grid step-by-step.

## Features

* Random maze generation
* Recursive Backtracking maze generator
* Automatic start and end point selection
* Maze solving algorithm visualization
* Real-time animation of algorithm exploration
* Final shortest path highlighting
* Scalable visualization window

## Project Structure

```
maze-solver/
│
├── _main.py           # Program entry point
├── constants.py       # Grid cell constants (WALL, FREE, PATH, etc.)
├── maze_gen.py        # Maze generation interface
├── backtracking.py    # Backtracking maze generator implementation
├── maze_solve.py      # Maze solving algorithm
├── renderer.py        # Visualization and animation
├── class_maze.py      # Maze helper class (ASCII printing etc.)
└── maze_image.png     # Generated maze image output
```

## How It Works

### 1. Maze Generation

The maze is generated using the **Recursive Backtracking algorithm**:

1. Start from a random cell.
2. Mark it as visited.
3. Randomly choose a direction.
4. Move two cells in that direction.
5. Break the wall between the cells.
6. Recursively continue until all reachable cells are visited.

This creates a **perfect maze** (one unique path between any two cells).

### 2. Start and End Selection

After generation:

* All free cells are scanned.
* Two random free cells are selected.
* They are marked as:

  * `START`
  * `END`

### 3. Maze Solving

The solver explores the maze step-by-step:

* Each visited cell is recorded.
* The algorithm yields animation steps.
* When the end is reached, the final shortest path is reconstructed.

### 4. Visualization

The renderer animates the process using OpenCV:

Color legend:

| Cell Type    | Color  |
| ------------ | ------ |
| Wall         | Black  |
| Free space   | White  |
| Visited cell | Blue   |
| Final path   | Green  |
| Start        | Yellow |
| End          | Red    |

Each algorithm step is displayed as a frame, creating a smooth animation.

## Installation

### Requirements

* Python 3.10+
* NumPy
* OpenCV

Install dependencies:

```bash
pip install numpy opencv-python
```

## Running the Project

Run the main script:

```bash
python _main.py
```

This will:

1. Generate a random maze
2. Select start and end positions
3. Solve the maze
4. Display an animated visualization

## Example Workflow

```
Generate Maze
      ↓
Find Start & End
      ↓
Solve Maze
      ↓
Animate Exploration
      ↓
Display Shortest Path
```

## Customization

### Change Maze Size

In `_main.py`:

```python
maze = generate_maze("backtracking", 25, 25, "maze_image.png", True)
```

Example larger maze:

```python
maze = generate_maze("backtracking", 51, 51, "maze_image.png", True)
```

### Adjust Animation Speed

In `renderer.py`:

```python
cv2.waitKey(20)
```

Lower value → faster animation.

### Adjust Display Scale

```
scale = 30
```

Increase to enlarge the maze window.

## Possible Improvements

* Add more solving algorithms:

  * Breadth-First Search (BFS)
  * Depth-First Search (DFS)
  * A* Search
  * Dijkstra
* Add maze generation algorithms:

  * Prim's algorithm
  * Kruskal's algorithm
  * Wilson's algorithm
* Interactive maze controls
* Export solving animation as video
* Web visualization

## Educational Purpose

This project is useful for learning:

* Graph traversal algorithms
* Recursion
* Pathfinding techniques
* Visualization of algorithms
* Grid-based problem solving

## License

This project is open source and free to use for educational purposes.
