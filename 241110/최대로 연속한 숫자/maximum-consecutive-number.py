from sortedcontainers import SortedList

def find_longest_consecutive(n, m, removes):
    active_intervals = SortedList([(0, n)])  # 초기 구간: (0, n)
    results = []
    
    for remove in removes:
        # 구간 내에서 삭제할 위치 찾기
        idx = active_intervals.bisect_right((remove,)) - 1
        if idx < 0:
            continue  # 유효한 구간이 없으면 건너뜀
        
        start, end = active_intervals[idx]
        
        # 삭제된 숫자가 포함된 구간이 맞는지 확인
        if not (start <= remove <= end):
            results.append(end - start + 1)
            continue
        
        # 기존 구간을 분할하여 제거
        active_intervals.pop(idx)
        
        # 좌우로 새로운 구간 추가
        if start < remove:
            active_intervals.add((start, remove - 1))
        if remove < end:
            active_intervals.add((remove + 1, end))
        
        # 현재 가장 긴 구간 찾기
        max_length = max(e - s + 1 for s, e in active_intervals)
        results.append(max_length)
    
    return results

# 입력
n, m = map(int, input().split())
removes = list(map(int, input().split()))

# 결과 계산 및 출력
results = find_longest_consecutive(n, m, removes)
for result in results:
    print(result)