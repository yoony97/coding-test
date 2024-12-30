N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

reflect = {
    1:{
        'D': (-1, 0, 'L'),
        'U': (1, 0, 'R'),
        'R': (0, -1, 'U'),
        'L': (0, 1, 'D')
    },
    2:{
        'U': (-1, 0, 'L'),
        'D': (1, 0, 'R'),
        'R': (0, 1, 'D'),
        'L': (0, -1, 'U')
    }
}
def get_d(d):
    if d == 'U':
        dy, dx = (0, -1)
    if d == 'D':
        dy, dx = (0, 1)
    if d == 'L':
        dy, dx = (-1, 0)
    if d == 'R':
        dy, dx = (1, 0)
    return dx, dy


def simulate(start):
    cx, cy, d = start
    dx, dy = get_d(d)
    time = 0
    while True:
        if arr[cx][cy] == 1:
            dy, dx, d = reflect[1][d]
        
        elif arr[cx][cy] == 2:
            dy, dx, d = reflect[2][d]
    
        time += 1
        nx = cx + dx
        ny = cy + dy
        #print(nx, ny, d)
        if not(0 <= nx < N and 0 <= ny < N):
            return time + 1
        cx = nx
        cy = ny
        # if arr[nx][ny] == 1:
        #     dy, dx, d = reflect[1][d]
        # elif arr[nx][ny] == 2:
        #     dy, dx, d = reflect[2][d]
    

# [0][0, ..., N-1], D
# [N-1][0, ..., N-1], U
# [0, ..., N-1][0], L
# [0, ....,N-1][N-1], R

answer = 0
for i in range(N):
    answer = max(answer, simulate((i, 0, 'R')))
    
for i in range(N):
    #print(simulate((0, i, 'D')))
    answer = max(answer, simulate((0, i, 'D')))

for i in range(N):
    answer = max(answer, simulate((N-1,i, 'U')))

for i in range(N):
    answer = max(answer, simulate((i,N-1, 'L')))

print(answer)
#print(simulate((2, 0, 'R')))

