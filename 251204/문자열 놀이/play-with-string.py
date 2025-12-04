s, n = input().split()
arr = [
    i for i in s
]
n = int(n)
for _ in range(n):
    a, b, c = input().split()
    if a == '1':
        tmp = arr[int(b) - 1]
        arr[int(b) - 1] = arr[int(c) - 1]
        arr[int(c) - 1] = tmp
    else:
        for i in range(len(arr)):
            if arr[i] == b:
                arr[i] = c
    for i in arr:
        print(i, end='')
    print()
        