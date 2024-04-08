#https://www.acmicpc.net/problem/12100
from itertools import product


def find_max(arr):
    maximum = 0
    for i in arr:
        if maximum < max(i):
            maximum = max(i)
    return maximum

def find_zero(arr):
    cnt = 0
    for i in arr:
        for j in i:
            if j == 0:
                cnt += 1
    return cnt

def dfs(arr, d, cnt):
    if cnt > 5:
        return find_max(arr)
    new_arr = move(arr, d)
    

def left(board):
    for i in range(N):
        cursor = 0
        for j in range(1, N):
            if board[i][j] != 0: # 0이 아닌 값이
                tmp = board[i][j]
                board[i][j] = 0 # 일단 비워질꺼니까 0으로 바꿈

                if board[i][cursor] == 0: # 비어있으면
                    board[i][cursor] = tmp # 옮긴다

                elif board[i][cursor] == tmp: # 같으면
                    board[i][cursor] *= 2 # 합친다
                    cursor += 1

                else: # 비어있지도 않고 다른 값일때
                    cursor += 1 # pass
                    board[i][cursor] = tmp # 바로 옆에 붙임
    return board

def right(board):
    for i in range(N):
        cursor = N-1
        for j in range(1, N):
            if board[i][N-1-j] != 0: # 0이 아닌 값이
                tmp = board[i][N-1-j]
                board[i][N-1-j] = 0 # 일단 비워질꺼니까 0으로 바꿈

                if board[i][cursor] == 0: # 비어있으면
                    board[i][cursor] = tmp # 옮긴다

                elif board[i][cursor] == tmp: # 같으면
                    board[i][cursor] *= 2 # 합친다
                    cursor -= 1
                else: # 비어있지도 않고 다른 값일때
                    cursor -= 1 # pass
                    board[i][cursor] = tmp # 바로 옆에 붙임
    return board

def up(board):
    for j in range(N):
        cursor = 0
        for i in range(N):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0

                if board[cursor][j] == 0:
                    board[cursor][j] = tmp

                elif board[cursor][j] == tmp:
                    board[cursor][j] *= 2
                    cursor += 1

                else:
                    cursor += 1
                    board[cursor][j] = tmp
    return board

def down(board):
    for j in range(N):
        cursor = N - 1
        for i in range(N - 1, -1, -1):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0

                if board[cursor][j] == 0:
                    board[cursor][j] = tmp

                elif board[cursor][j] == tmp:
                    board[cursor][j] *= 2
                    cursor -= 1

                else:
                    cursor -= 1
                    board[cursor][j] = tmp
    return board


if __name__ == '__main__':
    N = int(input())
    
    direct = {
        'r' : right,
        'l' : left,
        'u' : up,
        'd' : down
    }

    arr = []
    maximum = 0

    for row in range(N):
        column = [int(num) for num in input().split(" ")]
        arr.append(column)
        if max(column) > maximum:
            maximum = max(column)

    stages = list(product(list(direct.keys()),repeat=5))
    for stage in stages:
        new_arr = [a[:] for a in arr]
        for s in stage:
            f = direct[s]
            new_arr = f(new_arr)
        local_max = find_max(new_arr)
        if  local_max > maximum:
            maximum = local_max
    print(maximum)

