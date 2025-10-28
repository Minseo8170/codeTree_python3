arr = ["Vacancy", "John", "Tom", "Paul", "Sam"]
while 1:
    a = int(input())
    if a > 4 or a < 1:
        print(arr[0])
        break
    print(arr[a])
