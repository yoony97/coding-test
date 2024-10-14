from itertools import permutations
N = int(input())

d = {}

for i in range(N):
    isinclude = False
    key = ''.join(sorted(input()))
    if key in d:
        d[key] += 1
    else:
        d[key] = 1
print(max(d.values()))