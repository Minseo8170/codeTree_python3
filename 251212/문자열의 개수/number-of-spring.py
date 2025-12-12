s = input()
arr = []
cnt = 0
while s != '0':
    cnt += 1
    if cnt % 2 == 1:
        arr.append(s)
    s = input()
print(cnt)
for i in arr:
    print(i)