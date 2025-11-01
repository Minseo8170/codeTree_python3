N = int(input())
flag = True
for i in range(2, N//2 + 1):
    if N % i == 0:
        flag = False
        print('C')
        break
if flag:
    print('P')
