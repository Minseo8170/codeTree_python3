n, m = map(int, input().split())

# Please write your code here.
def min_num(n, m):
    cnt = 0
    for i in range(1, n//2 + 1):
        if n % i == 0 and m % i == 0:
            cnt = i
    return cnt

if n > m:
    print(min_num(m, n))
else:
    print(min_num(n, m))