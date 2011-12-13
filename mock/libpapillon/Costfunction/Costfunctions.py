#cost functions most be child of BaseCostfunction.BaseCostfunction
#the eval method most be define in chile class
import BaseCostfunction

class doublex(BaseCostfunction.BaseCostfunction):
    def __init__(self,rank):
        BaseCostfunction.BaseCostfunction.__init__(self,rank)
        self.domain = (0,100)

    def eval(self,*arg):
        sum = 0
        for n in range(0,self.rank):
            sum = sum + arg[n] * arg[n]
        return sum

class x(BaseCostfunction.BaseCostfunction):
    def __init__(self,rank):
        BaseCostfunction.BaseCostfunction.__init__(self,rank)
        self.domain = (0,100)

    def eval(self,*arg):
        sum = 0
        for n in range(0,self.rank):
            sum = sum + arg[n]
        return sum
