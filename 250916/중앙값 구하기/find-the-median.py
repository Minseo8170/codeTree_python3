A, B, C = map(int, input().split())
if A >= B and A <= C:
    print(A)
elif A <= B and B <= C:
    print(B)
else:
    print(C)
