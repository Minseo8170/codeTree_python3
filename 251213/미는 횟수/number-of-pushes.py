s1 = input()
s2 = input()
for i in range(len(s1)+1):
    if s1 == s2:
        print(i)
        break
    s1 = s1[-1] + s1[:-1]
if i == len(s1):
    print(-1)