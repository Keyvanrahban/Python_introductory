b = int(input())
a = int(input())
maxi = 0
maxi2 = 0
if a > b:
    maxi = a
    maxi2 = b
else:
    maxi = b
    maxi2 = a
while b != -1:
    b = int(input())
    if b > maxi:
        maxi2 = maxi
        maxi = b
print(maxi, '', maxi2)
