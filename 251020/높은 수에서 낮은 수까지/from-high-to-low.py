A, B = map(int, input().split())
if A < B:
    tmp = A
    A = B
    B = tmp
for i in range(A, B-1, -1):
    print(i, end=' ')