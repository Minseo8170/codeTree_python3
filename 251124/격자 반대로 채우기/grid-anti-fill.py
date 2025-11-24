n = int(input())
arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

cnt = 1
for i in range(n - 1, -1, -1):
    if (n % 2 == 1 and i % 2 == 0) or (n % 2 == 0 and i % 2 == 1):
        for j in range(n - 1, -1, -1):
            arr[j][i] = cnt
            cnt += 1
    else:
        for j in range(n):
            arr[j][i] = cnt
            cnt += 1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()