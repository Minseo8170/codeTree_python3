n = int(input())
cnt = 0
for _ in range(n):
    a = list(map(int, input().split()))
    if sum(a)/4 >= 60:
        print("pass")
        cnt += 1
    else:
        print("fail")
print(cnt)