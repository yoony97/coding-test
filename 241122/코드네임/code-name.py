import sys

class people:
    def __init__(self, name, score):
        self.n = name
        self.s = score

inputs = sys.stdin.read().strip().split("\n")
ps = []
for inp in inputs:
    na, sc = inp.split()
    ps.append(people(na,sc))

min_idx = 0
for i in range(len(ps)):
    if ps[min_idx] > ps[i].s:
        min_idx = i

print(ps[min_idx].n, ps[min_idx].s)
