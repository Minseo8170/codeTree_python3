s, n = input().split()
n = int(n)
for _ in range(n):
    a, b, c = input().split()
    if a == '1':
        b = int(b) - 1
        c = int(c) - 1
        s = s[:b] + s[c] + s[b+1:c] + s[b] + s[c+1:]
        print(s)
    else:
        for i in range(len(s)):
            if s[i] == b:
                s = s[:i] + c + s[i+1:]
            elif s[i] == c:
                s = s[:i] + c + s[i+1:]
        print(s)