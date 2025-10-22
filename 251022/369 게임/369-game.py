N = int(input())
i = 1
while i <= N:
    if i % 3 == 0 or i % 10 in {3, 6, 9} or i / 10 in {3, 6, 9}:
        print(0, end=' ')
    else:
        print(i, end=' ')
    i += 1