import threading
import time

class add(threading.Thread):
    def __init__(self,v):
        threading.Thread.__init__(self)
        self.i = 0
        self.v = v

    def run(self):
        print "Start."
        while True:
            self.i += 1
            print self.v
            if self.i == 20: break



if __name__ == "__main__":
    t1 = Test(2)
    t2 = Test(3)
    t1.start()
    t2.start()
