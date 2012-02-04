NUM_MAX = float("inf")

import BaseCostfunction

class Sphere(BaseCostfunction.BaseCostfunction):
    def __init__(self,rank):
        BaseCostfunction.BaseCostfunction.__init__(self,rank)
        self.domain = (-5.12,5.12)

    def eval(self,*arg):
        sum = 0
        for n in arg:
            sum = sum + n * n
        return sum

