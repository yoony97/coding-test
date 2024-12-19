block = [
    [(0,0),(0,1),(1,1)], 
    [(0,0),(1,0),(1,1)],
    [(1,0),(0,1),(1,1)], 
    [(0,0),(1,0),(0,1)],
    # 블록 2
    [(0,0), (0,1), (0,2)],
    [(0,0), (1,0), (2,0)]
]


N, M = map(int, input().split())
maps = []
for _ in range(N):
    maps.append(list(map(int, input().split())))
ans = 0
for cy in range(N):
    for cx in range(M):
        for b in block:
            cnt = 0
            for (dy, dx) in b:
                nx = cx + dx
                ny = cy + dy
                if 0 <= nx < M and 0 <= ny < N:
                    cnt += maps[ny][nx]
                else:
                    cnt = 0
                    break
            ans = max(ans, cnt)

print(ans)        