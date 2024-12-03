N = int(input())
li = list(map(int, input()))
ans = 0

def min_dist():
    dist = N 
    # 둘 다 1인 곳에 대해
    # 모든 쌍을 조사하여, 그 중 가장 가까운 거리를 구합니다.
    for i in range(N):
        for j in range(i + 1, N):
            if li[i] == 1 and li[j] == 1:
                dist = min(dist, j - i)
    return dist


for p1 in range(N):
    for p2 in range(p1+1,N):
        #새로 배정받은 자리 p1, p2
        if li[p1] == 1 or li[p2] == 1:
            continue
        li[p1] = 1
        li[p2] = 1
        #print(''.join([str(i) for i in li]))
        
        dist = min_dist()
                
        ans = max(dist, ans)
        li[p1] = 0
        li[p2] = 0
    
print(ans)