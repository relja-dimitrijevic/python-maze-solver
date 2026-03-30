import random
import numpy as np
import cv2
from constants import *


class Prims:

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

    def createMaze(self):
        # 0 = wall, 1 = free
        maze = np.zeros((self.height, self.width), dtype=float)

        # Step 1: pick random starting cell (even coordinates)
        start_x = random.randrange(2, self.width - 2, 2)
        start_y = random.randrange(2, self.height - 2, 2)

        maze[start_y][start_x] = 1
        
        # Step 2: frontier list (cells to expand)
        frontier = []
        
        directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        
        for dx, dy in directions:
            fx = start_x + dx
            fy = start_y + dy

            if 0 <= fx < self.width and 0 <= fy < self.height:
                frontier.append((fx, fy))

        # Step 3: main loop
        while frontier:
            current_x, current_y = random.choice(frontier)
            frontier.remove((current_x, current_y))

            neighbors = []

            for dx, dy in directions:
                nx = current_x + dx
                ny = current_y + dy

                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if maze[ny][nx] == 1:
                        neighbors.append((nx, ny))

            if not neighbors:
                continue

            neighbor_x, neighbor_y = random.choice(neighbors)

            # break wall
            middle_x = (current_x + neighbor_x) // 2
            middle_y = (current_y + neighbor_y) // 2

            maze[current_y][current_x] = 1
            maze[middle_y][middle_x] = 1

            # add NEW frontier cells
            for dx, dy in directions:
                fx = current_x + dx
                fy = current_y + dy

                if 0 <= fx < self.width and 0 <= fy < self.height:
                    if maze[fy][fx] == 0 and (fx, fy) not in frontier:
                        frontier.append((fx, fy))

        # Display
        if self.displayMaze:
            cv2.namedWindow("Maze", cv2.WINDOW_NORMAL)
            cv2.imshow("Maze", maze)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        img = maze * 255.0
        cv2.imwrite(self.path, img)

        return maze
