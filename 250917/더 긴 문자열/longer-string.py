a, b = input().split()
if len(a) > len(b):
    print(f"{a} {len(a)}")
elif len(a) == len(b):
    print("same")
else:
    print(f"{b} {len(b)}")