import random
import copy
import sys
import threading

class evocop(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.repcount = 0
        self.queue = queue

    def destruct(self):
        print 'no method'
        exit

    def update(self):
        print 'no method'
        exit

    def is_end(self):
        print 'no method'
        exit

    def fitness(self):
        print 'no method'
        exit

    def run(self):
        self.construct()
        while not self.is_end():
            self.repcount = self.repcount + 1
            self.update()
        return self.destruct()

class random_compute(evocop):
    def __init__(self,queue):
        evocop.__init__(self,queue)

    def construct(self):
        self.num_unit = 100
        def newunit():
            x = random.random()
            fitness = self.fitness(x)
            return {'x':x,'fitness':fitness}

        self.units = []
        self.result = []
        for x in range(0,self.num_unit):
            self.units.append(copy.copy(newunit()))
            

    def destruct(self):
        return self.units

    def fitness(self,x):
        return x*x

    def update(self):
        for unit in self.units:
            x = random.random()
            f = self.fitness(x)
            if unit['fitness'] < f:
                pass
            else:
                unit['x'] = x
                unit['fitness'] = f

        self.queue.append(copy.deepcopy(self.units))
                
    def is_end(self):
       return self.repcount > 1000

if __name__ == "__main__":
    queue = []
    ran = random_compute(queue)
    ran.start()
    print ran.queue
