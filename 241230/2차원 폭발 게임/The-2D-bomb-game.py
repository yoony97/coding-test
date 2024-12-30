def rotate(arr, N):
    # 배열을 시계 방향으로 90도 회전
    return [[arr[N - 1 - j][i] for j in range(N)] for i in range(N)]

def boom(arr, N, M):
    exploded = False
    to_explode = [[False] * N for _ in range(N)]

    # 폭발 처리
    for col in range(N):
        start_idx = 0
        while start_idx < N:
            if arr[start_idx][col] == 0:
                start_idx += 1
                continue

            curr_num = arr[start_idx][col]
            end_idx = start_idx
            while end_idx < N and arr[end_idx][col] == curr_num:
                end_idx += 1

            if end_idx - start_idx >= M:
                for row in range(start_idx, end_idx):
                    to_explode[row][col] = True
                exploded = True

            start_idx = end_idx

    for i in range(N):
        for j in range(N):
            if to_explode[i][j]:
                arr[i][j] = 0

    return arr, exploded

def drop(arr, N):
    for col in range(N):
        temp = [arr[row][col] for row in range(N) if arr[row][col] != 0]
        for row in range(N):
            if row < N - len(temp):
                arr[row][col] = 0
            else:
                arr[row][col] = temp[row - (N - len(temp))]
    return arr

# 입력 데이터 처리
N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# K번 회전 및 폭발 반복
for _ in range(K):
    while True:
        arr, exploded = boom(arr, N, M)
        arr = drop(arr, N)
        if not exploded:
            break
    arr = rotate(arr, N)

# 마지막 폭발 반복
while True:
    arr, exploded = boom(arr, N, M)
    arr = drop(arr, N)
    if not exploded:
        break

# 남은 폭탄 개수 계산
answer = sum(1 for i in range(N) for j in range(N) if arr[i][j] != 0)
print(answer)
