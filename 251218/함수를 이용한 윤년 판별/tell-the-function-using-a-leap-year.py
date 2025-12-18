y = int(input())

# Please write your code here.
def yun(y):
    if y % 4 == 0:
        if y % 100 == 0 and y % 400 != 0:
            return "false"
        else:
            return "true"
    return "false"

print(yun(y))