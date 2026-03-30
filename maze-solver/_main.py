from maze_gen import generateMaze
from backtracking import Backtracking
from maze_solve import solveMaze
from class_maze import Maze
from renderer import Animate
import numpy as np

maze = generateMaze("prims", 40, 40, "maze_image.png", False)
print("Maze values:", np.unique(maze))

start, end, maze = Backtracking.findStartEnd(maze, 1)

maze_obj = Maze(maze, start, end)
maze_obj.printASCII(start, end)

print("Start:", start)
print("End:", end)

solver = solveMaze(maze, start, end, algorithm="a*") # algorithm = bfs / wall_follower / a*
Animate(maze, solver, end, start)