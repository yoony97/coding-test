N, M = map(int, input().split())
li = list(map(int, input().split()))

def can_divide(max_sum):
    m = 1  # 초기 구간 개수 (구간 1개로 시작)
    s = 0  # 현재 구간의 합

    for num in li:
        if s + num > max_sum:  # 현재 구간에 추가할 수 없으면
            m += 1            # 새로운 구간 추가
            s = num           # 새로운 구간의 합 초기화
            if m > M:         # 구간 개수가 초과되면 실패
                return False
        else:
            s += num          # 현재 구간에 추가
    return True


for i in range(max(li), sum(li)):
    if can_divide(i):            
        print(i)
        break