import threading
import time

class Put(threading.Thread):
    def __init__(self,list):
        threading.Thread.__init__(self)
        self.l = list

    def run(self):
        print "put start."
        while True:
            print list
            if list == ["end"]:
                break

if __name__ == "__main__":
    i = 0
    list = []
    display = Put(list)
    display.start()
    while True:
        i = i+1
        list.append(i)
        time.sleep(0.1)
        if i > 9:
            list = ["end"]
            break

