total = 0
cnt = 0
for i in range(10):
    a = int(input())
    if a >= 0 and a <= 200:
        total += a
        cnt += 1
print(f"{total} {total/cnt:.1f}")