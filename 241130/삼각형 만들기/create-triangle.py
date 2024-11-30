N  = int(input())
points = []
for i in range(N):
    a, b = map(int, input().split())
    points.append((a,b))

def check_condition(i,j,k):
    if points[i][0] - points[j][0] == 0: #i,j 선분이 y축에 평행
        height = abs(points[i][1] - points[j][1])
        if points[i][1] - points[k][1] == 0:   # i,k 선분이 x축에 평행
            width = abs(points[i][0] - points[k][0])
            return height*width
        elif points[j][1] - points[k][1] == 0:   # i,k 선분이 x축에 평행
            width = abs(points[j][0] - points[k][0])
            return height*width
        else:
            return 0
    if points[i][0] - points[k][0] == 0: #i,k 선분이 y축에 평행
        height = abs(points[i][1] - points[k][1])
        if points[i][1] - points[j][1] == 0:   # i,j 선분이 x축에 평행
            width = abs(points[i][0] - points[j][0])
            return height*width
        elif points[j][1] - points[k][1] == 0:   # i,k 선분이 x축에 평행
            width = abs(points[j][0] - points[k][0])
            return height*width
        else:
            return 0

    if points[j][0] - points[k][0] == 0: #j,k 선분이 y축에 평행
        height = abs(points[j][1] - points[k][1])
        if points[i][1] - points[k][1] == 0:   # i,k 선분이 x축에 평행
            width = abs(points[i][0] - points[k][0])
            return height*width
        
        elif points[j][1] - points[i][1] == 0:   # i,k 선분이 x축에 평행
            width = abs(points[j][0] - points[i][0])
            return height*width
        else:
            return 0
    return 0
        

ans = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            area = check_condition(i,j,k)
            ans = max(area, ans)

print(ans)