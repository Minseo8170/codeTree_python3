n = int(input())
for i in range(n * 2 + 1):
    if i % 2 == 1:
        print('*   ' * n + '*')
    else:
        print('* ' * (n * 2 + 1))