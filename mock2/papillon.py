import sys
sys.path.append("./libpapillon") 

import Costfunction.Costfunctions
import Costfunction
import Evolution

c = Costfunction.Costfunctions.doublex(5)
e = Evolution.ParticalSwarmOptimization.ParticalSwarmOptimization(100,2000,c,0.2,0.3,0.9)
#e = Evolution.RandomCompute.RandomCompute(100,50000,c)
#e = Evolution.RealCodedGA.RealCodedGA(100,500,c,0.05)
e.run() 

#print e.to_string()
#print "\n"
#print "%10.10f"%(e.get_best().fit)


