text = input()
pattern = input()

# Please write your code here.
flag = False
for i in range(len(text) - len(pattern) + 1):
    if text[i:i+len(pattern)] == pattern:
        print(i)
        flag = True
        break
if not flag:
    print(-1)