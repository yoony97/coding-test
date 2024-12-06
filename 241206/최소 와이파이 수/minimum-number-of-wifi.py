n, m = map(int, input().split())
home = list(map(int, input().split()))

cnt = 0
dist = 0
ans = 0
for i in range(n):
    dist += 1

    if home[i] == 1:
        cnt += 1
    
    #cnt > 0 이고 
    if dist > 2*m and cnt > 0:
        dist = 0
        cnt = 0
        ans +=  1
    
print(ans)