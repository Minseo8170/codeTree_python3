arr = list(map(int, input().split()))
sum_1 = 0
sum_2 = 0
for i in range(10):
    if i % 2 == 0:
        sum_2 += arr[i]
    else:
        sum_1 += arr[i]
print(abs(sum_1 - sum_2))