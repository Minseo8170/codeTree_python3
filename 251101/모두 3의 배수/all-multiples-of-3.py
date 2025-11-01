cnt = 0
for _ in range(5):
    a = int(input())
    if a % 3 == 0:
        cnt += 1
print(1) if cnt == 5 else print(0)