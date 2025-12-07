s = input()
cnt = 0
for i in s:
    if i >= '0' and i <= '9':
        cnt += int(i)
print(cnt)