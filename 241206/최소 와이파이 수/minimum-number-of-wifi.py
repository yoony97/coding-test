n, m = map(int, input().split())
home = list(map(int, input().split()))

cnt = 0
dist = 0
ans = 0
for i in range(n):
    #내가 지나온 m만큼의 거리 까지 사람이 존재하냐?
    if home[i] == 1:
        cnt += 1
    
    if dist == m and cnt > 0:
        #print(f"{i}에 설치")
        ans += 1

    if dist == (2*m+1):
        dist = 0

    dist += 1
    
print(ans)