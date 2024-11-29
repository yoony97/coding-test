N, K = map(int,  input().split())
MAX_LEN = 200
candy = [0]*(MAX_LEN+1)

for _ in range(N):
    c,p = map(int,  input().split())
    candy[p] += c

ans = 0
#print(candy)
for i  in range(K,MAX_LEN-K+1):
    val  = 0
    for j in range(i-K, i+K+1):
        val +=  candy[j]
    #print(val, i-K, i+K+1)
    ans = max(val, ans)

print(ans)