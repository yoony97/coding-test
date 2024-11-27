n = int(input())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

li = []
for _ in range(n):
    li.append(list(map(int,input().split())))
ans = 0
for y in range(n):
    for x in range(n):
        cnt = 0
        for d in range(4):
            cx = x + dx[d]
            cy = y + dy[d]
            
            if 0 <= cx < n and 0 <= cy < n and li[cx][cy] == 1:
                cnt+= 1
        if cnt >= 3:
            ans += 1

print(ans)