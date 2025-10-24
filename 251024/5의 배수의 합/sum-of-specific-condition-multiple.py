A, B = map(int, input().split())
total = 0
if A > B:
    tmp = A
    A = B
    B = tmp
for i in range(A, B+1):
    if i % 5 == 0:
        total += i
print(total)