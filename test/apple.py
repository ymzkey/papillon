import randomevo
import printer

queue = []
r = randomevo.random_compute(queue)
p = printer.Printer(queue)
r.start()
p.start()
