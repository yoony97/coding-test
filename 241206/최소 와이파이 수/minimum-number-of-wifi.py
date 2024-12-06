n, m = map(int, input().split())
home = list(map(int, input().split()))

cnt = 0
dist = 0
ans = 0
if m == 0:
    print(sum(home))
else:    
    for i in range(n):
        dist += 1
        if home[i] == 1:
            cnt += 1
        if dist > 2*m:
            dist = 0
            cnt = 0
            ans += 1
    if cnt > 0:
        ans += 1

    print(ans)