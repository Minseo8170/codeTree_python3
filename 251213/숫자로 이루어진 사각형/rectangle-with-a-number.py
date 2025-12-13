n = int(input())

# Please write your code here.
def print_num(n):
    for i in range(n):
        for j in range(i * n, i * n + n):
            print(j % 9 + 1, end=' ')
        print()

print_num(n)