s = input()
for i in s:
    if i >= '0' and i <= '9':
        print(i, end='')
    elif i >= 'a' and i <= 'z':
        print(i, end='')
    elif i >= 'A' and i <= 'Z':
        print(chr(ord(i) + (ord('a') - ord('A'))), end='')