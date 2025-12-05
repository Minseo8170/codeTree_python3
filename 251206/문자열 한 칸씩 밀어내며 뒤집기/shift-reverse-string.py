input_str, q = input().split()
q = int(q)
queries = [int(input()) for _ in range(q)]

# Please write your code here.
for i in queries:
    if i == 1:
        input_str = input_str[1:] + input_str[0]
    elif i == 2:
        input_str = input_str[-1] + input_str[:-1]
    else:
        s = input_str
        input_str = ''
        for i in range(len(s)-1, -1, -1):
            input_str += s[i]
    print(input_str)