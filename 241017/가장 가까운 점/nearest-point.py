import heapq

queue = []

#원점에서 가장 가까운 점을 하나 골라= abs
#x, y 값에 2씩 더해주는 작업을 m번

N, M = map(int, input().split())
for _ in range(N):
    x, y = map(int, input().split())
    heapq.heappush(queue, (abs(x) + abs(y), x, y))

for _ in range(M):
    _, x, y = heapq.heappop(queue)
    x, y = x+2, y+2
    heapq.heappush(queue, (abs(x)+abs(y), x, y))
_, x, y = heapq.heappop(queue)

print(x,y)