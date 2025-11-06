n = int(input())
for i in range(1, n+1):
    if i % 2 == 0:
        print('* ' * (n-int(i / 2) + 1))
    else:
        print('* ' * (int(i / 2) + 1))
for i in range(n, 0, -1):
    if i % 2 == 0:
        print('* ' * (n-int(i / 2) + 1))
    else:
        print('* ' * (int(i / 2) + 1))