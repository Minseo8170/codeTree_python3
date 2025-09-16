A, B, C = map(int, input().split())
if A > B:
    if A < C:
        print(A)
    elif B < C:
        print(B)
    else:
        print(C)
else:
    if A > C:
        print(A)
    elif B < C:
        print(B)
    else:
        print(C)