s = input()
for i in s:
    if i >= 'a' and i <= 'z':
        print(i.upper(), end='')
    else:
        print(i.lower(), end='')