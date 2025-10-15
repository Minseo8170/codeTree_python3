A, B, C = map(int, input().split())
if ((A > B) and (A < C)) or ((A < B) and (A > C)):
    print(A)
elif ((B > C) and (B < A)) or ((B < C) and (B > A)):
    print(B)
else:
    print(C)
