n, m = map(int, input().split())
result = [
    [0 for _ in range(n)]
    for _ in range(n)
]
for i in range(1, m+1):
    a, b = map(int, input().split())
    result[a-1][b-1] = i

for i in range(n):
    for j in range(n):
        print(result[i][j], end=' ')
    print()