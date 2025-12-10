a = input()
b = input()
A, B = "", ""
for i in a:
    if i >= '0' and i <= '9':
        A += i
for i in b:
    if i >= '0' and i <= '9':
        B += i
print(int(A) + int(B))        