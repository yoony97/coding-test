from sortedcontainers import SortedDict
n = int(input())
d = SortedDict()
for i in range(n):
    ops = input().split()
    if ops[0] == 'add':
        d[int(ops[1])] = int(ops[2])
    if ops[0] == 'remove':
        d.pop(int(ops[1]))
    if ops[0] == 'find':
        if int(ops[1]) in d:
            print(d[int(ops[1])])
        else:
            print("None")
    if ops[0] == 'print_list':
        if d:
            print(' '.join([str(k) for k in d.values()]))
        else:
            print("None")