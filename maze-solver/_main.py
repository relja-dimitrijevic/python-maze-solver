from maze_gen import generate_maze
from backtracking import Backtracking
from maze_solve import solveMaze
from class_maze import Maze

maze_matrix = generate_maze("backtracking", 15, 15, "maze_test.png", True)

start, end, maze = Backtracking.find_start_end(maze_matrix)

maze_obj = Maze(maze, start, end)
maze_obj.print_ascii(start, end)

print("Start:", start)
print("End:", end)

distance = solveMaze(maze, start, end)
print("Shortest distance:", distance)