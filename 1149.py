import sys

data = sys.stdin.read().strip().split("\n")

N = int(data[0])
element = data[1:]
count = 0
dps = [[0]*3 for i in range(N+1)]



init = list(map(int, element[0].split(" ")))
for idx, i in enumerate(init):
    dps[0][idx] = i


for idx, i in enumerate(element[1:]):
    data = list(map(int, i.split(" ")))
    for jdx in range(3):
        if jdx == 0:
            dps[idx+1][jdx] = min(dps[idx][1], dps[idx][2]) + data[jdx]
        elif jdx == 1:
            dps[idx+1][jdx] = min(dps[idx][0], dps[idx][2]) + data[jdx]
        elif jdx == 2:
            dps[idx+1][jdx] = min(dps[idx][0], dps[idx][1]) + data[jdx]

print(min(dps[N-1]))
