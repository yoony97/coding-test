#두 계란의 차이가 L 이상 R이하면 합친다
#분리안된 애들 합치기

N, L, R = map(int, input().split())
maps = []
for i in range(N):
    maps.append(list(map(int, input().split())))

dx = [1,0,-1,0]
dy = [0,1,0,-1]


def simulation():
    graph = [[[] for _ in range(N)] for _ in range(N)]
    ispossible = False
    for x in range(N):
        for y in range(N):
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < N and 0 <= ny < N:
                    if L <= abs(maps[x][y] - maps[nx][ny]) <= R:
                        graph[x][y].append((nx,ny))
                        ispossible = True
    if not ispossible:
        return True
    #이걸로 그래프 탐색해서, 셋을 만들어야함
    visited = set() #visited 넣는 방식을 고려해야한다**
    total_group = []

    for x in range(N):
        for y in range(N):
            if graph[x][y] and (x, y) not in visited: #**visited 넣는 방식을 고려해야한다**
                grouped = set()
                q = [(x, y)]
                while q:
                    nx, ny = q.pop()
                    if (nx, ny) in visited:
                        continue
                    visited.add((nx, ny)) #**visited 넣는 방식을 고려해야한다**
                    grouped.add((nx, ny))
                    for i in graph[nx][ny]:
                        if i not in visited: #**visited 넣는 방식을 고려해야한다**
                            q.append(i)
                total_group.append(list(grouped))

    for group in total_group:
        temp = 0
        cnt = 0
        for (x,y) in group:
            temp += maps[x][y]
            cnt += 1

        for (x,y) in group:
            maps[x][y] = temp//cnt
    return False

answer = 0
while not simulation():
    answer += 1

print(answer)