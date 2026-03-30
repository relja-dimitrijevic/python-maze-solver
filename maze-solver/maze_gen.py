from backtracking import Backtracking
from prims import Prims

def generateMaze(algorithm, height, width, path, displayMaze):
    if algorithm == "backtracking":
        backtracking = Backtracking(height, width, path, displayMaze)
        return backtracking.createMaze()
    elif algorithm == "prims":
        return Prims(height, width, path, displayMaze).createMaze()
    else:
        raise ValueError("Unknown algorithm")