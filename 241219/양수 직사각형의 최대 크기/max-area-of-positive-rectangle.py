n, m = map(int, input().split())
maps =[]

for _ in range(n):
    maps.append(list(map(int, input().split())))


def check(x1,y1, x2, y2):
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            if maps[j][i] < 0:
                return False
    return True

ans = -1
for sy in range(n):
    for sx in range(m):
        for ey in range(sy, n):
            for ex in range(sx, m):
                if check(sx, sy, ex, ey):
                    ans = max((ex-sx+1)*(ey-sy+1), ans)

print(ans)