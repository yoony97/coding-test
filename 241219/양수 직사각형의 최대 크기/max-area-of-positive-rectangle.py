n, m = map(int, input().split())
maps =[]

for _ in range(n):
    maps.append(list(map(int, input().split())))


def check(x1, y1, x2, y2):
    for i in range(y1, y2 + 1):  # 행(y)
        for j in range(x1, x2 + 1):  # 열(x)
            if maps[i][j] <= 0:
                return False
    return True

ans = -1
for sy in range(n):
    for sx in range(m):
        for ey in range(sy, n):
            for ex in range(sx, m):
                if check(sx, sy, ex, ey):
                    size = (ex-sx+1)*(ey-sy+1)
                    if size > 0:
                        #print(sx, sy, ex, ey, size)
                        ans = max(size, ans)

print(ans)