n = int(input())
arr = list(map(int, input().split()))
result = [0] * 10
for i in arr:
    result[i] += 1
for i in range(1, 10):
    print(result[i])