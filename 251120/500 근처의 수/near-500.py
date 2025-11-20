arr = list(map(int, input().split()))
over = 1001
low = 0
for i in arr:
    if i > 500 and i < over:
        over = i
    if i < 500 and i > low:
        low = i

print(low, over)