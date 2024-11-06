from sortedcontainers import SortedSet
import sys


data = sys.stdin.read().strip().split("\n")
n, m = map(int, data[0].split())
li = list(map(int, data[1].split()))
s = SortedSet(li)
for i in data[2:]:
    idx = s.bisect_left(int(i))
    if idx < len(s):
        print(s[idx])
    else:
        print(-1)