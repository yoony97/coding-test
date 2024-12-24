n, r, c = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

q = [(r-1,c-1)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
#중복이 가능한가?
while q:
    r,c = q.pop(0)
    direct = 0
    for i in range(4):
        nr = r + dy[i]
        nc = c + dx[i]
        if 0 <= nr < n and 0 <= nc < n:
            if arr[r][c] < arr[nr][nc]:
                direct = i
                q.append((nr, nc))
                break
    print(arr[r][c], end = " ")