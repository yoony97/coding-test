N, Q = map(int, input().split())
li = list(map(int, input().split()))
max_length = max(li)
lines = [0]*(max(li))
S = [0]*(max(li)+1)

for i in li:
    lines[i-1] = 1

for i in range(1, len(lines)+1):
    S[i] = S[i-1] + lines[i-1]

def get_sum(s,e):
    return S[e] - S[s-1]


for i in range(Q):
    s, e = map(int, input().split())
    if 0<= s <= max_length and 0 <= e <= max_length:
        print(get_sum(s,e))
    else:
        print(0)


#0 1 2 3 4 5 6 7
#0 0 1 1 0 1 0 1