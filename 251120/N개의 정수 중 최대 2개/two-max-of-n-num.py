n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
first = a[0]
second = a[0]

for i in a:
    if i >= first:
        second = first
        first = i
    elif second < i:
        second = i

print(first, second)