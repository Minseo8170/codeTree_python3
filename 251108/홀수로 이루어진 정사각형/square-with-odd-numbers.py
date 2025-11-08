n = int(input())
for i in range(11, 11+(n-1)*2+1, 2):
    for j in range(i, i+(n-1)*2+1, 2):
        print(j, end=' ')
    print()