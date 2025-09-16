A, B, C = map(int, input().split())
if A > B:
    X = A
    A = B
    B = X
if B > C:
    X = B
    B = C
    C = X
if A > B:
    X = A
    A = B
    B = X

print(B)
