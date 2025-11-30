A = input()

# Please write your code here.
s = ""
cnt = 0
prev = A[0]
for i in A:
    if prev == i:
        cnt += 1
    else:
        s += prev
        s += str(cnt)
        prev = i
        cnt = 1

s += prev
s += str(cnt)

print(len(s), s, sep='\n')