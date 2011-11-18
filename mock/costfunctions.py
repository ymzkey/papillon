import random

class costfunction():
    def __init__(self,rank):
        self.domain = (0,0)
        self.rank = rank

    def eval(*arg):
        pass


class doublex(costfunction):
    def __init__(self,rank):
        costfunction.__init__(self,rank)
        domain = (-100,100)

    def eval(self,*arg):
        sum = 0
        for n in range(0,self.rank):
            sum = sum + arg[n] * arg[n]
        return sum
