n = int(input())
price = list(map(int, input().split()))

# Please write your code here.
result = 0
for i in range(n):
    for j in range(i, n):
        if price[j] - price[i] > result:
            result = price[j] - price[i]

print(result)