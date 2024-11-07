from sortedcontainers import SortedSet
import sys
data = sys.stdin.read().strip().split("\n")
n, m = map(int, data[0].split())
s = SortedSet(list(map(int, data[1:])))
minimum = float('inf')
#a > b+m
for num in data[1:]:
    num = int(num)
    idx = s.bisect_right(num+m)
    if idx < len(s):
        minimum = min(minimum, s[idx]- num)
if minimum == float('inf'):
    print(-1)
else:
    print(minimum)