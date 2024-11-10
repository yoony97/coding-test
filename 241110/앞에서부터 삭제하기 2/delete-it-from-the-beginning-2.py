import heapq
from sortedcontainers import SortedList
N = int(input())
li = list(map(int, input().split()))
h = []
answer = 0 

def get_li(h):
    return SortedList([i[1] for i in h])

for idx, i in enumerate(li):
    heapq.heappush(h, (idx, i))

while h:
    heapq.heappop(h)
    temp = get_li(h)[1:]
    if len(temp) > 0:
        answer = max(answer, sum(temp) / len(temp))
        
print('%.2f' %answer)