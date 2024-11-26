#각각 시뮬레이션 해주고, 사람이 매초마다 어느 위치에 있는지 기록해주면, 이 문제를 해결할 수 있다.
MAX_T = 1000*1000
A = [0]*(MAX_T+1)
B = [0]*(MAX_T+1)

n, m = map(int, input().split())
current_t = 0
current_p = 0
for i in range(n):
    d, t = input().split()
    t = int(t)
    if d == 'R':
        for j in range(current_t, t):
            current_p += 1
            A[j] = current_p
        current_t += t
    else:
        for j in range(current_t, t):
            current_p -= 1
            A[j] = current_p
        current_t += t

current_t = 0
current_p = 0

for i in range(m):
    d, t = input().split()
    t = int(t)
    if d == 'R':
        for j in range(current_t, t):
            current_p += 1
            B[j] = current_p
        current_t += t
    else:
        for j in range(current_t, t):
            current_p -= 1
            B[j] = current_p
        current_t += t
ans = 0
ismeet = False
for i in range(MAX_T):
    if A[i] == B[i]:
        ismeet = True
        ans = i
        break
if ismeet:
    print(ans)
else:
    print(-1)