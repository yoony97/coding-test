N= int(input())
li = list(map(int, input().split()))

cnt = 0
for start in range(N):
    for end in range(start,N):
        s =  sum(li[start:end+1])
        m  = s / len(li[start:end+1])
        if float(m).is_integer() and int(m) in li:
            cnt += 1

print(cnt)
