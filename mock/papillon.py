import sys
sys.path.append("./libpapillon") 

import Costfunction
import Evolution
       

c = Costfunction.costfunctions.doublex(20)
e = Evolution.ParticalSwarmOptimization.ParticalSwarmOptimization(30,10000,c,0.4,0.99,0.99)
#e = Evolution.RandomCompute.RandomCompute(20,500,c)
#e = Evolution.RealCodedGA.RealCodedGA(20,500,c,0.2)
e.run() 

#print e.to_string()
#print "\n"
#print "%10.10f"%(e.get_best().fit)


