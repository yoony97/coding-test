import heapq

# 입력
N = int(input().strip())
bombs = [tuple(map(int, input().split())) for _ in range(N)]

# 시간 제한 기준으로 오름차순 정렬
bombs.sort(key=lambda x: x[1])

# 최대 점수 저장 변수 및 최대 힙 초기화
total_score = 0
max_heap = []

# 폭탄을 시간 제한 기준으로 순차적으로 처리
for score, limit_time in bombs:
    # 최대 힙에 점수 추가
    heapq.heappush(max_heap, score)
    
    # 해체 가능한 시간 초과 시 가장 점수가 낮은 폭탄 해제
    if len(max_heap) > limit_time:
        heapq.heappop(max_heap)

# 최대 힙에 남아있는 점수 합산
total_score = sum(max_heap)

print(total_score)
