#선두가 몇번이 바뀌는지 찾아 출력하는 프로그램을 작성해보세요.
#각각 시뮬레이션, 배열로  li[time] = position
# A[time] - B[time]을 저장 후 에 부호가 바뀌면, 선두가  바뀌는 것
N, M = map(int, input().split())
MAX_T = 50
A = [0]*(MAX_T+1)
B = [0]*(MAX_T+1)
current_t = 0
for i in range(N):
    v, t = map(int, input().split())
    for _ in range(t):
        current_t += 1
        A[current_t] = A[current_t-1] + v

current_t = 0

for i in range(M):
    v, t = map(int, input().split())
    for _ in range(t):
        current_t += 1
        B[current_t] = B[current_t-1] + v

cnt = 0
for i in range(1, MAX_T):
    if ((A[i-1] - B[i-1]) >= 0 and (A[i] - B[i]) < 0)  or ((A[i-1] - B[i-1]) <= 0 and (A[i] - B[i]) > 0 ):
        cnt += 1
print(cnt-1)

