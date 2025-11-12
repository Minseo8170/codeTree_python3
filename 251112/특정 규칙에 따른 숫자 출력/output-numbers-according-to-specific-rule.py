n = int(input())
cnt = 1
for i in range(n, 0, -1):
    for j in range(n, 0, -1):
        if j <= i:
            print(cnt, end=' ')
            cnt += 1
            if cnt == 10:
                cnt = 1
        else:
            print(' ', end=' ')
    print()