a, b, c = map(int, input().split())
yes = True
for i in range(a, b+1):
    if i % c == 0:
        print("YES")
        yes = False
        break
if yes:
    print("NO")