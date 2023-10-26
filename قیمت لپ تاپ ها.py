n = int(input())
my_list = []


for i in range(n):
    data = input().split()
    my_list = my_list+[data]
    my_list.sort()

z = False
z1 = my_list.pop()

for i in my_list:
    z2 = my_list.pop()
    if int(z2[0]) < int(z1[0]) and int(z1[1]) < int(z2[1]):
        z = True
        break
    elif int(z2[0]) < int(z1[0]) and int(z1[1]) >= int(z2[1]):
        z1 = z2


if z:
    print('happy irsa')
else:
    print('poor irsa')
