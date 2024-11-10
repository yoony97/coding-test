import heapq

# 입력:
n = int(input())
arr = list(map(int, input().split()))

# 변수 선언
sum_val = 0
max_avg = 0
pq = []

heapq.heappush(pq, arr[n - 1])
sum_val += arr[n - 1]
# k가 N - 2일 때부터 1일 때까지 거꾸로 탐색합니다.
# priority queue를 이용하여 진행합니다.
for i in range(n - 2, 0, -1):
    # 앞에서부터 K개를 삭제하고 나면
    # 뒤에 i ~ n - 1 까지의 숫자만이 남습니다.
    heapq.heappush(pq, arr[i])
    sum_val += arr[i]

    # 남아있는 정수 중 가장 작은 숫자를 찾아
    # 그 숫자를 제외한 평균을 구합니다.
    min_num = pq[0]
    avg = (sum_val - min_num) / (n - i - 1)

    # 평균이 최대가 된다면 정답을 현재 평균으로 갱신해줍니다.
    if max_avg < avg:
        max_avg = avg

# 평균값의 최대를 출력합니다.
print(f"{max_avg:.2f}")