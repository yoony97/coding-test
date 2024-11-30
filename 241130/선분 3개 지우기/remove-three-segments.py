N = int(input())
lines = []
for i in range(N):
    a, b = map(int, input().split())
    lines.append((a,b))

def isvalid(a, b, c):
    cnt = [0]*(101)
    for i in range(N):
        if i in [a,b,c]:
            continue #제외할 선분일 경우
        
        s, e = lines[i]
        for p in range(s,e+1):
            if cnt[p] == 0:
                cnt[p] = 1
            else:
                return False
    return True
                
            

cnt = 0

for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1, N):
            if i == j or i == k or j == k:
                continue
            if isvalid(i,j,k):
                cnt += 1
            #제거할 선분 i, j, k

print(cnt)