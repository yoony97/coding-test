from sortedcontainers import SortedSet

def find_longest_consecutive(n, m, removes):
    # 초기 상태에서 모든 숫자를 포함한 집합 생성
    active_numbers = SortedSet(range(n + 1))
    max_length = n + 1
    results = []

    for remove in removes:
        # 제거할 숫자를 집합에서 제거
        active_numbers.discard(remove)

        # 제거한 숫자의 좌우 이웃 숫자를 가져옴
        left_neighbor = active_numbers[active_numbers.bisect_left(remove) - 1] if active_numbers.bisect_left(remove) > 0 else None
        right_neighbor = active_numbers[active_numbers.bisect_right(remove)] if active_numbers.bisect_right(remove) < len(active_numbers) else None

        # 연속 구간의 길이 계산
        if left_neighbor is not None and right_neighbor is not None:
            current_length = right_neighbor - left_neighbor - 1
        elif left_neighbor is not None:
            current_length = remove - left_neighbor
        elif right_neighbor is not None:
            current_length = right_neighbor - remove
        else:
            current_length = 0

        # 최장 길이 업데이트
        max_length = max(max_length, current_length)
        results.append(max_length)

    return results

# 입력
n, m = map(int, input().split())
removes = list(map(int, input().split()))

# 결과 계산 및 출력
results = find_longest_consecutive(n, m, removes)
for result in results:
    print(result)