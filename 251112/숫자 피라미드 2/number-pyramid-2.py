n = int(input())
cnt = 0
for i in range(n):
    for _ in range(i+1):
        cnt += 1
        print(cnt, end=' ')
    print()