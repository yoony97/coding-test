N, M, K = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

def rotate(arr):
    new_arr = [[0]*N for _ in range(N)]

    #우측으로 당기고 회전하자
    for i in range(N):
        temp = []
        for j in range(N):
            if arr[i][j] != 0:
                temp.append(arr[i][j])
            temp2 = [0]*(N-len(temp))
            temp2.extend(temp)
        arr[i] = temp2

    for i in range(N):
        for j in range(N):
            new_arr[i][j] = arr[N-1-j][i]

    return new_arr


def check(arr, col, start_idx, curr_num):
    for end_idx in range(start_idx + 1, len(arr)):
        if arr[end_idx][col] != curr_num:
            return end_idx - 1
        
    return len(arr) - 1


def boom(arr):
    for col in range(N):
        for start_idx in range(N):
            if arr[start_idx][col] != 0:
                end = check(arr, col, start_idx, arr[start_idx][col])
                if (end-start_idx+1)>= M:
                    for i in range(start_idx, end+1):
                        arr[i][col] = 0
    return arr

def drop(arr):
    for col in range(N):
        temp = []
        # 0이 아닌 값을 수집
        for row in range(N):
            if arr[row][col] != 0:
                temp.append(arr[row][col])
        
        # 0으로 초기화 후, 수집된 값을 아래부터 채우기
        for row in range(N):
            if row < N - len(temp):
                arr[row][col] = 0
            else:
                arr[row][col] = temp[row - (N - len(temp))]
    return arr
            


for _ in range(K):
    arr = boom(arr)
    arr = drop(arr)
    arr = rotate(arr)

arr = boom(arr)
arr = drop(arr)
aarr = boom(arr)
answer = 0

for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            answer += 1 

print(answer)



