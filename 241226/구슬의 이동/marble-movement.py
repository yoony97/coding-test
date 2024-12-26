direct  = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0,-1),
    'R': (0, 1)
}


n, m, t, k = map(int, input().split())
ball = []
for pr in range(m):
    r, c, d, v = input().split()
    ball.append((int(r)-1, int(c)-1, d, int(v), pr+1))


def move_ball(ball, n):
    next_cnt = []
    result = []
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append([])
        next_cnt.append(temp)

    for i in ball:
        r, c, d, v, pr = i
        dx, dy = direct[d]
        nr = r + dx*v
        nc = c + dy*v
        ischrush = False
        
        if nr < 0:
            nr = abs(nr) % (2 * n)
            if nr >= n:
                nr = 2 * n - nr - 1
            ischrush = True
        if nc < 0:
            nc = abs(nc) % (2 * n)
            if nc >= n:
                nc = 2 * n - nc - 1
            ischrush = True
        if nr >= n:
            nr = nr % (2 * n)
            if nr >= n:
                nr = 2 * n - nr - 1
            ischrush = True
        if nc >= n:
            nc = nc % (2 * n)
            if nc >= n:
                nc = 2 * n - nc - 1
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
        next_cnt[nr][nc].append((d, v, pr))
    

    for i in range(n):
        for j in range(n):
            length = len(next_cnt[i][j])
            if 0 < length <= k:
                for p in range(length):
                    d, v, pr = next_cnt[i][j][p]
                    result.append((i,j,d,v, pr))
            elif length > k:
                s = sorted(next_cnt[i][j], key=lambda x: (-x[1], -x[2]))
                for p in range(k):
                    d, v, pr = s[p]
                    result.append((i, j, d, v, pr))
    return result

for _ in range(t):
    #print(ball)
    ball = move_ball(ball, n)
print(len(ball))



