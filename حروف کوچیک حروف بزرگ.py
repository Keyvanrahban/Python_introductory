def low_counter(a):
    l_counter = 0
    lo = a.lower()
    for i in range(0, int(len(a))):
        if a[i] == lo[i]:
            l_counter += 1
    return l_counter


def up_counter(b):
    u_counter = 0
    up = a.upper()
    for j in range(0, int(len(a))):
        if a[j] == up[j]:
            u_counter += 1
    return u_counter


a = input("")
vaziat = True

if low_counter(a) == up_counter(a):
    vaziat = True
if low_counter(a) > up_counter(a):
    vaziat = True
if low_counter(a) < up_counter(a):
    vaziat = False

if vaziat:
    a = a.lower()
else:
    a = a.upper()
print(a)
