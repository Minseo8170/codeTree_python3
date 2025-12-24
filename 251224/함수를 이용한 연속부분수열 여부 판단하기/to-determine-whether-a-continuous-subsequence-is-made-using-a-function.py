n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
flag = False
for i in range(n1 - n2 + 1):
    if a[i] == b[0]:
        for j in range(n2):
            if a[i + j] != b[j]:
                flag = False
                break
            flag = True
    if flag:
        print("Yes")
        break
if not flag:
    print("No")