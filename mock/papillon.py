import sys
sys.path.append("./libpapillon") 

import Costfunction
import Evolution
       
c = Costfunction.costfunctions.doublex(4)
e = Evolution.ParticalSwarmOptimization.ParticalSwarmOptimization(10,1000,c,0.8,0.99,0.99)
#e = Evolution.RandomCompute.RandomCompute(50,1000,c)
e.run() 

#print e.to_string()
#print "\n"
print e.get_best().fit


