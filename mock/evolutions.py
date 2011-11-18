#when adding new evolution method, it most be child of evocop.
#evocop is an interface class. 
#unit = [fitness,x1,x2,x3.......]
import random
import copy
import sys
import threading

class unit():
    def __init__(self,rank,max,min):
        def _rand(max,min):
           return min + random.random() * (max - min)

        self.x = []
        for n in range(0,rank):
            xn = _rand(max,min)
            self.x.append(xn)
        self.fit = float("inf")
        
class evocop(): #threading.Thread):
    def __init__(self,costfunction):
        #threading.Thread.__init__(self)
        self.numrep = 100
        self.numunit = 10
        self.repcount = 0
        self.log = []
        self.units = []
        self.costfunction = costfunction

    def destruct(self):
        que = []
        for units in self.log:
            us = []
            for unit in units:
                x1 = unit.x[0]
                x2 = unit.x[2]
                fitness = unit.fit
                us.append({"x1":x1,"x2":x2,"fitness":fitness})
                que.append(us)
        return que

    def update(self):
        print 'no method: %(name)s'%{"name":self.update.__name__}
        exit

    def is_end(self):
       return self.repcount > self.numrep

    def run(self):
        self.construct()
        while not self.is_end():
            self.repcount = self.repcount + 1
            self.update()
            self.logging()
        return self.destruct()
    
    def logging(self):
        self.log.append(copy.deepcopy(self.units))

class randunit(unit):
    def __init__(self,rank,max,min):
        unit.__init__(self,rank,max,min)
        self.r = random.random

class random_compute(evocop):
    def __init__(self,costfunction):
 
        evocop.__init__(self,costfunction)

    def construct(self):
        self.units = []
        for n in range(0,self.numunit):
            self.units.append(
                randunit(
                    self.costfunction.rank,
                    self.costfunction.domain[1],
                    self.costfunction.domain[0]
                    )
                )
            
    def update(self):
        newage = []
        for unit in self.units:
            sun  = randunit(
                self.costfunction.rank,
                self.costfunction.domain[1],
                self.costfunction.domain[0]
                )
            sun.fit = self.costfunction.eval(*(sun.x))
            if unit.fit < sun.fit:
                newage.append(unit)
            else:
                newage.append(sun)
        self.units = newage
            
