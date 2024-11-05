import sys
from collections import deque
data = sys.stdin.read().strip().split("\n")
N, G  = map(int, data[0].split())
data = data[1:]
groups = [list(map(int, i.split()[1:])) for i in data]
groups.sort(key = lambda x: (len(x), x[0]))
queue = deque(groups)
s = set([groups[0][0]])
pre_len = len(queue)
while queue:
    i = queue.popleft()
    
    if len(set(i) - s) < 2:
        s = s.union(set(i))    
    
    else:
        queue.append(i)

    if pre_len == len(queue):
        break
    
    pre_len = len(queue)

print(len(s))