#백준 13460번 구슬탈출 2


# Insert inputs and preprocess map 
N, M = [int(i) for i in input().split(" ")]
arr = []
red = [0,0]
blue = [0,0]
goal = [0,0]
for i in range(N):
    maps = input()
    temp = [0 for _ in range(M)]
    for idx, str in enumerate(maps):
        if str == '#':
            temp[idx] = -1
        if str == 'R':
            red = [i,idx]
        if str == 'B':
            blue = [i,idx]
        if str == 'O':
            goal = [i,idx]
    arr.append(temp)

 
            
            
            
            
            



def dfs(arr, red, blue, cnt=0):
    dys = [1, -1, 0, 0]
    dxs = [0, 0, -1, 1]

    if red == goal:
        return cnt
    if blue == goal:
        return -1
    if cnt > 10:
        return -1
    
    for i in range(4):
        dy = dys[i]
        dx = dxs[i]
        isend = False
        while not isend:
            ry, rx = red
            by, bx = blue
            nry, nrx = ry+dy, rx+dx
            nby, nbx = by+dy, bx+dx
            
            #순서가 애매하다.