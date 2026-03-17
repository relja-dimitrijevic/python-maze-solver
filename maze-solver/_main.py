from maze_gen import generate_maze
from backtracking import Backtracking
from maze_solve import solveMaze
from class_maze import Maze
from renderer import animate
import numpy as np

maze = generate_maze("backtracking", 25, 25, "maze_image.png", True)
print("Maze values:", np.unique(maze))

start, end, maze = Backtracking.find_start_end(maze, 1)

maze_obj = Maze(maze, start, end)
maze_obj.print_ascii(start, end)

print("Start:", start)
print("End:", end)

solver = solveMaze(maze, start, end)
animate(maze, solver, end)