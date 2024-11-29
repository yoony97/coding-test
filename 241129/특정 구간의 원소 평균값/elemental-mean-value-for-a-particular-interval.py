N= int(input())
li = list(map(int, input().split()))

cnt = 0
for start in range(N):
    for end in range(start+1,N):
        s =  sum(li[start:end])
        m  = s //len(li[start:end])
        if m in li:
            cnt += 1

print(cnt)