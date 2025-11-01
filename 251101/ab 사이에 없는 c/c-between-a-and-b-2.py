a, b, c = map(int, input().split())
flag = True
for i in range(a, b+1):
    if i % c == 0:
        print("NO")
        flag = False
        break;
if flag:
    print("YES")