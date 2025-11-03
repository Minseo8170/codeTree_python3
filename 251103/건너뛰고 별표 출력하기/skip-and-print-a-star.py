N = int(input())
for i in range(N):
    for _ in range(i+1):
        print('*', end='')
    print('\n')
for i in range(N-1, 0, -1):
    for _ in range(i):
        print('*', end='')
    print('\n')