n = int(input())
li = []
for i in range(n):
    ops = input().split()
    if len(ops) == 2:
        op, num = ops
    else:
        op = ops[0]
    if op == 'push_back':
        li.append(int(num))
    elif op == 'get':
        print(li[int(num)-1])
    elif op =='size':
        print(len(li))
    else:
        li.pop()