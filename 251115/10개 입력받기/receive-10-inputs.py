n = list(map(int, input().split()))
cnt = 0
total = 0
for i in n:
    if i == 0:
        break
    cnt += 1
    total += i
print(f"{total} {total/cnt:.1f}")
