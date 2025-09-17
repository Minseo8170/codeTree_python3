N = int(input())
num = list(map(int, input().split()))
num.reverse()
for i in num:
    if i%2 == 0:
        print(i, end=' ')