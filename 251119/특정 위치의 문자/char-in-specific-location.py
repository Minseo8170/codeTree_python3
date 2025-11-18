arr = ['L', 'E', 'B', 'R', 'O', 'S']
find = -1
a = input()
for i in range(6):
    if a == arr[i]:
        find = i
        break
if find == -1:
    print("None")
else:
    print(find)
