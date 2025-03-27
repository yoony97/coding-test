from collections import deque
import heapq

# 전투 로봇 클래스
class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.level = 2
        self.eaten = 0
        self.time = 0

    def level_up(self):
        self.eaten += 1
        if self.eaten >= self.level:
            self.level += 1
            self.eaten = 0

# 가장 가까운 먹이 탐색
def find_enemy(robot, arr, n):
    visited = [[False]*n for _ in range(n)]
    q = deque([(robot.x, robot.y, 0)])
    visited[robot.x][robot.y] = True

    candidates = []
    while q:
        x, y, dist = q.popleft()

        # 먹을 수 있는 몬스터 발견
        if 0 < arr[x][y] < robot.level:
            heapq.heappush(candidates, (dist, x, y))

        for dx, dy in [(-1,0), (0,-1), (0,1), (1,0)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if arr[nx][ny] <= robot.level:
                    visited[nx][ny] = True
                    q.append((nx, ny, dist+1))

    return heapq.heappop(candidates) if candidates else None

# 입력 처리
n = int(input())
arr = []
robot = None
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 9:
            robot = Robot(i, j)
            row[j] = 0
    arr.append(row)

# 시뮬레이션
while True:
    result = find_enemy(robot, arr, n)
    if result:
        dist, x, y = result
        robot.x, robot.y = x, y
        robot.time += dist
        arr[x][y] = 0
        robot.level_up()
    else:
        break

print(robot.time)
