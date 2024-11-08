import sys
from sortedcontainers import SortedSet


n, m = map(int, input().split())
s = SortedSet([i for i in range(n+1)])
li = list(map(int, input().split()))

def cal():
    max_len = 0
    current_len = 1
    if not s:  # SortedSet이 비어 있는 경우
        return 0

    for i in range(1, len(s)):
        # 연속된 숫자인지 확인
        if s[i] == s[i-1] + 1:
            current_len += 1
        else:
            max_len = max(max_len, current_len)
            current_len = 1

    max_len = max(max_len, current_len)
    return max_len


for num in li:
    s.remove(num)
    
    print(cal())
#이게 왜 TreeSet인가?

#계산하는 함수