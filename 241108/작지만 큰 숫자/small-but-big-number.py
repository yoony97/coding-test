import sys
from sortedcontainers import SortedSet
inputs = sys.stdin.read().strip().split("\n")
n, m = map(int, inputs[0].split())
el = SortedSet()
for i in inputs[1].split():
    el.add(-int(i))
query = list(map(int, inputs[2].split()))


for i in query:
    idx = el.bisect_left(-i)
    if len(el) == idx or -el[idx] > i:
        print(-1)
    else:
        print(-el[idx])
        el.remove(el[idx])