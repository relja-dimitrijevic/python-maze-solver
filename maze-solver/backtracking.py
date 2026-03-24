import random
from constants import *
from enum import Enum
import numpy as np
import cv2
import math

class Directions(Enum):
	UP = 1
	DOWN = 2
	LEFT = 3
	RIGHT = 4

class Backtracking:

	def __init__(self, height, width, path, displayMaze):
		# Ensure odd dimensions
		if width % 2 == 0:
			width += 1
		if height % 2 == 0:
			height += 1

		self.width = width
		self.height = height
		self.path = path
		self.displayMaze = displayMaze

	# Generate maze
	def createMaze(self):
		maze = np.ones((self.height, self.width), dtype=float)

		# Fill walls (0) and free cells (1)
		for i in range(self.height):
			for j in range(self.width):
				if i % 2 == 1 or j % 2 == 1:
					maze[i, j] = 0  # Wall
				else:
					maze[i, j] = 1  # Free

		# Pick random starting point (even indices inside the maze)
		sx = random.choice(range(2, self.width - 2, 2))
		sy = random.choice(range(2, self.height - 2, 2))
		self.Generator(sx, sy, maze)

		maze[maze == 0.5] = 1

		# Display
		if self.displayMaze:
			cv2.namedWindow('Maze', cv2.WINDOW_NORMAL)
			cv2.imshow('Maze', maze)
			cv2.waitKey(0)
			cv2.destroyAllWindows()

		# Save as image
		img = maze * 255.0
		cv2.imwrite(self.path, img)

		return maze

	# Recursive generator with boundary check
	def Generator(self, current_cell_x, current_cell_y, grid):
		grid[current_cell_y, current_cell_x] = 0.5  # mark current as visited

		# Build list of valid directions dynamically
		directions = []
		if current_cell_y - 2 >= 0 and grid[current_cell_y-2, current_cell_x] == 1:
			directions.append(Directions.UP.value)
		if current_cell_y + 2 < self.height and grid[current_cell_y+2, current_cell_x] == 1:
			directions.append(Directions.DOWN.value)
		if current_cell_x - 2 >= 0 and grid[current_cell_y, current_cell_x-2] == 1:
			directions.append(Directions.LEFT.value)
		if current_cell_x + 2 < self.width and grid[current_cell_y, current_cell_x+2] == 1:
			directions.append(Directions.RIGHT.value)

		random.shuffle(directions)

		# Recursively move
		# Middle cell - wall supposed to be broken by the algorithm
		for dir in directions:
			if dir == Directions.UP.value:
				next_cell_x, next_cell_y = current_cell_x, current_cell_y-2
				middle_cell_x, middle_cell_y = current_cell_x, current_cell_y-1
			elif dir == Directions.DOWN.value:
				next_cell_x, next_cell_y = current_cell_x, current_cell_y+2
				middle_cell_x, middle_cell_y = current_cell_x, current_cell_y+1
			elif dir == Directions.LEFT.value:
				next_cell_x, next_cell_y = current_cell_x-2, current_cell_y
				middle_cell_x, middle_cell_y = current_cell_x-1, current_cell_y
			elif dir == Directions.RIGHT.value:
				next_cell_x, next_cell_y = current_cell_x+2, current_cell_y
				middle_cell_x, middle_cell_y = current_cell_x+1, current_cell_y

			if grid[next_cell_y, next_cell_x] == 1:
				grid[middle_cell_y, middle_cell_x] = 0.5
				self.Generator(next_cell_x, next_cell_y, grid)

	def findStartEnd(maze, limit_id):
     
		if limit_id != 1 and limit_id != 0:
			print("Invalid limit_id value, chose 0 or 1")
		
		else:
			free_cells = [(x, y) for y in range(0, len(maze))
									for x in range(0, len(maze[0]))
									if maze[y][x] == 1]

			if not free_cells:
				return None, None, maze
		
			if limit_id == 0:
				start = random.choice(free_cells)
				end = random.choice(free_cells)
  
				while end == start:
					end = random.choice(free_cells)
			
			elif limit_id == 1:
				start = free_cells[0]
				end = free_cells[len(free_cells) - 1]

			maze[start[1]][start[0]] = START
			maze[end[1]][end[0]] = END

			return start, end, maze