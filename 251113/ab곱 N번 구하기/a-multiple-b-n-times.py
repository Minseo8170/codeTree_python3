n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    result = a
    for j in range(a+1, b+1):
        result *= j
    print(result)