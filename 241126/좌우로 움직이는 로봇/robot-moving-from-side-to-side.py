N, M = map(int, input().split())

MAX_LEN = 70#1000000
OFFSET = MAX_LEN//2
A = [(0,0)]
B = [(0,0)]

for i in range(N):
    t, d = input().split()
    t = int(t)
    for _ in range(t):
        A_t, position = A[-1]        
        if d == 'R':
            A.append((A_t+1, position+1))    
        else:
            A.append((A_t+1, position-1))

for i in range(M):
    t, d = input().split()
    t = int(t)
    for _ in range(t):
        B_t, position = B[-1]        
        if d == 'R':
            B.append((B_t+1, position+1))    
        else:
            B.append((B_t+1, position-1))

cnt = 0
prev_A = 0
prev_B = 0
while True:
    if (not A) and (not B):
        break
    if A:
        A_t, A_p = A.pop(0)
        prev_A = A_p
    if B:
        B_t, B_p = B.pop(0)
        prev_B = B_p
    print(f"At={A_t}: {A_p}, Bt={B_t}:{B_p}")
    if A_p == B_p and ((prev_A != A_p) or (prev_B != B_p)):
        print("matching!")
        cnt+=1

print(cnt-1)