N = int(input())
li = list(map(int, input().split()))

max_average = float('-inf')  # 최대 평균값 초기화

# K를 1부터 N-2까지 순회
for K in range(1, N - 1):
    remaining_list = li[K:]  # 앞에서 K개를 삭제한 리스트
    min_value = min(remaining_list)  # 남은 리스트에서 최솟값 찾기
    
    # 최솟값을 제외한 리스트 만들기
    remaining_list.remove(min_value)
    total = sum(remaining_list)
    count = len(remaining_list)
    
    # 평균 계산 및 최대 평균값 갱신
    average = total / count
    max_average = max(max_average, average)

# 결과 출력
print(f"{max_average:.2f}")