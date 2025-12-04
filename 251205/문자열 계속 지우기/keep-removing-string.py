A = input()
B = input()

# Please write your code here.
b = len(B)
while A.count(B):
    for i in range(len(A) - b + 1):
        if A[i:i+b] == B:
            A = A[:i] + A[i+b:]
            break
print(A)