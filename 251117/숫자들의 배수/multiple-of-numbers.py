n = int(input())
fin = False
if n == 5:
    print(5, 10)
else:
    for i in range(n, n * 10 + 1, n):
        if fin and i % 5 == 0:
            break
        print(i, end=' ')
        if i % 5 == 0:
            fin == True