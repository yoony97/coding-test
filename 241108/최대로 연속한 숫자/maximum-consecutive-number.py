import sys
from sortedcontainers import SortedSet

n, m = map(int, input().split())
s = SortedSet([i for i in range(n+1)])
li = list(map(int, input().split()))

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
    s.remove(num)
    print(cal())