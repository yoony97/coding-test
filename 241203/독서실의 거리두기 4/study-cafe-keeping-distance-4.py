N = int(input())
li = list(map(int, input()))
ans = 0
for p1 in range(N):
    for p2 in range(N):
        #새로 배정받은 자리 p1, p2
        if li[p1] == 1 or li[p2] == 1:
            continue
        
        li[p1] = 1
        li[p2] = 1
        #print(''.join([str(i) for i in li]))
        min_dist = float('inf')
        for i in range(N):
            isend = True
            for j in range(i+1, N):
                if li[i] == 1 and li[j] == 1:
                    dist = j - i
                    min_dist = min(min_dist, dist)
                    isend = False
                    break
            if li[i] == 1 and isend:
                dist = N - i
                min_dist = min(min_dist, dist)
                
        ans = max(min_dist, ans)
        li[p1] = 0
        li[p2] = 0
    
print(ans)