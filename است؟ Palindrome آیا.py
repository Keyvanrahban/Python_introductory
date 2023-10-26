def palidrome(a):
    lenny = len(a)
    vaziat = True
    temp = a[::-1]
    for i in range(0, lenny):
        if a[i] != temp[i]:
            vaziat = False
    return vaziat


a = input("")
a = a.lower()

if palidrome(a):
    print('palindrome')
else:
    print('not palindrome')
