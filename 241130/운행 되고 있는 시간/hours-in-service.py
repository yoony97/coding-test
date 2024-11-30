N = int(input())
times = []
for i in range(N):
    a, b = map(int, input().split())
    times.append((a,b))

ans = 0
#해고하는 인원 i
for i in range(N):
    time_table = [0]*1001
    #일하는 인원 j
    for j in range(N):
        if i == j:
            continue
        t1, t2 = times[j]
        for k in range(t1, t2):
            time_table[k] = 1
    
    result = sum(time_table)
    ans = max(ans, result)

print(ans)