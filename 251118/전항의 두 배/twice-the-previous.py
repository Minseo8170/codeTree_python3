arr = list(map(int, input().split()))
print(arr[0], arr[1], end=' ')
for i in range(8):
    arr.append(arr[i+1] + 2 * arr[i])
    print(arr[i+2], end=' ')