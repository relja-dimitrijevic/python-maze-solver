from collections import deque
from constants import *


def solveMaze(maze, start, end, algorithm):
    if algorithm == "bfs":
        return solveBFS(maze, start, end)
    elif algorithm == "wall_follower":
        return solveWallFollower(maze, start, end)
    else:
        raise ValueError("Unknown algorithm!")


def solveBFS(maze, start, end):
    R = len(maze)
    C = len(maze[0])

    start_row = start[1]
    start_col = start[0]

    queue = deque()
    queue.append((start_row, start_col, 0))

    visited = [[False] * C for _ in range(R)]
    parent = {}

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        row, col, dist = queue.popleft()

        if visited[row][col]:
            continue

        visited[row][col] = True
        yield ("visit", row, col)

        if (row, col) == (end[1], end[0]):
            break

        for dr, dc in directions:
            next_row = row + dr
            next_col = col + dc

            if 0 <= next_row < R and 0 <= next_col < C:
                if not visited[next_row][next_col] and maze[next_row][next_col] != WALL:
                    queue.append((next_row, next_col, dist + 1))
                    parent[(next_row, next_col)] = (row, col)

    # reconstruct path
    path = []
    current = (end[1], end[0])

    while current in parent:
        path.append(current)
        current = parent[current]

    path.append((start[1], start[0]))
    path.reverse()

    for row, col in path:
        yield ("path", row, col)


def solveWallFollower(maze, start, end):
    R, C = maze.shape

    parent = {}
    visited_states = set()

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right  # down  # left  # up

    row, col = start[1], start[0]
    direction_index = 0

    while (row, col) != (end[1], end[0]):

        # loop detection
        state = (row, col, direction_index)
        if state in visited_states:
            print("Loop detected — wall follower stuck")
            return None
        visited_states.add(state)

        yield ("visit", row, col)

        # --- LEFT ---
        left_index = (direction_index - 1) % 4
        dr, dc = directions[left_index]
        next_row = row + dr
        next_col = col + dc

        if 0 <= next_row < R and 0 <= next_col < C and maze[next_row][next_col] != WALL:
            prev = (row, col)
            row, col = next_row, next_col
            if (row, col) not in parent:
                parent[(row, col)] = prev
            direction_index = left_index
            continue

        # --- FORWARD ---
        dr, dc = directions[direction_index]
        next_row = row + dr
        next_col = col + dc

        if 0 <= next_row < R and 0 <= next_col < C and maze[next_row][next_col] != WALL:
            prev = (row, col)
            row, col = next_row, next_col
            if (row, col) not in parent:
                parent[(row, col)] = prev
            continue

        # --- RIGHT ---
        right_index = (direction_index + 1) % 4
        dr, dc = directions[right_index]
        next_row = row + dr
        next_col = col + dc

        if 0 <= next_row < R and 0 <= next_col < C and maze[next_row][next_col] != WALL:
            prev = (row, col)
            row, col = next_row, next_col
            if (row, col) not in parent:
                parent[(row, col)] = prev
            direction_index = right_index
            continue

        # --- BACK (SAFE) ---
        back_index = (direction_index + 2) % 4
        dr, dc = directions[back_index]
        next_row = row + dr
        next_col = col + dc

        if 0 <= next_row < R and 0 <= next_col < C:
            prev = (row, col)
            row, col = next_row, next_col
            if (row, col) not in parent:
                parent[(row, col)] = prev
            direction_index = back_index
        else:
            return None

    yield ("visit", row, col)

    # reconstruct path
    path = []
    current = (row, col)

    visited_path = set()

    while current in parent:
        if current in visited_path:
            break
        visited_path.add(current)
    
        path.append(current)
        current = parent[current]

    path.append((start[1], start[0]))
    path.reverse()

    for row, col in path:
        yield ("path", row, col)
        
    