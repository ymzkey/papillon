import evolutions
import costfunctions
        
c = costfunctions.x(3)
e = evolutions.ParticalSwarmOptimization(3,100,c,0.5,0.5,0.5)
#e = evolutions.RandomCompute(10,100,c)
e.run() 

print e.to_string()

