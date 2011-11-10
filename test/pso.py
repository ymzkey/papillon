import random
import copy
import sys
class evocop():
    def __init__(self):
        self.repcount = 0

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
    def __init__(self):
        evocop.__init__(self)

    def construct(self):
        self.num_unit = 10
        self.unit = {'x':0,'fitness':100}
        self.units = []
        self.result = []
        for x in range(0,self.num_unit):
            self.units.append(copy.copy(self.unit))
            

    def destruct(self):
        return self.units

    def fitness(self,x):
        return x * x

    def update(self):
        for unit in self.units:
            x = random.random()
            f = self.fitness(x)
            if unit['fitness'] < f:
                pass
            else:
                unit['x'] = x
                unit['fitness'] = f
            sys.stdout.write(str(unit['x']) + ' ')
            sys.stdout.write('\n')
        sys.stdout.write('\n')

                
    def is_end(self):
       return self.repcount > 100

ran = random_compute()
ran.run()
