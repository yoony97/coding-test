A, B, C = map(int, input().split())
MAX_ITER = 1001
ans = 0

for i in range(MAX_ITER):#A를 더한 횟수 i
    for j in range(MAX_ITER): #B를 더한 횟수 j
        s = A*i + B*j
        if s < C:
            ans = max(s, ans)

print(ans)