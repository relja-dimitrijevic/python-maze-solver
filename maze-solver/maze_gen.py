from backtracking import Backtracking

def generate_maze(algorithm, height, width, path, displayMaze):
    if algorithm == "backtracking":
        backtracking = Backtracking(height, width, path, displayMaze)
        return backtracking.createMaze()
    else:
        pass