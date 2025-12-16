n = int(input())

# Please write your code here.
def func(n):
    sum = 0
    for i in range(n+1):
        sum += i
    return sum//10

print(func(n))