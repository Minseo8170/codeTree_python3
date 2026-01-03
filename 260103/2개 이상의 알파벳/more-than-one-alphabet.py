A = input()

# Please write your code here.
arr = [ 0 for _ in range(26) ]
cnt = 0
for i in A:
    if arr[ord(i) - ord('a')] == 0:
        arr[ord(i) - ord('a')] += 1
        cnt += 1
if cnt == 1:
    print("No")
else:
    print("Yes")    