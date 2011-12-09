import evolutions
import costfunctions
import time

def log_to_string(log):
    history = ""
    for age in log:
        for unit in age:
            for data  in unit:
                history += "%(data)f"%{'data':data}
                history += " "
            history += "\n"
        history += "\n"
    return history
        
c = costfunctions.doublex(2)
e = evolutions.RandomCompute(100,100,c)
log = e.run()
print log_to_string(log)

