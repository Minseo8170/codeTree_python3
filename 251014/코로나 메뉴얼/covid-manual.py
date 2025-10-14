a = list(map(str, input().split()))
b = list(map(str, input().split()))
c = list(map(str, input().split()))
d = [a, b, c]
cnt = 0

for i in range(3):
    if d[i][0] == 'Y':
        if int(d[i][1]) >= 37:
            cnt += 1;

if cnt >= 2:
    print('E')
else:
    print('N')