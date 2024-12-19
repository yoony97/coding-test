n, m = map(int, input().split())
maps = []
ans = 0
for i in range(n):
    maps.append(list(map(int, input().split())))

for i in range(n):
    #연속을 기록해야하네
    prev_col = -1
    prev_row = -1
    c_cnt = 1
    r_cnt = 1
    max_colc = 0
    max_rowc = 0
    for j in range(n):
        col = maps[i][j]
        row = maps[j][i]
        if prev_col == col:
            c_cnt += 1
        else:
            max_colc = max(max_colc, c_cnt)
            c_cnt = 1
        
        if prev_row == row:
            r_cnt += 1
        else:
            max_rowc = max(max_rowc, r_cnt)
            r_cnt = 1

        prev_col = col
        prev_row = row
    max_rowc = max(max_rowc, r_cnt)
    max_colc = max(max_colc, c_cnt)
    #print(max_colc, max_rowc)

    if max_colc >= m:
        ans += 1
    if max_rowc >= m:
        ans += 1

print(ans)