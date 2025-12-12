n = int(input())
sum = 0
for _ in range(n):
    sum += int(input())
s = str(sum)
print(s[1:] + s[0])