MAX_R = 2000
OFFSET = 1000
li = [[0]*MAX_R for i in range(MAX_R)]

ax1, ay1, ax2, ay2 = map(int, input().split())
bx1, by1, bx2, by2 = map(int, input().split())

def fill(x1,y1,x2,y2, value, check):
    for i in range(x1,x2):
        for j in range(y1,y2):
            if li[i][j] == check:
                li[i][j] = value


fill(ax1, ay1, ax2, ay2,1 ,0)
fill(bx1, by1, bx2, by2,0 ,1)

ans = 0
for i in range(MAX_R):
    for j in range(MAX_R):
        if li[i][j] == 1:
            ans += 1

print(ans)

