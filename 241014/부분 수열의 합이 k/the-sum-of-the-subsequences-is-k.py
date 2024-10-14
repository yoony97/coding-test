n, k = map(int, input().split())
li = list(map(int, input().split()))
S = [0]*(n+1)

for i in range(1, n+1):
    S[i] = S[i-1] + li[i-1]

def get_sum(s, e):
    return S[e] - S[s-1]
ans = 0 
for i in range(1, n+1):
    for j in range(1,n+1):
        if k == get_sum(i, j):
            ans += 1

print(ans)