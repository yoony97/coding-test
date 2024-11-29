N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt = 0

for i in range(N-M+1):
    isBeautiful = True
    for j in range(i, i+M):
        if A[j] not in B:
            isBeautiful  = False
            break
    
    if isBeautiful:
        cnt += 1

print(cnt)