a = input()
b = a.replace(a[1], 'a', 1)
c = b.replace(a[-2], 'a', 1)
print(c)