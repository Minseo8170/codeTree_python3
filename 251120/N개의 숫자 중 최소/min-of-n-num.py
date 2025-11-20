n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
min_num = [a[0], 1]

for i in a[1:]:
    if i == min_num[0]:
        min_num[1] += 1
    elif i < min_num[0]:
        min_num[0] = i
        min_num[1] = 1

print(min_num[0], min_num[1])