MAX_R = 2000
OFFSET = 1000

Ax1, Ay1, Ax2, Ay2 = map(int, input().split())
Bx1, By1, Bx2, By2 = map(int, input().split())
Cx1, Cy1, Cx2, Cy2 = map(int, input().split())

li = [[0]*MAX_R for i in range(MAX_R)]



def check(x1,y1,x2,y2, value):
    for i in range(x1,x2):
        for j in range(y1,y2):
            li[i][j] = value

check(Ax1, Ay1, Ax2, Ay2, 1)
check(Bx1, By1, Bx2, By2, 1)
check(Cx1, Cy1, Cx2, Cy2, -1)

ans = 0

for i in range(MAX_R):
    for j in range(MAX_R):
        if li[i][j] == 1:
            ans += 1

print(ans)
