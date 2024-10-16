import heapq
p = []
N, M = map(int, input().split())
for i in list(map(int, input().split())):
    heapq.heappush(p, -i)

for i in range(M):
    a = -heapq.heappop(p) -1
    heapq.heappush(p, -a)

print(-p[0])