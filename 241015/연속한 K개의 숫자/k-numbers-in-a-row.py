def get_sum(S, s,e):
    return S[e] - S[s-1]

def preprocess(numbers):
    n = len(numbers)
    prefix = [0] * (n + 1)  # prefix[i]는 numbers[0]부터 numbers[i-1]까지의 0이 아닌 수 개수
    for i in range(n):
        prefix[i + 1] = prefix[i] + (1 if numbers[i] != 0 else 0)
    return prefix



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
    counting = preprocess(bnumbers)
    original_fix[i] = original_fix[i-1] + original[i-1]

d = {}


answer = 99999999999

for i in range(1,N-K+1):
    o = get_sum(original_fix, i, i+K-1)
    osum = get_sum(oS, i, i+K-1)
    bsum = get_sum(bS, i, i+K-1) 
    
    if o == osum + bsum:
        answer = min(answer, get_sum(counting, i, i+K-1))
    
print(answer)