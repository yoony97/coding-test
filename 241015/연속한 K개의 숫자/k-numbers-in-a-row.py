def get_sum(S, s,e):
    return S[e] - S[s-1]

N, K, B = map(int, input().split())
onumbers = list(range(1, N+1))
bnumbers = list(range(1, N+1))
oS = [0]*(N+1)
bS = [0]*(N+1)


li = []
for i in range(B):
    blank = int(input())
    bnumbers[blank-1] = 0
    li.append(blank)

for i in range(1, N+1):
    oS[i] = oS[i-1] + onumbers[i-1]
    bS[i] = bS[i-1] + bnumbers[i-1]

d = {}
for i in range(1,N-K+1):
    osum = get_sum(oS, i, i+K-1)
    bsum = get_sum(bS, i, i+K-1) 
    diff = osum - bsum
    if diff in li:
        if diff in d:
            d[diff] += 1
        else:
            d[diff] = 1
print(min(d.values()))