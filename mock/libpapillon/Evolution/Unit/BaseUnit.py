import random

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
