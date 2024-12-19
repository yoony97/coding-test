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
            cnt = 0 #arr[cx][cy]
            fail = False

            for curd in range(4):
                dx = dxs[curd]
                dy = dys[curd]
                for k in range(it):
                    if cx == sx and cy == sy:
                        ans = max(cnt, ans)
                        #print(sy, sx, it, cnt)
                    if fail:
                        break
                    nx = cx + dx
                    ny = cy + dy
                    if 0 <= nx < N and 0<= ny < N:
                        cnt += arr[ny][nx]
                        cx = nx
                        cy = ny
                    else:
                        if k == 0:
                            fail = True
                            cnt = 0
            

                

print(ans)    
            
            