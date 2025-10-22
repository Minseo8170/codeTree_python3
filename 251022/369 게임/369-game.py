N = input()
n = int(N)
i = 1
while i <= n:
    flag = False
    ten = 1
    for j in range(0, len(N)):
        if i % ten in {3, 6, 9}:
            flag = True
            break
        ten *= 10

    if i % 3 == 0 or flag:
        print(0, end=' ')
    else:
        print(i, end=' ')
    i += 1