n, m = map(int, input().split())
maps =[]

for _ in range(n):
    maps.append(list(map(int, input().split())))

def count(cx,cy,k):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if 0 <= i < n and 0 <= j < n and abs(i - cx) + abs(j - cy) <= k:
                cnt += maps[i][j]
    return cnt
    
ans = 0
for k in range(n//2+1):
    gold = 0
    cost = k*k + (k+1)*(k+1)
    for cx in range(n):
        for cy in range(n):
            cnt = count(cx,cy,k)
            gold = max(cnt, gold)
    
    total = gold*m - cost
    if total >= 0:
        ans = max(ans, gold)

print(ans)

