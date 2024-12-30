from collections import deque

def snake_game(n, m, apples, k, moves):
    directions = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}
    grid = [[0] * n for _ in range(n)]
    for x, y in apples:
        grid[x - 1][y - 1] = 1 

    
    snake = deque([(0, 0)])
    time = 0
    

    # 움직임 처리
    for direction, steps in moves:
        for _ in range(steps):
            time += 1
            head_x, head_y = snake[-1]  
            dx, dy = directions[direction]
            new_x, new_y = head_x + dx, head_y + dy  
            
            #충돌
            if not (0 <= new_x < n and 0 <= new_y < n):
                return time

            #꼬리를 제거했을 때도 확인해야할듯?
            if grid[new_x][new_y] == 1:
                grid[new_x][new_y] = 0  # 사과 제거
            else:
                snake.popleft()  # 꼬리 제거

            if (new_x, new_y) in snake:
                return time

            snake.append((new_x, new_y))


    
    return time

# 입력 처리
n, m, k = map(int, input().split())
apples = [tuple(map(int, input().split())) for _ in range(m)]
moves = [input().split() for _ in range(k)]
moves = [(d, int(p)) for d, p in moves]

# 결과 출력
print(snake_game(n, m, apples, k, moves))
