import sys
MAX_LEN = 1000000
inputs = sys.stdin.read().strip().split("\n")
N, M = map(int, inputs[0].split())
inputs = [tuple(map(int, i.split())) for i in inputs[1:]]
A = [0]*MAX_LEN
B = [0]*MAX_LEN
A_t = 0
B_t = 0
for i in inputs[:N]:
    v, t = i
    for _ in range(t):
        A_t += 1
        A[A_t] = A[A_t-1] + v

for i in inputs[N:]:
    v, t = i
    for _ in range(t):
        B_t += 1
        B[B_t] = B[B_t-1] + v
cnt = 0

for i in range(1,MAX_LEN):
    if A[i] > B[i] and not(A[i-1] > B[i-1]):
        cnt += 1
    if A[i] == B[i] and not(A[i-1] == B[i-1]):
        cnt += 1
    if A[i] < B[i] and not(A[i-1] < B[i-1]):
        cnt += 1

print(cnt-1)