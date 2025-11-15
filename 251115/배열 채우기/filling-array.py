n = list(map(int, input().split()))
for i in range(10):
    if n[i] == 0:
        break;
if n[i] != 0:
    i += 1
for j in range(i-1, -1, -1):
    print(n[j], end=' ')