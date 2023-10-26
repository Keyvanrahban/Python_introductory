loghatnamee = {}
a = int(input(""))
for i in range(0, a):
    a, b = input().split(' ')
    loghatnamee[a] = b
khoroji = []
vaje = ''
jomle = input("")
li_jomle = jomle.split(" ")
for it in li_jomle:
    if it in loghatnamee.keys():
        pass
    else:
        loghatnamee[it] = it
for item in li_jomle:
    vaje = loghatnamee[item]
    khoroji.append(vaje)
print(' '.join(khoroji))
