s = input()
a1, a2 = s[0], s[1]
for i in s:
    if i == a1:
        print(a2, end='')
    elif i == a2:
        print(a1, end='')
    else:
        print(i, end='')