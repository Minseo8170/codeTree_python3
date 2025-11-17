result = [0] * 7
arr = list(map(int, input().split()))
for i in arr:
    result[i] += 1

for i in range(1, 7):
    print(f"{i} - {result[i]}")