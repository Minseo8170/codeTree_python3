N = int(input())
i = 1
while i <= N:
    flag = False
    for j in range(0, len(str(i))):
        if str(i)[j] in {'3', '6', '9'}:
            flag = True
            break

    if i % 3 == 0 or flag:
        print(0, end=' ')
    else:
        print(i, end=' ')
    i += 1