n, m = map(int, input().split())

# Please write your code here.
def min_num(n, m):
    num = m
    while num % n != 0 or num % m != 0:
        num += 1
    return num

print(min_num(n, m))