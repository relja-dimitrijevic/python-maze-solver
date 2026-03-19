from collections import deque
from constants import *

def solveMaze(maze, start, end, algorithm):
    if algorithm == "bfs":
        return solve_bfs(maze, start, end)
    elif algorithm == "wall_follower":
        return solve_wall_follower(maze, start, end)
    else:
        raise ValueError("Unknown algorithm!")
    
def solve_bfs(maze, start, end):
    R = len(maze)
    C = len(maze[0])

    start_r = start[1]
    start_c = start[0]

    queue = deque()
    queue.append((start_r, start_c, 0))

    visited = [[False] * C for _ in range(R)]
    parent = {}

    Directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0)
    ]

    while len(queue) != 0:
        coord = queue.popleft()
        r, c, dist = coord

        if visited[r][c]:
            continue

        visited[r][c] = True

        yield("visit", r, c)

        if (r, c) == (end[1], end[0]):
            break

        for dr, dc in Directions:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < R and 0 <= nc < C:
                if not visited[nr][nc] and maze[nr][nc] != WALL:
                    queue.append((nr, nc, dist + 1))
                    parent[(nr, nc)] = (r, c)
            
    path = []
    current = (end[1], end[0])
    
    while current in parent:
        path.append(current)
        current = parent[current]
        
    path.reverse()
            
    for cell in path:
        yield("path", cell[0], cell[1])                        
            
    return None

def solve_wall_follower(maze, start, end):
    R, C = maze.shape

    # Directions: Right, Down, Left, Up (clockwise)
    directions = [
        (0, 1),   # right
        (1, 0),   # down
        (0, -1),  # left
        (-1, 0)   # up
    ]

    # Start position
    r, c = start[1], start[0]

    # Start facing right (you can change this)
    dir_idx = 0

    # Keep track of visited to avoid infinite loops
    visited = set()

    while (r, c) != (end[1], end[0]):

        visited.add((r, c))
        yield ("visit", r, c)

        # Try to turn LEFT first (left-hand rule)
        left_dir = (dir_idx - 1) % 4
        dr, dc = directions[left_dir]
        nr, nc = r + dr, c + dc

        if 0 <= nr < R and 0 <= nc < C and maze[nr][nc] != WALL:
            dir_idx = left_dir
            r, c = nr, nc
            continue

        # Otherwise try forward
        dr, dc = directions[dir_idx]
        nr, nc = r + dr, c + dc

        if 0 <= nr < R and 0 <= nc < C and maze[nr][nc] != WALL:
            r, c = nr, nc
            continue

        # Otherwise try right
        right_dir = (dir_idx + 1) % 4
        dr, dc = directions[right_dir]
        nr, nc = r + dr, c + dc

        if 0 <= nr < R and 0 <= nc < C and maze[nr][nc] != WALL:
            dir_idx = right_dir
            r, c = nr, nc
            continue

        # Otherwise turn back (dead end)
        back_dir = (dir_idx + 2) % 4
        dr, dc = directions[back_dir]
        nr, nc = r + dr, c + dc

        dir_idx = back_dir
        r, c = nr, nc

    # Mark final position
    yield ("visit", r, c)

    # No shortest path reconstruction — just show path taken
    return None