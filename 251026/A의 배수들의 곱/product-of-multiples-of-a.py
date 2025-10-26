A, B = map(int, input().split())
total = 1
for i in range(1, B+1):
    if i % A == 0:
        total *= i
print(total)