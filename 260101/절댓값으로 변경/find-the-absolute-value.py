n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def func(i):
    return abs(i)

for i in arr:
    print(func(i), end=' ')