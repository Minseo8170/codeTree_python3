A, B = map(int, input().split())

print(A//B, '.', sep='', end='')
i = 20
while i > 0:
    A = (A - A//B*B) * 10
    print(A//B, end='')
    i -= 1