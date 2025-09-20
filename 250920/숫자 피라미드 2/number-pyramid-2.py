N = int(input())
a = 1
b = 1
for i in range(1, N+1):
    for j in range(a, a+i):
        print(j, end=" ")
        b = j
    print()
    a = b+1
