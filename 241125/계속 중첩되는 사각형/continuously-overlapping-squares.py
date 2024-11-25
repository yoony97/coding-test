OFFSET = 100
MAX_R = 200

n = int(input())
li = [[0]*(MAX_R+1) for i in range(MAX_R+1)]
rects = []
for i in range(n):
    rects.append(tuple(map(int, input().split())))


for i, rect in enumerate(rects):
    i = i%2
    x1,y1,x2,y2 = rect
    for x in range(x1 + OFFSET, x2 + OFFSET):
        for y in range(y1 + OFFSET, y2 + OFFSET):
            li[x][y] = i
    
ans = 0
for i in range(MAX_R):
    for j in range(MAX_R):
        if li[i][j] == 1:
            ans += 1

print(ans)