N = int(input())
arr = [
    [i for i in range(1, N+1)]
    for _ in range(N)
]

for i in range(N):
    if i % 2 == 1:
        for j in range(N-1, -1, -1):
            print(arr[i][j], end='')
    else:
        for j in range(N):
            print(arr[i][j], end='')
    print()