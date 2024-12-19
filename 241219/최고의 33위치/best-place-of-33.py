N = int(input())
maps = []
for i in range(N):
    maps.append(list(map(int, input().split())))

def count(cx,cy):
    cnt = 0
    for i in range(cx-1, cx+2):
        for j in range(cy-1, cy+2):
            if 0 <= i < N and 0 <= j < N:
                cnt += maps[i][j]
            else:
                return 0
    return cnt 

max_ans = 0
for i in range(N):
    for j in range(N):
        ans = count(i,j)
        max_ans = max(ans, max_ans)

print(max_ans)