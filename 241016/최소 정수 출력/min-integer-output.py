import heapq

N = int(input())
p = []
for _ in range(N):
    num = int(input())
    if num == 0:
        if p:
            print(heapq.heappop(p))
        else:
            print(0)
    else:
        heapq.heappush(p, num)