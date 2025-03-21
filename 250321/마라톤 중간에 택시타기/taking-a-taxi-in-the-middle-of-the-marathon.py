n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]
L = [0]*(n)
R = [0]*(n)

L[0] = float('inf')
R[-1] = float('inf')
for i in range(1, n):
    L[i] = min(L[i-1], abs(x[i-1] - x[i]) + abs(y[i-1] - y[i]))

for i in range(n-2, -1, -1):
    R[i] = min(R[i+1], abs(x[i+1] - x[i]) + abs(y[i+1] - y[i]))
# Please write your code here.

L[0] = 0
L[-1] = 0
R[0] = 0
R[-1] = 0 

max_idx = 0
max_value = 0
for i in range(n):
    if max_value < L[i]:
        max_value = L[i]
        max_idx = i
    
    if max_value < R[i]:
        max_value = R[i]
        max_idx = i


answer = 0
prev = 0 

for cur in range(1, n):
    if cur == max_idx+1:
        continue
    answer += abs(x[prev] - x[cur])
    answer += abs(y[prev] - y[cur])
    prev = cur
print(L, R)
print(answer)
