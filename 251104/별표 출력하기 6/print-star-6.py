n = int(input())
for i in range(n, 0, -1):
    for _ in range((n-i)*2):
        print(' ', end='')
    for j in range((i*2-1) * 2 - 1):
        if j % 2 == 0:
            print('*', end='')
        else:
            print(' ', end='')    
    print()
for i in range(2, n+1):
    for _ in range((n-i)*2):
        print(' ', end='')
    for j in range((i*2-1) * 2 - 1):
        if j % 2 == 0:
            print('*', end='')
        else:
            print(' ', end='')    
    print()