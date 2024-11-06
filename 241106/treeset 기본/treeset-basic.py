import sys
from sortedcontainers import SortedSet
s = SortedSet()

data = sys.stdin.read().strip().split("\n")
N = int(data[0])
data = data[1:]
for i in range(N):
    ops = data[i].split()
    if ops[0] == 'add':
        s.add(int(ops[1]))
    if ops[0] == 'remove':
        s.remove(int(ops[1]))
    if ops[0] == 'find':
        if int(ops[1]) in s:
            print('true')
        else:
            print('false')
    if ops[0] == 'lower_bound':
        idx = s.bisect_left(int(ops[1]))
        if idx >= len(s):
            print('None')
        else:
            print(s[idx])
        #print(s[idx])
    if ops[0] == 'upper_bound':
        idx = s.bisect_right(int(ops[1]))
        if idx >= len(s):
            print('None')
        else:
            print(s[idx])
    if ops[0] == 'largest':
        if s:
            print(s[-1])
        else:
            print("None")
    if ops[0] == 'smallest':
        if s:
            print(s[0])
        else:
            print("None")