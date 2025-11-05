n = int(input())
for i in range(n):
    for _ in range(n-i-1):
        print(' ', end='')
    for j in range(i*2+1):
        if j % 2 == 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()
for i in range(n-1):
    for _ in range(i+1):
        print(' ', end='')
    for j in range((n-i-1)*2-1):
        if j % 2 == 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()