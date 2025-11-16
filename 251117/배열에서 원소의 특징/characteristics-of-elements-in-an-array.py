arr = list(map(int, input().split()))
for i in range(10):
    if arr[i] % 3 == 0:
        break
print(arr[i-1])