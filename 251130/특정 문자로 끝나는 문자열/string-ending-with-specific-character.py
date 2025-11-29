cnt = 0
arr = [input()]
while len(arr[cnt]) != 1:
    arr.append(input())
    cnt += 1

flag = 0
for i in range(0, len(arr) - 1):
    if arr[i][len(arr[i]) - 1] == arr[len(arr) - 1]:
        print(arr[i])
        flag = 1
if flag == 0:
    print("None")