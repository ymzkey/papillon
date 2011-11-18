import evolutions
import costfunctions
import printer
import time
c = costfunctions.doublex(3)
e = evolutions.random_compute(c)
log = e.run()
print log
p = printer.Printer(log)
p.start()
