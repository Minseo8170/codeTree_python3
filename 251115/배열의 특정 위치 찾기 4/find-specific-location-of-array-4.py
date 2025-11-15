n = list(map(int, input().split()))
cnt = 0
total = 0
for i in n:
    if i == 0:
        break
    if i % 2 == 0:
        cnt += 1
        total += i
print(cnt, total)
