from collections import deque
from constants import *

def solveMaze(maze, start, end):
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

    visited = [[False] * C for _ in range(R)]

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
            
        queue.append((nr, nc, dist + 1))
            
    for r, c in path:
        yield("path", r, c)

    return None