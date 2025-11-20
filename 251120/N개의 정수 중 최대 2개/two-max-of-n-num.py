n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
first = -pow(2, 31)
second = pow(2, 31)-1

for i in a:
    if i >= first:
        second = first
        first = i
    elif second < i:
        second = i

print(first, second)