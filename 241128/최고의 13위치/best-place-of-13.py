N = int(input())
maps = []
for i in range(N):
    maps.append(list(map(int, input().split())))

cnt = 0
for i in range(N):
    for j in range(N-2):
        cnt = max(cnt, maps[i][j]+ maps[i][j+1]+maps[i][j+2]) 

print(cnt)