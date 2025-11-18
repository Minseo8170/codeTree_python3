n, q = map(int, input().split())
arr = list(map(int, input().split()))
for _ in range(q):
    Q = list(input().split())
    Q1 = int(Q[1])

    if Q[0] == '1':
        print(arr[Q1-1])
    elif Q[0] == '2' and Q1 not in arr:
        print(0)
    elif Q[0] == '2':
        print(arr.index(Q1)+1)
    else:
        for i in range(Q1-1, int(Q[2]), 1):
            print(arr[i], end=' ')
        print()
