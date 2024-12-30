N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def rotate(arr):
    return [[arr[N - 1 - j][i] for j in range(N)] for i in range(N)]

def boom(arr):
    exploded = False
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
                    arr[row][col] = 0
                exploded = True
            
            start_idx = end_idx
    return arr, exploded

def drop(arr):
    for col in range(N):
        temp = [arr[row][col] for row in range(N) if arr[row][col] != 0]
        for row in range(N):
            if row < N - len(temp):
                arr[row][col] = 0
            else:
                arr[row][col] = temp[row - (N - len(temp))]
    return arr

for _ in range(K):
    arr, exploded = boom(arr)
    arr = drop(arr)
    arr = rotate(arr)

while True:
    arr, exploded = boom(arr)
    arr = drop(arr)
    if not exploded:
        break

answer = sum(1 for i in range(N) for j in range(N) if arr[i][j] != 0)
print(answer)
