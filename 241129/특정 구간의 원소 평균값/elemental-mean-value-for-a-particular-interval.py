N= int(input())
li = list(map(int, input().split()))

cnt = 0
for start in range(N):
    for end in range(start,N):
        s = 0
        for i in range(start, end+1):
            s += li[i]
        m = s / (end-start+1)
        if float(m).is_integer() and int(m) in li:
            
            cnt += 1

print(cnt)
