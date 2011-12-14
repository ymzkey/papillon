import sys
sys.path.append("./libpapillon") 

import Costfunction
import Evolution
       
c = Costfunction.costfunctions.x(20)
#e = Evolution.ParticalSwarmOptimization.ParticalSwarmOptimization(5,1000,c,.8,1.0,1.0)
e = Evolution.RandomCompute.RandomCompute(5,1000,c)
e.run() 

#print e.to_string()
#print "\n"
print e.get_best().fit


