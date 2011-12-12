#cost functions most be child of libpapillon.BaseCostfunction
#the eval method most be define in chile class
 
import libpapillon

class doublex(libpapillon.BaseCostfunction):
    def __init__(self,rank):
        libpapillon.BaseCostfunction.__init__(self,rank)
        self.domain = (0,100)

    def eval(self,*arg):
        sum = 0
        for n in range(0,self.rank):
            sum = sum + arg[n] * arg[n]
        return sum

class x(libpapillon.BaseCostfunction):
    def __init__(self,rank):
        libpapillon.BaseCostfunction.__init__(self,rank)
        self.domain = (0,100)

    def eval(self,*arg):
        sum = 0
        for n in range(0,self.rank):
            sum = sum + arg[n]
        return sum
