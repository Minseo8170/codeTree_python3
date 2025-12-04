s = input()
ss = s
for _ in range(len(s) - 1):
    n = int(input())
    if len(ss) <= n:
        ss = ss[:-1]
    else:
        ss = ss[:n] + ss[n+1:]
    print(ss)