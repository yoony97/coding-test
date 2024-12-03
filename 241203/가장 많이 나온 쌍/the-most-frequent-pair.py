N, M = map(int, input().split())
li = []
cnt = dict()
for i in range(M):
    a, b = map(int, input().split())
    if (a,b) in li:
        cnt[str(a)+str(b)] += 1
        
    elif (b,a) in li:
        cnt[str(b)+str(a)] += 1
    
    else:
        li.append((a,b))
        cnt[str(a)+str(b)] = 1

print(max([cnt[i] for i in cnt]))