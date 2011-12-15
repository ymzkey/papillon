#when adding new evolution method, it most be child of libpappilon.BaseEvolution.
#evocop is an interface class. 
#unit = [fitness,x1,x2,x3.......]
NUM_MAX = float("INF")

import BaseUnit

class RealCodedGAUnit(BaseUnit.BaseUnit):
    def __init__(self,rank,max,min):
        BaseUnit.BaseUnit.__init__(self,rank,max,min)
