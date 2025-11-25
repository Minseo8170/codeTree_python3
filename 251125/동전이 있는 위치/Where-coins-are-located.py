n, m = map(int, input().split())
arr = []
for _ in range(m):
    arr.append(list(map(int, input().split())))

a = 0
for i in range(n):
    for j in range(n):
        if  a < m and arr[a][0] == i + 1 and arr[a][1] == j + 1:
            print(1, end=' ')
            a += 1
        else:
            print(0, end=' ')
    print()