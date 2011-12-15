NUM_MAX = float("INF")
import random
import copy
import BaseEvolution
import Unit.RealCodedGAUnit

class RealCodedGA(BaseEvolution.BaseEvolution):
    def __init__(self,max_unit,max_repeat,costfunction,mutation_rate):
        BaseEvolution.BaseEvolution.__init__(self,max_unit,max_repeat,costfunction)
        self.mutation_rate = mutation_rate
        self.alpha = []
        for n in range(0,self.costfunction.rank):
            self.alpha.append(0.05)

    def construct(self):
        self.units = []
        for n in range(0,self.max_unit):
            self.units.append(
                Unit.RealCodedGAUnit.RealCodedGAUnit(
                    self.costfunction.rank,
                    self.costfunction.domain[1],
                    self.costfunction.domain[0]
                    )
                )


    def update(self):
        def brend_crossover(unit_a_xn,unit_b_xn,alpha):
            basing_point = unit_a_xn - alpha
            region = unit_b_xn - basing_point + 2*alpha
            addition = region * random.random()
            return basing_point + addition

        def boundary_mutation(unit_xn,domain,mutation_rate=0.5):
            if  mutation_rate < random.random():
                xn = unit_xn
            else:
                xn = random.choice(domain)
            return xn

        new_age = []
        for unit in self.units:
            new_one = Unit.RealCodedGAUnit.RealCodedGAUnit(
                self.costfunction.rank,
                self.costfunction.domain[1],
                self.costfunction.domain[0]
                )

            another_unit = random.choice(self.units)

            for index in range(0,len(unit.x)):
                new_one.x[index] = brend_crossover(unit.x[index],another_unit.x[index],self.alpha[index])
                new_one.x[index] = boundary_mutation(unit.x[index],self.costfunction.domain,self.mutation_rate)
            
            new_one.fit = self.costfunction.eval(*(new_one.x))
            if new_one.fit < unit.fit:
                new_age.append(copy.deepcopy(new_one))
            else:
                new_age.append(copy.deepcopy(unit))
        self.units = copy.deepcopy(new_age)
