start, end = map(int, input().split())

# Please write your code here.
cnt = 0
for i in range(start, end+1):
    cnt_2 = 0
    for j in range(1, i+1):
        if i % j == 0:
            cnt_2 += 1
    if cnt_2 == 3:
        cnt += 1
print(cnt)