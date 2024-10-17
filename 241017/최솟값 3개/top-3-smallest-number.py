import heapq
N = int(input())
numbers = list(map(int, input().split()))
q = []
for num in numbers:
    heapq.heappush(q, num)
    if len(q) < 3:
        print(-1)
    else:
        a = heapq.heappop(q)
        b = heapq.heappop(q)
        c = heapq.heappop(q)
        heapq.heappush(q, a)
        heapq.heappush(q, b)
        heapq.heappush(q, c)
        print(a*b*c)