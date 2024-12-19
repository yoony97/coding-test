dys = [-1, -1, 1, 1]
dxs = [1, -1, -1, 1]

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

ans = 0
for sy in range(N):
    for sx in range(N):
        for it in range(N):
            cx = sx
            cy = sy
            cnt = 0
            for curd in range(4):
                dx = dxs[curd]
                dy = dys[curd]
                for _ in range(it):    
                    nx = cx + dx
                    ny = cy + dy
                    if 0 <= nx < N and 0<= ny < N:
                        cnt += arr[ny][nx]
                        cx = nx
                        cy = ny
                    else:
                        cnt = 0
                        break
            if cx == sx and cy == sy:
                ans = max(cnt, ans)

print(ans)    
            
            