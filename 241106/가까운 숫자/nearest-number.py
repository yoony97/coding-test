from sortedcontainers import SortedSet

s = SortedSet([0])
n = input()
li = list(map(int, input().split()))
minimum = 999999999
for i in li:
    s.add(i)
    idx = s.bisect_left(i)
    if idx + 1 < len(s):
        minimum = min(s[idx] - s[idx-1], s[idx+1] - s[idx], minimum)
    else:
        minimum = min(minimum, s[idx] - s[idx-1])
    print(minimum)