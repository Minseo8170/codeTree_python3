N = int(input())
arr_1 = [
    [i for i in range(1, N+1)]
    for _ in range(N)
]
arr_2 = [
    [0 for i in range(1, N+1)]
    for _ in range(N)
    ]

for i in range(N):
    if i % 2 == 1:
        for j in range(N):
            arr_2[N-j-1][i] = arr_1[i][j]
    else:
        for j in range(N):
            arr_2[j][i] = arr_1[i][j]

for i in range(N):
    for j in range(N):
        print(arr_2[i][j], end='')
    print()