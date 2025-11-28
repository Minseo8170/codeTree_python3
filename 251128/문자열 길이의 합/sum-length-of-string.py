n = int(input())
arr = [
    input()
    for _ in range(n)
]

cnt_len = 0
cnt_a = 0
for i in arr:
    if i[0] == 'a':
        cnt_a += 1
    cnt_len += len(i)
print(cnt_len, cnt_a)