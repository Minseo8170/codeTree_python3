n = int(input())
arr = [
    [i * n - j for i in range(1, n+1)]
    for j in range(n-1, -1, -1)
]

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()