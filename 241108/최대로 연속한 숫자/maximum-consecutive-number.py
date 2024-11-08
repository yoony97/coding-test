import sys
from sortedcontainers import SortedSet


n, m = map(int, input().split())
s = SortedSet([i for i in range(n+1)])
li = list(map(int, input().split()))

#제거하는 함수
def cal():
    target = 1
    cnt = 0
    max_len = 0
    li = [s[0]]
    offset = 0
    for i in range(s[0]+1, s[-1]+1):
        i = i + offset
        if i== li[-1]+1 and i in s:
            li.append(i)
        else:
            max_len = max(len(li), max_len)
            idx = s.bisect_right(i)
            offset += 1
            if len(s) != idx:
                li = [s[idx]]
            else:
                return max_len

    return max_len




for num in li:
    s.remove(num)
    #idx = s.bisect_right(num)
    
    print(cal())
#이게 왜 TreeSet인가?

#계산하는 함수