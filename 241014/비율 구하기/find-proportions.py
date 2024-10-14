from sortedcontainers import SortedDict
n = int(input())
d = SortedDict()

for _ in range(n):
    s = input()
    if s in d:
        d[s] += 1
    else:
        d[s] = 1


for i in d:
    print(f'{i} {format(d[i]/n *100, ".4f")}')