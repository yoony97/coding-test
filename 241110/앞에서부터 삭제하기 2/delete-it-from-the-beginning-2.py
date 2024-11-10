import heapq
from sortedcontainers import SortedList

N = int(input())
li = list(map(int, input().split()))

# 두 힙과 SortedList 선언
idx_h = []
value_h = []
sorted_values = SortedList()
answer = 0 

# 힙과 SortedList에 초기값 삽입
for idx, i in enumerate(li):
    heapq.heappush(idx_h, (idx, i))
    heapq.heappush(value_h, (i, idx))
    sorted_values.add(i)

def pop_by_value():
    while value_h:
        value, idx = heapq.heappop(value_h)
        if (idx, value) in idx_h:
            sorted_values.remove(value)
            return idx, value
    return None, None

def pop_by_idx():
    while idx_h:
        idx, value = heapq.heappop(idx_h)
        if (value, idx) in value_h:
            sorted_values.remove(value)
            return idx, value
    return None, None

# 최솟값을 제거하면서 평균 계산
while len(idx_h) > 1:
    _, _ = pop_by_idx() # idx 기준으로 최솟값 제거
    idx, value = pop_by_value() # value 기준으로 최솟값 제거
    
    if idx is None or value is None:
        break
    
    # 평균 계산
    if len(sorted_values) > 0:
        current_avg = sum(sorted_values) / len(sorted_values)
        answer = max(answer, current_avg)
    
    # 최솟값 복원
    heapq.heappush(value_h, (value, idx))
    sorted_values.add(value)

# 결과 출력
print('%.2f' % answer)