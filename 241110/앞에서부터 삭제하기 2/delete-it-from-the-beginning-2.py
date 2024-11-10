from sortedcontainers import SortedList

N = int(input())
li = list(map(int, input().split()))

max_average = float('-inf')  # 최대 평균값 초기화

# K를 1부터 N-2까지 순회
for K in range(1, N - 1):
    # SortedList로 앞에서 K개 제거한 나머지 리스트 관리
    remaining_list = SortedList(li[K:])  # 앞에서 K개를 제거한 리스트
    
    # 최솟값을 제거하고 평균 계산
    min_value = remaining_list.pop(0)  # 최솟값 제거
    total = sum(remaining_list)
    count = len(remaining_list)
    
    # 평균 계산 및 최대 평균값 갱신
    average = total / count
    max_average = max(max_average, average)

# 결과 출력
print(f"{max_average:.2f}")