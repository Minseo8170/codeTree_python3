arr = list(map(int, input().split()))
for i in range(len(arr)):
    if arr[i] == 0:
        break
print(arr[i-3] + arr[i-2] + arr[i-1])