n = int(input())
for i in range(n):
    for j in range(i*n+1, i*n + n+1):
        print(j, end=' ')
    print()