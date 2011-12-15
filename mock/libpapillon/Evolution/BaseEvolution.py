NUM_MAX = float("INF")

import copy

class BaseEvolution():
    def __init__(self,max_unit,max_repeat,costfunction):
        #threading.Thread.__init__(self)
        self.max_repeat = max_repeat
        self.max_unit = max_unit
        self.count_repeat = 0
        self.log = []
        self.units = []
        self.costfunction = costfunction

    def destruct(self):
        return 0

    def update(self):
        print 'no method: %(name)s'%{"name":self.update.__name__}
        exit

    def is_end(self):
       return self.count_repeat > self.max_repeat

    def run(self):
        self.construct()
        while not self.is_end():
            self.count_repeat = self.count_repeat + 1
            self.update()
            self.logging()
            print self.get_best().fit #ki wo tsukete!
        return self.destruct()
    
    def logging(self):
        self.log.append(copy.deepcopy(self.units))

    def get_best(self):
        best_unit = None
        best_fitness = NUM_MAX
        for unit in self.units:
            if unit.fit <= best_fitness:
                best_fitness = unit.fit
                best_unit = copy.deepcopy(unit)
        return best_unit

    def to_string(self):
        history = ""
        for age in self.log:
            for unit in age:
                for data  in unit.to_list():
                    history += "%(data)f"%{'data':data}
                    history += " "
                history += "\n"
            history += "\n"
        return history

