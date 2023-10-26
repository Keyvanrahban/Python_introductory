from math import sqrt

number_of_inputs = int(input())
sqrts = []
for i in range(0, number_of_inputs):
    sqrts.append(sqrt(float(input())))

for i in sqrts:
    print("%.4f" % (int(i * 10000)/10000))
