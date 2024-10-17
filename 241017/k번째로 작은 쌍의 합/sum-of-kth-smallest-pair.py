import heapq
import sys

data = sys.stdin.read().strip().split("\n")

N, M, K = map(int, data[0].split())
q = []
for i in list(map(int, data[1].split())):
    for j in list(map(int, data[2].split())):
        heapq.heappush(q, (i+j, i,j))

for i in range(K):
    s, x, y = heapq.heappop(q)

print(s)