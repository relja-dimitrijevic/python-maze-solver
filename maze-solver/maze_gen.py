from backtracking import Backtracking

def generateMaze(algorithm, height, width, path, displayMaze):
    if algorithm == "backtracking":
        backtracking = Backtracking(height, width, path, displayMaze)
        return backtracking.createMaze()
    else:
        pass