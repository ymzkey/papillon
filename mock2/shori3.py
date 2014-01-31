import sys
import copy
import math

argvs = sys.argv
filename = argvs.pop()

f = open(filename)
[uni,gene] = map((lambda x : int(x)),f.readline().rstrip().split(" "))

age = []
for i in range(gene):
    units = []
    x = []
    for j in range(uni):
        units.append(map((lambda x : float(x)),f.readline().rstrip().split(" ")))
        #print f.readline().rstrip().split(" ")

    age.append(copy.deepcopy(units))
    f.readline()#yomitobashi

# age > units[] > unit([fit,x1,x2....])

min_fits = [] 
for units in age:
    fits = []
    for unit in units:
        fits.append(unit[0])
    min_fits.append(min(fits))

for element in min_fits:
    print element

f.close()
