#지역별 인구수 배열 N * N에서
#5개 부족
#땅나누기 중
#기울어진 직사각형(?) 
    # 대각선 움직임, 반시계 반향으로 순회
    # 지나왔던 지점들의 집합, 각 방향으로 최소 1번은 움직여야함
    # 격자 넘어가면 안됨

dx = [-1, -1, 1, 1]
dy = [1, -1, -1, 1]

N = int(input())
arr = []

for _ in range(N):
    row = list(map(int, input().split()))
    arr.append(row)

def ispossible(point):
    for (x,y) in point:
        if not(0 <= x < N and 0 <= y < N):
            return False
    return True

answer = float('inf')
for x in range(N):
    for y in range(N):
        for d1 in range(1,N): #특정 거리가 있으면
            for d2 in range(1,N):
                board = [[0]*N for _ in range(N)]
                #아래, 좌측, 위, 우측
                up, left, down, right = (x, y), (x + d1, y - d1), (x + d1 + d2, y - d1 + d2), (x + d2, y + d2)
                if ispossible([up, down, left, right]):
                    for i in range(d1 + 1):
                        board[x + i][y - i] = 1
                    for i in range(d2 + 1):
                        board[x + i][y + i] = 1
                    for i in range(d2 + 1):
                        board[x + d1 + i][y - d1 + i] = 1
                    for i in range(d1 + 1):
                        board[x + d2 + i][y + d2 - i] = 1
                    
                    inside = False
                    for i in range(x + 1, x + d1 + d2):
                        for j in range(N):
                            if board[i][j] == 1:
                                inside = not inside
                            
                            elif inside:
                                board[i][j] = 1
                    
                    
                    #2번 부족 좌측 상단 경계의 윗부분에 해당하는 지역을 가짐
                    #위쪽 꼭짓점 위에 있는 칸들은 모두 포함
                    for row in range(0, left[0]):
                        for col in range(0, up[1]+1):  # inclusive
                            if 0 <= row < N and 0 <= col < N and board[row][col] == 0:
                                board[row][col] = 2

                    #3번 부족
                    for row in range(0, right[0]+1):
                        for col in range(up[1],N):  # inclusive
                            if 0 <= row < N and 0 <= col < N and board[row][col] == 0:
                                board[row][col] = 3

                    #4번 부족
                    for row in range(left[0], N):
                        for col in range(0,down[1]):  # inclusive
                            if 0 <= row < N and 0 <= col < N and board[row][col] == 0:
                                board[row][col] = 4
                    
                    #Calculate
                    count = [0 for i in range(5)]
                    for i in range(N):
                        for j in range(N):
                            count[board[i][j]] += arr[i][j]
                    
                    answer = min(answer, max(count) - min(count))

print(answer)

                
            
        
