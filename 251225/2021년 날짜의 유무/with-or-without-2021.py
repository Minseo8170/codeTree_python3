M, D = map(int, input().split())

# Please write your code here.
eight = [2]
zero = [4, 6, 9, 11]
one = [1, 3, 5, 7, 8, 10, 12]
if D <= 28:
    print("Yes")
elif D == 31 and one.count(M):
    print("Yes")
elif D == 30 and (one.count(M) or zero.count(M)):
    print("Yes")
else:
    print("No")

