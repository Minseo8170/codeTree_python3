n, m = map(int, input().split())

# Please write your code here.
arr = [[0] * m] * n

for i in range(n):
    for j in range(m):
        if j % 2 == 0:
            print(j * n + i, end = ' ')
        else:
            print(j * n + n - 1 - i, end=' ')
    print()