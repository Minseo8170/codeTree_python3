Y, M, D = map(int, input().split())

# Please write your code here.
zero = [4, 6, 9, 11]
season = ["Winter", "Winter", "Winter", 
    "Spring", "Spring", "Spring",
    "Summer", "Summer", "Summer", 
    "Fall", "Fall", "Fall"]

flag = 0
if Y % 4 == 0:
    if Y % 100 == 0 and Y % 400 == 0:
        flag = 1
    elif Y % 400 == 0:
        flag = 0
    else:
        flag = 1
else:
    flag = 0

if M == 2 and D > 28 + flag:
    print(-1)
elif zero.count(M) and D > 30:
    print(-1)
else:
    print(season[M % 12])