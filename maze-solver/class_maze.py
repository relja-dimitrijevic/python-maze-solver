class Maze:

    def __init__(self, grid, start=None, end=None):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.start = start
        self.end = end

    def in_bounds(self, r, c):
        return 0 <= r < self.rows and 0 <= c < self.cols

    def is_wall(self, r, c):
        return self.grid[r][c] == 0

    def is_free(self, r, c):
        return self.grid[r][c] != 0

    def neighbors(self, r, c):
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        result = []

        for dr, dc in dirs:
            nr = r + dr
            nc = c + dc

            if self.in_bounds(nr, nc) and self.is_free(nr, nc):
                result.append((nr, nc))

        return result

    def print_ascii(self, start, end):
        for row in self.grid:
            line = ""
            for cell in row:
                if cell == 0:
                    line += "##"
                elif cell == 1:
                    line += "  "
                elif cell == 2:
                    line += "st"
                elif cell == 3:
                    line += "en"
            print(line)