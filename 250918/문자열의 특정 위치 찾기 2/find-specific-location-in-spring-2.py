list_s = ["apple", "banana", "grape", "blueberry", "orange"]
c = input()
cnt = 0
for s in list_s:
    if s[2] == c or s[3] == c:
        print(s)
        cnt += 1
print(cnt)