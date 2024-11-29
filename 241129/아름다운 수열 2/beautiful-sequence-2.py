N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
sB = set(B)
cnt = 0

for i in range(N-M+1):
    #isBeautiful = True
    
    sA = set(A[i:i+M])
    #print(i, i+M, sA)
    if sA == sB:
        cnt += 1
    
print(cnt)