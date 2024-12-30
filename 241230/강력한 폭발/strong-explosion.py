boom_coordinate = {
    1:[(1,0), (2,0), (-1,0), (-2,0)],
    2:[(1,0), (-1,0), (0,1), (0,-1)],
    3:[(1,1), (-1,1), (1,-1), (-1,-1)],
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
    cx, cy = locate
    for (dx, dy) in coords:
        nx = cx + dx
        ny = cy + dy
        if 0 <= nx < N and 0 <= nx < N:
            arr[nx][ny] = -1
    return arr

    

def solve(arr,cur):
    global answer
    if cur == num_boom-1:
        answer = max(answer, check(arr))
        return 
    
    for i in range(1, 4):
        coords = boom_coordinate[i]
        new_arr = boom(arr, coords, loc[cur])
        solve(new_arr, cur+1)

solve(maps, 0)
print(answer)
