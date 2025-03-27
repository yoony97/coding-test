from collections import deque

n, m, k = map(int, input().split())
food = [[5]*n for _ in range(n)]  # 초기 양분
plus_food = [list(map(int, input().split())) for _ in range(n)]  # 추가 양분
virus = [[deque() for _ in range(n)] for _ in range(n)]  # 칸마다 deque로 바이러스 관리

# 초기 바이러스 입력
for _ in range(m):
    x, y, age = map(int, input().split())
    virus[x-1][y-1].append(age)  # 나이순 정렬은 입력 때부터 정렬 가정

dx = [1,0,-1,0,-1,1,-1,1]
dy = [0,1,0,-1,-1,1,1,-1]

for _ in range(k):
    dead = [[[] for _ in range(n)] for _ in range(n)]  # 죽은 바이러스 기록용

    # 1. 봄: 나이 어린 바이러스부터 양분 섭취
    for i in range(n):
        for j in range(n):
            if virus[i][j]:
                new_q = deque()
                while virus[i][j]:
                    age = virus[i][j].popleft()
                    if food[i][j] >= age:
                        food[i][j] -= age
                        new_q.append(age + 1)
                    else:
                        dead[i][j].append(age)
                virus[i][j] = new_q

    # 2. 여름: 죽은 바이러스 양분화
    for i in range(n):
        for j in range(n):
            for age in dead[i][j]:
                food[i][j] += age // 2

    # 3. 가을: 번식
    for i in range(n):
        for j in range(n):
            for age in virus[i][j]:
                if age % 5 == 0:
                    for d in range(8):
                        ni = i + dx[d]
                        nj = j + dy[d]
                        if 0 <= ni < n and 0 <= nj < n:
                            virus[ni][nj].appendleft(1)  # 나이 1짜리 앞에 추가

    # 4. 겨울: 양분 추가
    for i in range(n):
        for j in range(n):
            food[i][j] += plus_food[i][j]

# 결과: 살아있는 바이러스 수
result = 0
for i in range(n):
    for j in range(n):
        result += len(virus[i][j])

print(result)
