arr = [
    input()
    for _ in range(11)
]

flag = 0
for i in range(10):
    if arr[i][len(arr[i]) - 1] == arr[10]:
        print(arr[i])
        flag = 1

if flag == 0:
    print("None")