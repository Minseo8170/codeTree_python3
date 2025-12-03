s = input()
cnt1, cnt2 = 0, 0
for i in range(len(s)-1):
    if s[i] == 'e':
        if s[i+1] == 'e':
            cnt1 += 1
        elif s[i+1] == 'b':
            cnt2 += 1
print(cnt1, cnt2)