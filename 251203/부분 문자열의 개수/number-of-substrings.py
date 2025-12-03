s = input()
sb = input()
cnt = 0
for i in range(len(s)-1):
    if s[i] == sb[0] and s[i+1] == sb[1]:
        cnt += 1
print(cnt)