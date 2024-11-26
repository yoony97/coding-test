N, M = map(int, input().split())
MAX_LEN = 5000*20
OFFSET = MAX_LEN//2
A = [0]*(MAX_LEN+1)
B = [0]*(MAX_LEN+1)

Aisited = [False]*(MAX_LEN+1)
Bisited = [False]*(MAX_LEN+1)


A_t = 0
B_t = 0

for i in range(N):
    t, d = input().split()
    t = int(t)
    for _ in range(t):
        A_t += 1
        if d == 'R':
            A[A_t] = A[A_t-1] + 1
        else:
            A[A_t] = A[A_t-1] - 1
        Aisited[A_t] = True
        


for i in range(M):
    t, d = input().split()
    t = int(t)
    for _ in range(t):
        B_t += 1
        if d == 'R':
            B[B_t] = B[B_t-1] + 1
        else:
            B[B_t] = B[B_t-1] - 1
        
        Bisited[B_t] = True

cnt = 1
#print(A,B)
for i in range(MAX_LEN):
    if A[i-1] != B[i-1] and A[i] == B[i] and (Bisited[i] and Aisited[i]):
        cnt += 1

print(cnt)

    

