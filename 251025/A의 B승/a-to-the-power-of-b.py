A, B = map(int, input().split())
total = 1
for _ in range(B):
    total *= A
print(total)