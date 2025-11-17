count = [0] * 10
a, b = map(int, input().split())

while a > 1:
    count[int(a) % b] += 1
    a /= b

result = 0
for i in count:
    result += pow(i, 2)

print(result)