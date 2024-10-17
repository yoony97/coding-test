import heapq
N = int(input())
q = []
for num in list(map(int, input().split())):
    heapq.heappush(q, -num)

while len(q) >= 2:
    a = -heapq.heappop(q)
    b = -heapq.heappop(q)

    if a - b != 0:
        heapq.heappush(q, -(a-b))

print(-q[0])