#when adding new evolution method, it most be child of libpappilon.BaseEvolution.
#evocop is an interface class. 
#unit = [fitness,x1,x2,x3.......]
NUM_MAX = float("INF")

import random
import copy
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
            
class ParticalSwarmOptimizationUnit(libpapillon.BaseUnit):
    def __init__(self,rank,max,min):
        self.INITIALI_SPEED = 0.0
        libpapillon.BaseUnit.__init__(self,rank,max,min)
        self.v = [] # This is not a abbreviation.  The speed value call "v"
        self.best = {"x":[],"fit":NUM_MAX}
        
        for index in range(0,rank):
            self.v.append(self.INITIALI_SPEED)
            self.best["x"].append(self.x[index])

class ParticalSwarmOptimization(libpapillon.BaseEvoluton):
    def __init__(self,max_unit,max_repeat,costfunction,w,c1,c2):
        libpapillon.BaseEvoluton.__init__(self,max_unit,max_repeat,costfunction)
        self.w = w
        self.c1 = c1
        self.c2 = c2

    def construct(self):
        self.units = []
        for n in range(0,self.max_unit):
            self.units.append(
                ParticalSwarmOptimizationUnit(
                    self.costfunction.rank,
                    self.costfunction.domain[1],
                    self.costfunction.domain[0]
                    )
                )

    def get_best(self):
        best_unit = None
        best_fitness = NUM_MAX
        for unit in self.units:
            if unit.fit <= best_fitness:
                best_unit = copy.deepcopy(unit)
        return best_unit
            
    def update(self):
        new_age = []
        best_all_unit = self.get_best();
        for unit in self.units:
            sun = ParticalSwarmOptimizationUnit(
                self.costfunction.rank,
                self.costfunction.domain[1],
                self.costfunction.domain[0]
                )
            r = random.random
            w = self.w
            c1 = self.c1
            c2 = self.c2
            for index in range(0,len(unit.x)):
                sun.x[index] = unit.x[index] + r()*100.0 - 50.0 
                sun.v[index] = w*unit.v[index] + c1*r()*unit.best["x"][index] + c2*r()*best_all_unit.x[index]

            sun.fit = self.costfunction.eval(*(sun.x))
            if unit.fit <= sun.fit:
                new_age.append(copy.deepcopy(unit))
            else:
                print "update"
                if sun.fit < unit.best["fit"]:
                    sun.best["x"]   = copy.deepcopy(sun.x)
                    sun.best["fit"] = copy.deepcopy(sun.fit)
                else:
                    sun.best["x"]   = copy.deepcopy(unit.best["x"])
                    sun.best["fit"] = copy.deepcopy(unit.best["fit"])
                new_age.append(copy.deepcopy(sun))
        self.units = new_age
