result = [0] * 10
arr = list(map(int, input().split()))
for i in arr:
    result[i//10] += 1

for i in range(1, 10):
    print(f"{i} - {result[i]}")
