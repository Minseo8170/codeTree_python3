A, B = map(int, input().split())
total = 1
for i in range(A, B+1):
    total *= i
print(total)