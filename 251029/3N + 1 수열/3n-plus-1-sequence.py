N = int(input())
cnt = 0
while 1:
    if N == 1:
        print(cnt)
        break
    if N % 2 == 0:
        N /= 2
    else:
        N = N * 3 + 1
    cnt += 1