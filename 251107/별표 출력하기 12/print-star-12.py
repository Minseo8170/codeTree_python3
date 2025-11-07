n = int(input())
print('* ' * n)
for i in range(2, n+1):
    for j in range(1, n+1):
        if j % 2 == 0 and j >= i:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
