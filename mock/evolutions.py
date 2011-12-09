#when adding new evolution method, it most be child of libpappilon.BaseEvolution.
#evocop is an interface class. 
#unit = [fitness,x1,x2,x3.......]

import random
import copy
import sys
import threading
import libpapillon

class RandomUnit(libpapillon.BaseUnit):
    def __init__(self,rank,max,min):
        libpapillon.BaseUnit.__init__(self,rank,max,min)

class RandomCompute(libpapillon.BaseEvoluton):
    def __init__(self,max_unit,max_repeat,costfunction):
        libpapillon.BaseEvoluton.__init__(self,max_unit,max_repeat,costfunction)

    def construct(self):
        self.units = []
        for n in range(0,self.max_unit):
            self.units.append(
                RandomUnit(
                    self.costfunction.rank,
                    self.costfunction.domain[1],
                    self.costfunction.domain[0]
                    )
                )
            
    def update(self):
        newage = []
        for unit in self.units:
            sun  = RandomUnit(
                self.costfunction.rank,
                self.costfunction.domain[1],
                self.costfunction.domain[0]
                )
            sun.fit = self.costfunction.eval(*(sun.x))
            if unit.fit < sun.fit:
                newage.append(copy.deepcopy(unit))
            else:
                newage.append(copy.deepcopy(sun))
        self.units = newage
            
