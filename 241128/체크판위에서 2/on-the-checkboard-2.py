R, C = map(int, input().split())
maps = []
for i in range(R):
    maps.append(input().split())
#점프: 현재 위치 색과 점프 위치 색은 달라야한다.
#룰2: 현재 위치보다 한칸 이상 오른쪽에 있는 위치 & 현재 위치에서 적어도 한칸 이상 아래쪽에 있는 위치
#룰3:  도달한 위치가 2 곳
current = maps[0][0]
cnt = 0
for col in range(1,R-1):
    for row in range(1,C-1):
        #새로운 점프 위치, 점프는 총 2번 밖에 못함
        if maps[row][col] != maps[0][0]:
            for new_col in range(col+1, R-1):
                for new_row in range(row+1, C-1):
                    if maps[row][col] != maps[new_col][new_row] and maps[new_col][new_row] != maps[R-1][C-1]:
                        #print(row+1, col+1, new_row+1, new_col+1)
                        cnt += 1

print(cnt)