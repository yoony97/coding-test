import sys

data = sys.stdin.read().strip().split("\n")
N = int(data[0])
ops = data[1:]

dic = dict()

for op in ops:
    op = op.split()
    if op[0] == 'add':
        key, value = int(op[1]), int(op[2])
        dic[key] = value
    elif op[0] == 'find':
        key = int(op[1])
        if key not in dic:
            print("None")
        else:
            print(dic[key])
    elif op[0] == 'remove':
        key = int(op[1])
        dic.pop(key)