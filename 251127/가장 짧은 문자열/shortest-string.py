a = input()
b = input()
c = input()

if len(a) > len(b):
    if len(b) > len(c):
        print(len(a) - len(c))
    elif len(a) > len(c):
        print(len(a) - len(b))
    else:
        print(len(c) - len(b))
else:
    if len(a) > len(c):
        print(len(b) - len(c))
    elif len(b) > len(c):
        print(len(b) - len(a))
    else:
        print(len(c) - len(a))
