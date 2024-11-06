from sortedcontainers import SortedSet
import sys
s = SortedSet()
data = sys.stdin.read().strip().split("\n")
n, m = map(int,data[0].split())
data = data[1:]
for i in range(n):
    p1, p2 = map(int, data[i].split())
    s.add((p1,p2))

data = data[n:]

for j in range(m):
    p1, p2 = map(int, data[j].split())
    idx = s.bisect_left((p1,p2))
    if idx >= len(s):
        print(-1,-1)
    else:
        print(s[idx][0], s[idx][1])