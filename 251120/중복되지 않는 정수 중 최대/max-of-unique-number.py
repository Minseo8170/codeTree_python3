n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
check = [0] * 1001
for i in nums:
    check[i] += 1

flag = True
for i in range(1000, 0, -1):
    if check[i] == 1:
        print(i)
        flag = False
        break
if flag:
    print(-1)