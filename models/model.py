import numpy as np


class grid:
    def __init__(self,grid =np.zeros(shape=(6,7))):
        self.grid = grid
        self.rows = 6
        self.cols = 7 
    

    def printGrid(self):
        grid_str = ""
        for row in self.grid:
            grid_str += "| " + " | ".join(map(str, row)) + " |\n"
        
        return grid_str
        
    def isFull(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i, j] == 0.0:
                    return False
                
        return True
    
   
    


class Player:
    def __init__(self,idx,grid):
        self.idx = idx
        self.grid = grid
    

    
    

   






class Agent(Player):
    pass 
