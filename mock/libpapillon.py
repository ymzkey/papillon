import random
import copy
import threading

class BaseCostfunction():
    def __init__(self,rank):
        self.domain = (float("inf"),float("inf"))
        self.rank = rank

    def eval(*arg):
        print "Warn: eval dose not exist"
        pass

class BaseUnit():
    def __init__(self,rank,max,min):
        def _rand(max,min):
           return float(min + random.random() * (max - min))

        self.x = []
        for n in range(0,rank):
            xn = _rand(max,min)
            self.x.append(xn)
        self.fit = float("inf")

    def to_list(self):
        def flatten(l):
            if type(l) == list:
                if len(l) == 1:
                    return flatten(l.pop(0))
                else:
                    return flatten(l.pop(0)) + flatten(l)
            else:
                return [l]
        return flatten([self.fit,self.x])

class BaseEvoluton(): #threading.Thread):
    def __init__(self,max_unit,max_repeat,costfunction):
        #threading.Thread.__init__(self)
        self.max_repeat = max_repeat
        self.max_unit = max_unit
        self.count_repeat = 0
        self.log = []
        self.units = []
        self.costfunction = costfunction

    def destruct(self):
        def flatten(l):
            if type(l) == list:
                if len(l) == 1:
                    return flatten(l.pop(0))
                else:
                    return flatten(l.pop(0)) + flatten(l)
            else:
                return [l]

        def unit_to_list(unit):
            return flatten([unit.fit,unit.x])

        return 0
        output = []
        for units in self.log:
            list_units = []
            for unit in units:
                list_units.append(unit_to_list(unit))
            output.append(list_units)
        return output

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
        return self.destruct()
    
    def logging(self):
        self.log.append(copy.deepcopy(self.units))

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

