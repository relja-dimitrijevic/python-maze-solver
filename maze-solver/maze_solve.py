from collections import deque

def solveMaze(maze, start, end):
    R = len(maze)
    C = len(maze[0])

    # convert (x,y) → (row,col)
    start_r = start[1]
    start_c = start[0]

    queue = deque()
    queue.append((start_r, start_c, 0))

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

        # reached end?
        if (c, r) == end:
            return dist

        for dr, dc in Directions:
            nr = r + dr
            nc = c + dc

            if nr < 0 or nr >= R or nc < 0 or nc >= C:
                continue

            if maze[nr][nc] == 0:
                continue

            if visited[nr][nc]:
                continue

            queue.append((nr, nc, dist + 1))

    return None