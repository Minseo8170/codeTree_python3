s = input()
for i in s:
    if i >= 'a' and i <= 'z' or i >= 'A' and i <= 'Z':
        if i <= 'Z':
            print(i, end='')
        else:
            print(chr(ord(i) - (ord('a') - ord('A'))), end='')