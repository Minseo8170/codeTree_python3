A, B = map(int, input().split())
if (A < B):
    temp = A
    A = B
    B = temp
print(A-B)