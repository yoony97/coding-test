MAX_R = 2000
OFFSET = 1000
li = [[0]*MAX_R for i in range(MAX_R)]

ax1, ay1, ax2, ay2 = map(int, input().split())
bx1, by1, bx2, by2 = map(int, input().split())

def fill(x1,y1,x2,y2, value, check):
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            if li[i][j] == check:
                li[i][j] = value


fill(ax1+OFFSET, ay1+OFFSET, ax2+OFFSET, ay2+OFFSET,1 ,0)
fill(bx1+OFFSET, by1+OFFSET, bx2+OFFSET, by2+OFFSET,0 ,1)

mx, my = 0, 0
ux, uy = MAX_R, MAX_R
for i in range(MAX_R):
    for j in range(MAX_R):
        if li[i][j] == 1:
            print(i,j)
            mx, my = max(i, mx), max(j, my)
            ux, uy = min(i, ux), min(j, uy)

#print(mx,my, ux, uy)
if mx == my == 0 and ux == uy == MAX_R:
    print(0)
else:
    print((mx-ux)*(my-uy))
