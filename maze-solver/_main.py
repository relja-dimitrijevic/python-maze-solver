from maze_gen import generateMaze
from backtracking import Backtracking
from maze_solve import solveMaze
from class_maze import Maze
from renderer import Animate
import numpy as np

maze = generateMaze("backtracking", 40, 40, "maze_image.png", True)
print("Maze values:", np.unique(maze))

start, end, maze = Backtracking.findStartEnd(maze, 0)

maze_obj = Maze(maze, start, end)
maze_obj.printASCII(start, end)

print("Start:", start)
print("End:", end)

solver = solveMaze(maze, start, end, algorithm="bfs") # algorithm = bfs / wall_follower 
Animate(maze, solver, end)