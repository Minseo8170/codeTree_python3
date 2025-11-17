a = list(input().split())
b = list(input().split())
c = list(input().split())
arr = [a, b, c]

result = [0] * 5

for i in range(3):
    if arr[i][0] == 'Y':
        if int(arr[i][1]) >= 37:
            result[0] += 1
        else:
            result[2] += 1
    else:
        if int(arr[i][1]) >= 37:
            result[1] += 1
        else:
            result[3] += 1

for i in range(4):
    print(result[i], end=' ')

if result[0] >= 2:
    print('E')