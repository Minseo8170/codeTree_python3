n = list(map(int, input().split()))

a = list(map(int, input().split()))
b = list(map(int, input().split()))

tmp = 0
flag = False
for i in a:
    if i == b[tmp]:
        tmp += 1
        if tmp == len(b):
            flag = True
            break
    else:
        tmp = 0

if flag:
    print("Yes")
else:
    print("No")