num = list(map(int, input().split()))
for i in range(2, 10):
    num.append((num[i-1]+num[i-2])%10)
for i in num:
    print(i, end=" ")