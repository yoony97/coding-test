N = int(input())
st = list(map(int, input()))

def calculate():
    min_dis = float('inf')
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if st[i] == st[j] == 1:
                min_dis = min(abs(i-j), min_dis)
    return min_dis

#print(calculate())                

ans = 0
#양 끝 중 1개라도 0인 경우를 고민해봐야한다.
if st[0] == 0:
    st[0] = 1
    ans = max(ans, calculate())
    st[0] = 0

if st[-1] == 0:
    st[-1] = 1
    ans = max(ans, calculate())
    st[-1] = 0

prev = 0
max_dis = 0
candidate = (0, N)
for i in range(1,N):
    if st[i] == 1:
        if max_dis < i - prev:
            candidate = (prev, i)
            max_dis = i - prev
        prev = i


st[sum(candidate)//2] = 1
#print(max_dis, candidate, ans)
ans = max(ans, calculate())
print(ans)


214 - 147
