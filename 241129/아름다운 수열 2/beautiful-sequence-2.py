N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
B.sort()
cnt = 0

for i in range(N-M+1):
    sub = []
    for j in range(i, i+M):
        sub.append(A[j])
    sub.sort()
    
    isBeautiful = True
    for a, b in zip(sub, B):
        if  a != b:
            isBeautiful = False
            break
    
    if isBeautiful:
        cnt += 1

print(cnt)