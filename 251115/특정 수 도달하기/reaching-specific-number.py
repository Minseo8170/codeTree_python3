n = list(map(int, input().split()))
total = 0
for i in range(10):
    if n[i] >= 250:
        break;
    total += n[i]
print(f"{total} {total/i:.1f}")
