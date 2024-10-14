from sortedcontainers import SortedDict

d = SortedDict()
n = int(input())

for i in range(n):
    s = input()
    if s in d:
        d[s] += 1
    else:
        d[s] = 1

for i in d:
    print(f"{i} {d[i]}")