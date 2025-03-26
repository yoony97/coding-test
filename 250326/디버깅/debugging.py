n, m, h = map(int, input().split())
graph = [tuple(map(int, input().split())) for _ in range(m)]
ladder = [[0] * (n+1) for _ in range(h+1)]

# 입력된 가로선 정보 반영
for a, b in graph:
    ladder[a][b] = 1  # b와 b+1 사이 연결

def simulate():
    for start in range(1, n+1):
        k = start
        for i in range(1, h+1):
            if ladder[i][k]:       # 오른쪽 이동
                k += 1
            elif ladder[i][k-1]:   # 왼쪽 이동
                k -= 1
        if k != start:
            return False
    return True

def dfs(count, x, y):
    global answer
    if count > answer:  # 가지치기
        return
    if simulate():
        answer = count
        return
    if count == 3:  # 최대 3개까지만 허용
        return
    for i in range(x, h+1):
        k = y if i == x else 1
        for j in range(k, n):
            if ladder[i][j] == ladder[i][j-1] == ladder[i][j+1] == 0:
                ladder[i][j] = 1
                dfs(count+1, i, j+2)
                ladder[i][j] = 0


answer = 4  # 최대 3개까지만 추가 가능하므로 4 이상이면 불가능

dfs(0, 1, 1)

print(answer if answer < 4 else -1)