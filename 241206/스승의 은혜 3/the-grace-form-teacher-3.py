N, B = map(int, input().split())
li = []
for i in range(N):
    p, s = map(int, input().split())
    li.append((p,s))

li.sort(key = lambda x: x[0] + x[1])
ans = 0
for i in range(N):# i가 반값일 때,
    current = (li[i][0]//2, li[i][1])
    li[i] = (li[i][0]//2, li[i][1])
    li.sort(key = lambda x: x[0] + x[1])
    idx = li.index(current)
    total = 0
    cnt = 0
    for j in range(N):
        if total + li[j][0] + li[j][1] <= B:
            total += li[j][0] + li[j][1]
            cnt += 1
        else:
            ans = max(ans, cnt)
            
    li[idx] = (li[idx][0]*2, li[idx][1])

print(ans)