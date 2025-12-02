n = int(input())
arr = list(input().split())
s = ""
for i in arr:
    s += i
for i in range(0, len(s), 5):
    for j in range(i, i+5):
        if j >= len(s):
            break
        print(s[j], end='')
    print()
