import random
import copy
import BaseUnit

class RandomUnit(BaseUnit.BaseUnit):
    def __init__(self,rank,max,min):
        BaseUnit.BaseUnit.__init__(self,rank,max,min)
