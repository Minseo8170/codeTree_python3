A = int(input())
for i in range(1, A+1):
    if (i % 4 != 0 and i % 2 == 0) or (i // 8) % 2 == 0 or i % 7 < 4:
        continue
    print(i, end=' ')