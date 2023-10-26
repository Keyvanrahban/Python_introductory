def estandardsazi(a):
    a = a.lower()
    first = a[0]
    edame = a[1::]
    first = first.upper()
    return first+edame


list = []
for i in range(0, 10):
    temp = estandardsazi(input())
    list.append(temp)
for j in range(0, 10):
    print(list[j])
