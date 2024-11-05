import sys
from itertools import combinations

data = sys.stdin.read().strip().split("\n")
N, M = map(int, data[0].split())
idx = [i for i in range(M)]
data = data[1:]
A = data[:N]
B = data[N:]
cnt = 0
for i in combinations(idx, 3):
    pattern_a = set()
    pattern_b = set()
    
    for s in A:
        pattern_a.add((s[i[0]], s[i[1]], s[i[2]]))
    
    for s in B:
        pattern_b.add((s[i[0]], s[i[1]], s[i[2]]))
    
    if len(pattern_a.intersection(pattern_b)) == 0:
        cnt+=1

print(cnt)