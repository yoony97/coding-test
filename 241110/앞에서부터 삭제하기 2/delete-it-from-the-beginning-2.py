import heapq
from sortedcontainers import SortedList
N = int(input())
li = list(map(int, input().split()))
idx_h = []
value_h = []
removed_items = set()
answer = 0 


for idx, i in enumerate(li):
    heapq.heappush(idx_h, (idx, i))
    heapq.heappush(value_h, (i, idx))

def pop_by_value():
    while value_h:
        value, idx = heapq.heappop(value_h)
        if (idx, value) not in removed_items:
            return idx, value

def pop_by_idx():
    while idx_h:
        idx, value = heapq.heappop(idx_h)
        if (idx, value) not in removed_items:
            removed_items.add((idx,value))
            return idx, value

while len(idx_h) > 1:
    total = 0
    cnt = 0
    _, _ = pop_by_idx() #원소 제거
    idx, value = pop_by_value() #최솟값 제거
    for v, i in value_h:
        if (i, v) not in removed_items:
            print(v, end=' ')
            total += v
            cnt += 1
    print("")
    heapq.heappush(value_h,(value, idx))
    if cnt != 0:
        answer = max(answer, total/cnt)

print('%.2f' %answer)