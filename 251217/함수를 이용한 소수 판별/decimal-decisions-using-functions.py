a, b = map(int, input().split())

# Please write your code here.
def count(a, b):
    cnt = 0
    for i in range(a, b+1):
        flag = 1
        for j in range(2, i):
            if i % j == 0:
                flag = 0
                break
        if flag:
            cnt += i
    return cnt

print(count(a, b))