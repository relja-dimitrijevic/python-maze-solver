import random
from enum import Enum
import numpy as np
import cv2
import sys

class Directions(Enum):
	UP = 1
	DOWN = 2
	LEFT = 3
	RIGHT = 4

#Class for Backtracking algorithm
class Backtracking:
		
	def __init__(self, height, width, path, displayMaze):
	 	
		#Adjust the width and height of the grid
		if width % 2 == 0:
			width += 1
		if height % 2 == 0:
			height += 1
	
		self.width = width
		self.height = height
		self.path = path
		self.displayMaze = displayMaze

	#Generating grid as a 2D array using height and width
	def createMaze(self):
		maze = np.ones((self.height, self.width), dtype=float)

		for i in range(self.height):
			for j in range(self.width):
				if i % 2 == 1 or j % 2 == 1:
					maze[i, j] = 0 #Walls
				if (i == 0 or j == 0 or i == self.height - 1 or j == self.width - 1):
					maze[i, j] = 0.5  #Visited cell
		
		sx = random.choice(range(2, self.width - 2, 2))
		sy = random.choice(range(2, self.width - 2, 2))
		self.generator(sx, sy, maze)

		for i in range(self.height):
			for j in range(self.width):
				if maze[i, j] == 0.5:
					maze[i, j] = 1

		maze[1, 2] = 1
		maze[self.height - 2, self.width - 3] = 1

		if self.displayMaze: #Displaying the maze
			cv2.namedWindow('Maze', cv2.WINDOW_NORMAL)
			cv2.imshow('Maze', maze)
			cv2.waitKey(0)
			cv2.destroyAllWindows()

		#Saving the maze as a image
		img = maze * 255.0
		cv2.imwrite(self.path, img)

		return maze
						  
	#Recursive function for generating a maze
	def generator(self, cx, cy, grid):
		grid[cy, cx] = 0.5

		if grid[cy - 2, cx] == 0.5 and grid[cy + 2, cx] == 0.5 and grid[cy, cx - 2] == 0.5 and grid[cy, cx + 2] == 0.5:
			pass
		else:
			li = [1, 2, 3, 4]
			while len(li) > 0:
				dir = random.choice(li)
				li.remove(dir)

				if dir == Directions.UP.value:
					ny = cy - 2
					my = cy - 1
				elif dir == Directions.DOWN.value:
					ny = cy + 2
					my = cy + 1
				else:
					ny = cy
					my = cy


				if dir == Directions.LEFT.value:
					nx = cx - 2
					mx = cx - 1
				elif dir == Directions.RIGHT.value:
					nx = cx + 2
					mx = cx + 1
				else:
					nx = cx
					mx = cx

				if grid[ny, nx] != 0.5:
					grid[my, mx] = 0.5
					self.generator(nx, ny, grid)
	 
	# Finding start and end of a maze using random free cells
	def find_start_end(maze):
		free_cells = []

		for y in range(1, len(maze)-1):
			for x in range(1, len(maze[0])-1):
				if maze[y][x] == 1:
					free_cells.append((x, y))

		if not free_cells:
			return None, None, maze

		start = random.choice(free_cells)
		end = random.choice(free_cells)

		while end == start:
			end = random.choice(free_cells)

		# Mark start and end
		maze[start[1]][start[0]] = 2
		maze[end[1]][end[0]] = 3

		return start, end, maze