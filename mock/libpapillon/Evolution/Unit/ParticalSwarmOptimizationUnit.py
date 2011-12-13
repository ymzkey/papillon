#when adding new evolution method, it most be child of libpappilon.BaseEvolution.
#evocop is an interface class. 
#unit = [fitness,x1,x2,x3.......]
NUM_MAX = float("INF")

import BaseUnit

class ParticalSwarmOptimizationUnit(BaseUnit.BaseUnit):
    def __init__(self,rank,max,min):
        self.INITIALI_SPEED = 0.0
        BaseUnit.BaseUnit.__init__(self,rank,max,min)
        self.v = [] # This is not a abbreviation.  The speed value call "v"
        self.best = {"x":[],"fit":NUM_MAX}
        
        for index in range(0,rank):
            self.v.append(self.INITIALI_SPEED)
            self.best["x"].append(self.x[index])
