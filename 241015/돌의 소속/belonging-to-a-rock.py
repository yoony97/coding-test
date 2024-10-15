N, Q = map(int, input().split())
number1 = [0]*N
number2 = [0]*N
number3 = [0]*N

for i in range(N):
    s = int(input())
    if s == 1:
        number1[i] = 1
    if s == 2:
        number2[i] = 1
    if s == 3:
        number3[i] = 1


group1 = [0]*(N+1)
group2 = [0]*(N+1)
group3 = [0]*(N+1)

for i in range(1, N+1):
    group1[i] = group1[i-1] + number1[i-1]
    group2[i] = group2[i-1] + number2[i-1]
    group3[i] = group3[i-1] + number3[i-1]

def get_sum(s,e, S):
    return S[e] - S[s-1]

for i in range(Q):
    s, e = map(int, input().split())
    print(get_sum(s,e, group1), get_sum(s,e, group2), get_sum(s,e, group3))