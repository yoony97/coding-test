import sys
import heapq

data = sys.stdin.read().strip().split("\n")
n = int(data[0])
li = list(map(int, data[1:]))
queue = []

for i in range(n):
    if li[i] == 0:
        if not queue:
            print(0)
        else:
            print(-heapq.heappop(queue))
    else:
        heapq.heappush(queue, -li[i])