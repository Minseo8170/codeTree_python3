M = int(input())
if M >= 3 and M <= 5:
    print("Spring")
elif M < 3 or M >= 12:
    print("Winter")
elif M >= 9:
    print("Fall")
else: 
    print("Summer")