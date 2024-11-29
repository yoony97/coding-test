N= int(input())
li = list(map(int, input().split()))

cnt = 0
for start in range(N):
    for end in range(start+1,N+1):
        s =  sum(li[start:end])
        m  = s / len(li[start:end])
        if float(m).is_integer() and int(m) in li:
            #print(li[start:end], m)
            cnt += 1

print(cnt)
