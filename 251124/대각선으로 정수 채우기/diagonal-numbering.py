n, m = map(int, input().split())

# Please write your code here.
arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]
x, y = 0, 0
for i in range(1, n * m + 1):
    arr[x][y] = i
    if x + 1 >= n or y - 1 < 0:
        y += x + 1
        x = 0
        if y >= m:
            x = y - m + 1
            y = m - 1
    else:
        x += 1
        y -= 1

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()