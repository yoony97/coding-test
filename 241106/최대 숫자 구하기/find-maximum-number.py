import sys
from sortedcontainers import SortedSet


n, m = map(int, input().split())
s = SortedSet([i for i in range(1,m+1)])
li = list(map(int, input().split()))

for i in li:
    s.remove(i)
    print(s[-1])