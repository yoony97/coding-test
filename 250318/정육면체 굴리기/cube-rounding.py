N, M, X, Y, K = list(map(int, input().split()))
MAPS = []
for _ in range(N):
    inputs = list(map(int, input().split()))
    MAPS.append(inputs)

operation = list(map(int, input().split()))

def solve(MAPS, X, Y, operation):
    cx, cy = X, Y
    dice = [0, 0, 0, 0, 0, 0] #top, bottom, left, right, front, back    
    dxs = [0, 0, 0, -1, 1] #동서북남
    dys = [0, 1, -1, 0, 0] #동서북남
    def roll(op):
        if op == 1: #동쪽
            top, bottom, left, right, front, back = dice
            return [right, left, top, bottom, front, back]
        
        if op == 2: #서쪽
            # top -> right, left -> top, bottom -> left, right -> bottom
            top, bottom, left, right, front, back = dice
            return [left, right, bottom, top, front, back]
        
        if op == 3: #북쪽
            #front -> top, back -> bottom, top -> back, bottom -> front
            top, bottom, left, right, front, back = dice
            return [front, back, left, right, bottom, top]
        
        if op == 4: #남쪽
            # top->front, front->bottom, bottom -> back, back-> top
            top, bottom, left, right, front, back = dice
            return [back, front, left, right, top, bottom]
    
            
    for op in operation:
        
        nx = cx + dxs[op]
        ny = cy + dys[op]
        if 0 <= nx < N and 0 <= ny < M:
            cx = nx
            cy = ny
            dice = roll(op)
            #칸에 쓰여져있는 수가 0이면 바닥면 복사
            if MAPS[cx][cy] == 0:
                MAPS[cx][cy] = dice[1]
            else:
                dice[1] = MAPS[cx][cy]
                MAPS[cx][cy] = 0
                
            
            print(dice[0])

solve(MAPS, X, Y, operation)
            