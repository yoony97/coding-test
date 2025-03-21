n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]
answer = float('inf')
visited = [False] * n
visited[0] = True

def backtracking(cur_num, hist):
    global answer
    if cur_num == n:
        last = hist[-1][0]
        if A[last][0] == 0:  # 돌아갈 수 없는 경우
            return
        temp = 0
        for (node, value) in hist:
            temp += value
        temp += A[last][0]
        answer = min(answer, temp)
        return

    for i in range(n):
        if visited[i]:
            continue
        prev = hist[-1][0]
        if A[prev][i] != 0:
            visited[i] = True
            hist.append((i, A[prev][i]))
            backtracking(cur_num + 1, hist)
            hist.pop()
            visited[i] = False

# 시작점 0에서 시작
for i in range(n):
    if A[0][i] != 0:
        visited[i] = True
        hist = [(i, A[0][i])]  # 0 -> i
        backtracking(2, hist)  # 0과 i 방문
        visited[i] = False

print(answer)
