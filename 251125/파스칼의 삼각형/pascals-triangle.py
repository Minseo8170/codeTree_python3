n = int(input())
arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for i in range(n):
    for j in range(i+1):
        if j == 0 or j == i:
            arr[i][j] = 1
        else:
            arr[i][j] = arr[i-1][j] + arr[i-1][j-1]
        print(arr[i][j], end=' ')
    print()
 