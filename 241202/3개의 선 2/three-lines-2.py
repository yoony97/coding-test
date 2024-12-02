N = int(input())
points = []
Xs = set()
Ys = set()

for i in range(N):
    a, b = map(int,input().split())
    points.append((a,b))
    Xs.add(a)
    Ys.add(b)


def select(X, n):
    coord  = set()
    if n == 1:    
        for i in range(len(X)):
            coord.add((X[i]))

    if n == 2:    
        for i in range(len(X)):
            for j in range(i+1, len(X)):
                coord.add((X[i],X[j]))
    if n == 3:
        for i in range(len(X)):
            for j in range(i+1, len(X)):
                for k in range(j+1, len(X)):
                    coord.add((X[i],X[j], X[k]))        
    return coord

ans = 0
Xs = list(Xs)
Ys = list(Ys)
for nx in range(1,4): # nx: x와 평행한 직선 개수
    ny = 3 -  nx      # ny: y와 평행한 직선 개수
    fail = False
    cxs = select(Xs, nx)
    cys = select(Ys, ny)

    remains = []
    for point in points:
        ispass = False
        for cx in cxs:
            if cx == point[0]:
                ispass  = True
        
        if not ispass:
            remains.appnd(point)
    # 선택한 직선을 지나지 않는 남는 점들
    for point in remains:
        ispass = False
        for cy in cys:
            if cy == point[1]:
                ispass  = True
        #남는 점들 중 하나라도 지나지 않으면, False    
        if not ispass:
            fail = True
    
    if not fail:
        ans = 1
        break

print(ans)
        
    
        
    


        



