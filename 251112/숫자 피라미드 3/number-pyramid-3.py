n = int(input())
for i in range(n):
    for j in range(i+1, (i+1)*(i+1)+1, i+1):
        print(j, end=' ')
    print()