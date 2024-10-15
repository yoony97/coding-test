def get_sum(S, s,e):
    return S[e] - S[s-1]

def count(numbers, s,e):
    count = 0
    for i in range(s-1, e):
        if numbers[i] != 0:
            count += 1
    return count


N, K, B = map(int, input().split())
original = list(range(1, N+1))
onumbers = list(range(1, N+1))
bnumbers = [0]*N
oS = [0]*(N+1)
bS = [0]*(N+1)
original_fix = [0]*(N+1)

for i in range(B):
    blank = int(input())
    bnumbers[blank-1] = blank
    onumbers[blank-1] = 0

for i in range(1, N+1):
    oS[i] = oS[i-1] + onumbers[i-1]
    bS[i] = bS[i-1] + bnumbers[i-1]
    original_fix[i] = original_fix[i-1] + original[i-1]

d = {}


answer = 99999999999

for i in range(1,N-K+1):
    o = get_sum(original_fix, i, i+K-1)
    osum = get_sum(oS, i, i+K-1)
    bsum = get_sum(bS, i, i+K-1) 
    
    if o == osum + bsum:
        answer = min(answer, count(bnumbers, i, i+K-1))
    
print(answer)