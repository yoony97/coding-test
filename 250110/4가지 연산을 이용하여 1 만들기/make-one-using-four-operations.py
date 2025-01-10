from collections import deque
N = int(input())
q = deque([(N)])
cnt = [float('inf')]*(N+10)
cnt[N] = 0
answer = float('inf')

while q:
    num= q.popleft()    
    if num%3 == 0 and cnt[num//3] > cnt[num]+1:
        #나눠지고  현재 num%3의 연산횟수가 cnt[num]+1 보다 크면, 추가
        q.append((num//3))
        cnt[num//3] = cnt[num]+1
    if num%2 == 0 and cnt[num//2] > cnt[num]+1:
        q.append((num//2))
        cnt[num//2] = cnt[num]+1
    
    if cnt[num-1] > cnt[num]+1:
        q.append((num-1))
        cnt[num-1] = cnt[num]+1
    
    if num+1 < N+10  and cnt[num+1] > cnt[num]+1:
        q.append((num+1))
        cnt[num+1] = cnt[num]+1


print(cnt[1])