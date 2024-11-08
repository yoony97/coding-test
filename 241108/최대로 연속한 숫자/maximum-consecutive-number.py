import sys
from sortedcontainers import SortedSet

# 입력 받기
n, m = map(int, input().split())
s = SortedSet()
li = list(map(int, input().split()))

# SortedSet을 동적으로 업데이트하여 메모리 사용 최적화
s.update(range(n + 1))  # 초기화 시 전체를 추가하지 않고 동적 업데이트

# 제거 후 가장 긴 연속된 숫자들의 길이를 구하는 함수
def cal():
    if not s:  # SortedSet이 비어 있는 경우
        return 0
    
    max_len = 0
    current_len = 1

    for i in range(1, len(s)):
        # 연속된 숫자인지 확인
        if s[i] == s[i-1] + 1:
            current_len += 1
        else:
            max_len = max(max_len, current_len)
            current_len = 1

    max_len = max(max_len, current_len)  # 마지막 연속 길이 체크
    return max_len

# li에 있는 숫자들을 순서대로 제거하고, 연속된 숫자의 최대 길이를 출력
for num in li:
    s.discard(num)  # 삭제 (존재하지 않는 경우에도 안전하게 수행)
    print(cal())