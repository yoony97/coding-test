from sortedcontainers import SortedSet

n, k = map(int, input().split())
li = list(map(int, input().split()))
s = SortedSet(li)
for i in range(len(s)-1, len(s)-k-1, -1):
    print(s[i], end=" ")