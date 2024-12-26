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
        remain_v = v
        while remain_v > 0:
            nr = r + dx
            nc = c + dy

            if 0 <= nr < n and 0 <= nc < n:
                remain_v -= 1
                r = nr
                c = nc
            
            else:
                if nr < 0:
                    d = 'D'    
                elif nr >= n:
                    d = 'U'
                elif nc < 0:
                    d = 'R'
                elif nc >= n:
                    d = 'L'
                dx, dy = direct[d]

        next_cnt[nr][nc].append((d, v, pr))
    

    for i in range(n):
        for j in range(n):
            length = len(next_cnt[i][j])
            if 0 < length <= k:
                for p in range(length):
                    d, v, pr = next_cnt[i][j][p]
                    result.append((i,j,d,v, pr))
            elif length > k:
                next_cnt[i][j].sort(key=lambda x: (-x[1], -x[2]))  # 속도 우선, 번호 우선
                for p in range(k):
                    d, v, pr = next_cnt[i][j][p]
                    result.append((i, j, d, v, pr))
    
    return result

for _ in range(t):
    #print(ball)
    ball = move_ball(ball, n)
#print(ball)
print(len(ball))



