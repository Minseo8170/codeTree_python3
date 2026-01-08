n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
cnt = 0
while m >= 1:
    cnt += A[m - 1]
    if m % 2 == 0:
        m = m // 2
    else:
        m -= 1
print(cnt)