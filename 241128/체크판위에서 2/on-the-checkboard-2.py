R, C = map(int, input().split())
maps = []
for i in range(R):
    maps.append(input().split())
#점프: 현재 위치 색과 점프 위치 색은 달라야한다.
#룰2: 현재 위치보다 한칸 이상 오른쪽에 있는 위치 & 현재 위치에서 적어도 한칸 이상 아래쪽에 있는 위치
#룰3:  도달한 위치가 2 곳
current = maps[0][0]
paths = []
cnt = 0
for i in range(1,R):
    for j in range(1,C):
        if maps[i][j] != maps[0][0]:
            path = [(0,0), (i,j)]
            for k in range(i+1, R-1):
                for l in range(j+1, C-1):
                    if maps[i][j] != maps[k][l]:
                        cnt += 1
            
#print(paths)
print(cnt)

