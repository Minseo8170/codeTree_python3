a, b = map(int, input().split())

# Please write your code here.
def count(a, b):
    cnt = 0
    for i in range(a, b+1):
        if i % 3 == 0:
            cnt += 1
        elif str(i).count('3') or str(i).count('6') or str(i).count('9'):
            cnt += 1
    return cnt

print(count(a, b))