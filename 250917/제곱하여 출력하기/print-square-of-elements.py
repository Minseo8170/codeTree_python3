N = int(input())
num = list(input().split())
squares = [int(n)**2 for n in num]
for n in squares:
    print(n, end=' ')