from constants import *
import cv2
import numpy as np

def Animate(maze, solver, end):
    
    display = maze.copy()
    scale = 15
    
    for action, r, c in solver:
        
        if action == "visit":
            if display[r][c] == FREE:
                display[r][c] = VISITED
            
        elif action == "path":
            display[r][c] = PATH
            
        display[end[1], end[0]] = END
                  
        img = Render(display)
        img = cv2.resize(
            img, 
            (img.shape[1] * scale, img.shape[0] * scale),
            interpolation = cv2.INTER_NEAREST)
    
        cv2.imshow("Maze Solver", img)
        cv2.waitKey(20)
        
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def Render(maze):
    h, w = maze.shape
    img = np.zeros((h, w, 3), dtype = np.uint8)
    
    for r in range(h):
        for c in range(w):
            
            if maze[r][c] == WALL:
                img[r, c] = (0, 0, 0)
                
            elif maze[r][c] == FREE:
                img[r, c] = (255, 255, 255)
            
            elif maze[r][c] == VISITED:
                img[r, c] = (255, 0, 0)
            
            elif maze[r][c] == PATH:
                img[r, c] = (0, 255, 0)
            
            elif maze[r][c] == START:
                img[r, c] = (0, 255, 255)
    
            elif maze[r][c] == END:
                img[r, c] = (0, 0, 255)
                
    return img