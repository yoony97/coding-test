boom_coordinate = {
    1:[(1,0), (2,0), (-1,0), (-2,0), (0, 0)],
    2:[(1,0), (-1,0), (0,1), (0,-1), (0, 0)],
    3:[(1,1), (-1,1), (1,-1), (-1,-1), (0, 0)],
}

N = int(input())
maps = [[0]*N for _ in range(N)]
loc = []

for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        if temp[j] == 1:
            loc.append((i,j))
num_boom = len(loc)
answer = 0

def check(arr):
    result = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == -1:
                result += 1
    return result

def boom(arr, coords, locate):
    new_arr = [[arr[i][j] for j in range(N)] for i in range(N)]
    cx, cy = locate
    for (dx, dy) in coords:
        nx = cx + dx
        ny = cy + dy
        if 0 <= nx < N and 0 <= ny < N:
            new_arr[nx][ny] = -1
    return new_arr

    

def solve(arr,cur):
    global answer
    if cur == num_boom:
        answer = max(answer, check(arr))
        #print(arr)
        return 
    
    for i in range(1, 4):
        coords = boom_coordinate[i]
        new_arr = boom(arr, coords, loc[cur])
        solve(new_arr, cur+1)

if N == 1:
    print(1)
else:
    solve(maps, 0)
    print(answer)


