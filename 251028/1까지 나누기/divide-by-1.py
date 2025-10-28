N = int(input()) 
i = 1
cnt = 0
while 1:
    cnt += 1
    N /= i
    if N <= 1:
        print(cnt)
        break
    i += 1