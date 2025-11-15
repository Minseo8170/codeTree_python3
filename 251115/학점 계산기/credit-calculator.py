n = int(input())
total = 0
a = list(map(float, input().split()))
for i in a:
    total += i
print(f"{total/n:.1f}")
if total/n >= 4.0:
    print("Perfect")
elif total/n >= 3.0:
    print("Good")
else:
    print("Poor")