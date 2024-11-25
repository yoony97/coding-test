MAX_R = 2000
OFFSET = 1000
li = [[0]*(MAX_R+1) for i in range(MAX_R+1)]

rects = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

for i, (x1, y1, x2, y2) in enumerate(rects, start=1):
    # OFFSET을 더해줍니다.
    x1, y1 = x1 + OFFSET, y1 + OFFSET
    x2, y2 = x2 + OFFSET, y2 + OFFSET
    
    # 직사각형에 주어진 순으로 1, 2 번호를 붙여줍니다.
    # 격자 단위로 진행하는 문제이므로
    # x2, y2에 등호가 들어가지 않음에 유의합니다.
    for x in range(x1, x2):
        for y in range(y1, y2):
            li[x][y] = i


min_x, max_x, min_y, max_y = MAX_R, 0, MAX_R, 0
first_rect_exist = False

for i in range(MAX_R+1):
    for j in range(MAX_R+1):
        if li[i][j] == 1:
            found = True
            mx, my = max(i, mx), max(j, my)
            ux, uy = min(i, ux), min(j, uy)

if found:
    print((mx-ux+1)*(my-uy+1))
else:
    print(0)

