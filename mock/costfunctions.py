import random

class BaseCostfunction():
    def __init__(self,rank):
        self.domain = (0,0)
        self.rank = rank

    def eval(*arg):
        pass

class doublex(BaseCostfunction):
    def __init__(self,rank):
        BaseCostfunction.__init__(self,rank)
        self.domain = (0,100)

    def eval(self,*arg):
        sum = 0
        for n in range(0,self.rank):
            sum = sum + arg[n] * arg[n]
        return sum
