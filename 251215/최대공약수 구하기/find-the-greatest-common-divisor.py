n, m = map(int, input().split())

# Please write your code here.
def min_num(n, m):
    cnt = 0
    for i in range(1, 101):
        if i >= n or i >= m:
            break
        if n % i == 0 and m % i == 0:
            cnt = i
    return cnt

print(min_num(n, m))