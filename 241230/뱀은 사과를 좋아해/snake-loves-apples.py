from collections import deque

N, M, K = map(int, input().split())
apples = []
movement = []
for _ in range(M):
    x, y = map(int, input().split())
    apples.append((x-1,y-1))

for _ in range(K):
    d, p = input().split()
    movement.append((d, p))

def get_d(d):
    if d == 'U':
        dx, dy = -1, 0
    if d == 'D':
        dx, dy = 1, 0
    if d == 'R':
        dx, dy = 0, 1
    if d == 'L':
        dx, dy = 0, -1
    return dx, dy

def check_apple(nx, ny, apples):
    for i in range(len(apples)):
        ax, ay = apples[i]
        if ax == nx and ny == ay:
            last_apples = apples[:i] + apples[i+1:]
            return 1, last_apples
    return 0, apples


current_length = 1
current = (0,0)
history = deque([(0,0)]) # queue
answer = 0
isFail = False
for (d, p) in movement:
    dx, dy = get_d(d)
    if not(0 <= current[0] + dx*int(p) < N and 0 <= current[1] + dy*int(p) < N):
        isFail = True
        break
        
    if not isFail:
        #print(current, history, current_length, answer)
        

        for _ in range(int(p)):
            #print(current, history, current_length, apples)
            cx, cy = current
            nx, ny = cx + dx, cy + dy
            
            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in history:
                answer += 1
                current = (nx, ny)
                history.append(current)
                temp, apples = check_apple(nx, ny, apples)
                if temp:
                    current_length += temp
                else:
                    if current_length > 1:
                        current_length -= 1
            
                while len(history) != current_length:
                    history.popleft()                        
            
            else:
                answer += 1
                isFail = True
                break
    else:
        break


print(answer)
