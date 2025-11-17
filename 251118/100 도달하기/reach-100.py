n = int(input())
a = 1
print(a, n, end=' ')
while n < 100:
    tmp = n
    n = a + n
    a = tmp
    print(n, end=' ')