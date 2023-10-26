import math
from re import I
a = int(input())
pri = 'prime'

for i in range(2, int(math.sqrt(a))*1):
    if (a % i) == 0:
        pri = 'not prime'
        break

print(pri)
