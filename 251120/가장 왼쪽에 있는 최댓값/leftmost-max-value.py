n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
while n != 0:
    max_num = a[0]
    idx = 0
    for i in range(0, n):
        if a[i] > max_num:
            max_num = a[i]
            idx = i
        elif a[i] == max_num:
            max_num = a[i]
    print(idx + 1, end=' ')
    n = idx