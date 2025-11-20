min_num = 1000
max_num = -1000
arr = list(map(int, input().split()))
for a in arr:
    if a == 999 or a == -999:
        break

    if a > max_num:
        max_num = a
    
    if a < min_num:
        min_num = a

print(max_num, min_num)