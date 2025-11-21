arr = [
    list(map(int, input().split()))
    for _ in range(2)
]

for i in range(2):
    print(f"{sum(arr[i]) / 4:.1f}", end=' ')
print()

for i in range(4):
    sum_num = 0
    for j in range(2):
        sum_num += arr[j][i]
    print(f"{sum_num / 2:.1f}", end=' ')
print()

result = 0
for i in range(2):
    result += sum(arr[i])
print(f"{result / 8:.1f}")
