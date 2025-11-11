a, b = map(int, input().split())
for i in range(1, 10):
    for j in range(b, a-1, -1):
        if j % 2 == 0:
            print(j, '*', i, '=', j*i, end='')
            if j != a and j != a+1:
                print(' / ', end='')
    print()