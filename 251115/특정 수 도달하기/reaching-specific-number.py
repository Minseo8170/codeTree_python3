n = list(map(int, input().split()))
total = 0
cnt = 0
for i in range(10):
    if n[i] >= 250:
        break;
    cnt += 1
    total += n[i]
print(f"{total} {total/cnt:.1f}")
