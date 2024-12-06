n, m = map(int, input().split())
home = list(map(int, input().split()))

cnt = 0
dist = 0
ans = 0
isexits = False
if m == 0:
    print(sum(home))
else:    
    for i in range(n):
        if home[i] == 1:
            isexits = True
        
        if isexits:
            dist+=1
        
        if dist == 2*m+1:
            ans += 1
            dist = 0
            isexits=False
    print(ans)


#[2m+1] 마다확인해야함
# 집이 존재하면 가운데 설치함
