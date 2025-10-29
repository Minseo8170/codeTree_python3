total = 0
cnt = 0
while 1:
    a = int(input())
    if a >= 30 or a < 20:
        break
    total += a
    cnt += 1
print(f"{total/cnt:.2f}")