import sys
inputs = sys.stdin.read().strip().split("\n")
n = int(inputs[0])
lines = [tuple(map(int, i.split())) for i in inputs[1:]]
S = []

for i in lines:
    S.append((i[0], 1))
    S.append((i[1], -1))

S.sort()

overlap = 0
max_overlap = 0

for (p, s) in S:
    #print(overlap, p ,s)
    overlap += s
    max_overlap = max(max_overlap, overlap)

print(max_overlap+1)
