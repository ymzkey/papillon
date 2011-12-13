NUM_MAX = float("INF")

import copy
import Unit.RandomUnit
import BaseEvolution

class RandomCompute(BaseEvolution.BaseEvolution):
    def __init__(self,max_unit,max_repeat,costfunction):
        BaseEvolution.BaseEvolution.__init__(self,max_unit,max_repeat,costfunction)

    def construct(self):
        self.units = []
        for n in range(0,self.max_unit):
            self.units.append(
                Unit.RandomUnit.RandomUnit(
                    self.costfunction.rank,
                    self.costfunction.domain[1],
                    self.costfunction.domain[0]
                    )
                )
            
    def update(self):
        newage = []
        for unit in self.units:
            sun  = Unit.RandomUnit.RandomUnit(
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
