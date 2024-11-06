from sortedcontainers import SortedSet
n, m = map(int, input().split())
li = list(map(int, input().split()))
s = SortedSet([i for i in range(1, m+1)]) #i번째 사람은 1번 이상 a_i번 이하의 의자에만 앉고 싶다
cnt = 0
for i in li:
    if not s:
        break
        
    idx = s.bisect_left(i)
    if idx == 0:
        if s[idx] != i:
            break
    s.remove(s[idx])
    cnt += 1

print(cnt)