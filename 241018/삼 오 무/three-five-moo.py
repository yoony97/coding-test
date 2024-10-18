n = int(input())

left = 1
right = 10**9

def get_count(target):
    return target - (target // 3 + target // 5 - target // 15)

answer = -1

while left <= right:
    mid = (left + right) // 2
    if get_count(mid) >= n:  # n 이상인 경우를 찾음
        answer = mid  # 잠정적으로 저장
        right = mid - 1  # 더 작은 값이 있는지 탐색
    else:
        left = mid + 1

# 출력: 정확한 N번째 값 출력
print(answer)