N = int(input())
maps = []
dx = [0, 1, 2]
ans = 0
for i in range(N):
    maps.append(list(map(int, input().split())))

for col in range(N):
    for row in range(N-2):
        current = maps[col][row] + maps[col][row+1] + maps[col][row+2]
        rows = [row, row+1, row+2]
        for new_col in range(col, N):
            for new_row in range(row, N, 3):
                #같은 행에서 로우가 겹칠 경우 무시
                if new_col == col and new_row in rows:
                    continue
                else:
                    if new_row + 2 < N:   
                        nex = maps[new_col][new_row] + maps[new_col][new_row+1] + maps[new_col][new_row+2]        
                        ans = max(ans, nex + current)
print(ans)        
            