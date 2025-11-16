n = int(input())
arr = [i for i in range(n, n * 10 + 1, n)]
flag = False
for i in arr:
    print(i, end=' ')
    if not flag and i % 5 == 0:
        flag = True
    elif flag and i % 5 == 0:
        break
