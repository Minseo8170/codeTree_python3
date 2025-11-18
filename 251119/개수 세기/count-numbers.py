n, m = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
for i in arr:
    if m == i:
        cnt += 1
print(cnt)