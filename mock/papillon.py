import evolutions
import costfunctions

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
        
c = costfunctions.doublex(3)
e = evolutions.RandomCompute(10,100,c)
e.run() 
print e.to_string()

