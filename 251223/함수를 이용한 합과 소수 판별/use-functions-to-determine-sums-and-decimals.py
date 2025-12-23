a, b = map(int, input().split())

# Please write your code here.
def sosu(i):
    for j in range(2, i // 2):
        if i % j == 0:
            return False
    return True

def even(i):
    s = str(i)
    tmp = 0
    for j in s:
        tmp += int(j)
    if tmp % 2 == 0:
        return True
    else:
        return False

cnt = 0
for i in range(a, b+1):
    if sosu(i):
        if even(i):
            cnt += 1

print(cnt)