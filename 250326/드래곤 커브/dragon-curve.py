n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
#0차 드래곤 커브 = 길이 1인 선분, y좌표가 증가하는 방향으로 시작함
#1차 드래곤 커브 = 0차 드래곤 커브 의 끝점 기준 90도 회전
#n개의 드래곤 커브가 주어질 때, 만들어지는 단위 정사각형(길이가 1인)

#차수와 방향에 대해서 드래곤 커브 만드는 함수
#정사각형 판별하는 함수 작성 필요 (중복 고려 해야하겠는데?, set으로 만들면 될듯)

def make_dragon(x, y, d, g):
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]  # 오른쪽, 위, 왼쪽, 아래
    

    directions = [d]  # 0세대: 시작 방향
    for _ in range(g):
        temp = []
        for dir in reversed(directions):
            temp.append((dir + 1) % 4)
        directions += temp

    curve = [(x, y)]
    for dir in directions:
        x += dx[dir]
        y += dy[dir]
        curve.append((x, y))

    return curve

curve = []

for x,y,d,g in graph:
    curve.extend(make_dragon(x,y,d,g))

curves = set(curve)
box = []
for c in curves:
    x, y = c
    if (x+1, y+1) in curves and (x+1, y) in curves  and (x,y+1) in curves:
        new_box = (x,y,x+1,y,x,y+1,x+1,y+1)
        if new_box not in box:
            box.append(new_box)

print(len(box))
         


