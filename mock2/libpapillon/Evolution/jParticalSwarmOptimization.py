NUM_MAX = float("INF")

import random
import copy
import Unit.ParticalSwarmOptimizationUnit
import BaseEvolution

class ParticalSwarmOptimization(BaseEvolution.BaseEvolution):
    def __init__(self,max_unit,max_repeat,costfunction,w=0.3,c1=0.3,c2=0.3,f=0.5,cr=0.5):
        BaseEvolution.BaseEvolution.__init__(self,max_unit,max_repeat,costfunction)
        self.w = w
        self.c1 = c1
        self.c2 = c2
        self.unit_class = Unit.ParticalSwarmOptimizationUnit.ParticalSwarmOptimizationUnit
        self.F = f
        self.CR = cr

    def construct(self):
        self.units = []
        for n in range(0,self.max_unit):
            self.units.append(
                self.unit_class(
                    self.costfunction.rank,
                    self.costfunction.domain[1],
                    self.costfunction.domain[0]
                    )
                )

    def update(self):
        new_age = []
        best_all_unit = self.get_best();
        for unit in self.units:
            sun = Unit.ParticalSwarmOptimizationUnit.ParticalSwarmOptimizationUnit(
                    self.costfunction.rank,
                    self.costfunction.domain[1],
                    self.costfunction.domain[0]
                    )

            r = random.random
            w = self.w
            c1 = self.c1
            c2 = self.c2
            for index in range(0,len(unit.x)):
                sun.x[index] = unit.x[index] + unit.v[index]
                sun.v[index] = w*unit.v[index] + c1*r()*(unit.best["x"][index] - unit.x[index]) + c2*r()*(best_all_unit.x[index] - unit.x[index])

            sun.fit = self.costfunction.eval(*(sun.x))
            if sun.fit < unit.best["fit"]:
                sun.best["x"]   = copy.deepcopy(sun.x)
                sun.best["fit"] = copy.deepcopy(sun.fit)
            else:
                sun.best["x"]   = copy.deepcopy(unit.best["x"])
                sun.best["fit"] = copy.deepcopy(unit.best["fit"])
            new_age.append(copy.deepcopy(sun))
        self.units = copy.deepcopy(new_age)
        self.paramete_fit()

def paramete_fit(self):
    cr = random.random()
    f  = random.random()
    
    self.w  = f
    self.c1 = cr
    self.c2 = cr
    self.cr = cr
    self.f  = f
    
