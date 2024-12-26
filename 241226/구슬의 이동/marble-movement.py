direct  = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0,-1),
    'R': (0, 1)
}


n, m, t, k = map(int, input().split())
ball = []
for _ in range(m):
    r, c, d, v = input().split()
    ball.append((int(r)-1, int(c)-1, d, int(v)))


def move_ball(ball, n):
    next_cnt = []
    result = []
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append([])
        next_cnt.append(temp)

    for i in ball:
        r, c, d, v = i
        dx, dy = direct[d]
        nr = r + dx*v
        nc = c + dy*v
        ischrush = False
        
        if nr < 0:
            nr = -1*nr
            ischrush = True
        if nc < 0:
            nc = -1*nc    
            ischrush = True
        if nr >= n:
            nr = n - nr%n - 1
            ischrush = True
        if nc >= n:
            nc = n - nc%n - 1
            ischrush = True
        
        if ischrush:
            if d == 'U':
                d = 'D'
            elif d == 'D':
                d = 'U'
            elif d == 'L':
                d = 'R'
            else:
                d = 'L'
        next_cnt[nr][nc].append((d, v))
    

    for i in range(n):
        for j in range(n):
            length = len(next_cnt[i][j])
            if 0 < length <= k:
                for p in range(length):
                    d, v= next_cnt[i][j][p]
                    result.append((i,j,d,v))
            elif length > k:
                s = sorted(next_cnt[i][j], key=lambda x: (-x[1]))
                for p in range(k):
                    d, v = s[p]
                    result.append((i, j, d, v))
    return result

for _ in range(t):
    ball = move_ball(ball, n)

print(len(ball))

