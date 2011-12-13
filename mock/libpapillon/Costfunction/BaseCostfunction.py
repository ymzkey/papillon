NUM_MAX = float("inf")

class BaseCostfunction():
    def __init__(self,rank):
        self.domain = (NUM_MAX,NUM_MAX)
        self.rank = rank

    def eval(*arg):
        print "Warn: eval dose not exist"
        pass
