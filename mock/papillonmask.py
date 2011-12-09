#convert log file to glaph
#log format
#number_line number_units rank
#m n 3
#x111 x112 x113 fitness x121 x122 x123 fitness ... x1n1 x1n2 x1n3 fitness
#x211 x212 x213 fitness x221 x222 x223 fitness ... x2n1 x2n2 x2n3 fitness
#                                 ...
#xmn1 xmn2 x213 fitness xmn1 xmn2 xmn3 fitness ... xmn1 xmn2 xmn3 fitness
#unit has only x,fitness.

#magic numbers
FOLAT_MAX = float("inf")


class Data():
    def __init__(self):
        self.x = []
        self.rank = 0
        self.fitness = FLOAT_MAX

class Analizer():
    def __init__(file):
        self.data_set = self.loadfile(file_name)
        
    def loadfile(self,file_name):
        def splitlLine(line):
            data = []
            return data

        file = []
        data_set = []

        for line in file:
            list = splitLine(line)
            data = 
            data_set.appned(data)

    def convert(self):
        pass
 
    def put_file(filename):
        
