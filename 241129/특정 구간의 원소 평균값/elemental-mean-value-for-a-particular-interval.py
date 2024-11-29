N= int(input())
li = list(map(int, input().split()))

cnt = 0
for start in range(N):
    for end in range(start,N+1):
        #print(start, end)
        s =  sum(li[start:end])
        l = len(li[start:end])
        if l == 0:
            l = 1
        m  = s / l
        if float(m).is_integer() and int(m) in li:
            #print(li[start:end], m)
            cnt += 1

print(cnt)
