N, K = map(int, input().split())
max_len = 20#W10000
li = [0]*(max_len+1)
for i in range(N):
    p, flag = input().split()
    if flag == 'G':
        li[int(p)-1] = 1
    if flag == 'H':
        li[int(p)-1] = 2
    
ans =  0
#print(li)
for i in range(max_len-K):
    val = 0
    for j in range(i, i+K+1):
        val += li[j]
    ans =  max(ans, val)
print(ans)