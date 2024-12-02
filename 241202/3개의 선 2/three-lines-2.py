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
    coord  = list()
    if n == 1:    
        for i in range(len(X)):
            coord.append([X[i]])

    if n == 2:    
        for i in range(len(X)):
            for j in range(i+1, len(X)):
                coord.append([X[i],X[j]])
    if n == 3:
        for i in range(len(X)):
            for j in range(i+1, len(X)):
                for k in range(j+1, len(X)):
                    coord.append([X[i],X[j], X[k]])        
    return coord

def solve(cxss, cyss):
    for cxs in cxss:
        for cys in cyss:
            if check(cxs, cys):
                return True
    return False


def check(cx, cy):
    remains = []
    for p in points:
        iscrossed = False
        for x in cx:
            if x == p[0]:
                iscrossed = True
                break
        
        if not iscrossed:
            remains.append(p)

    for r in remains:
        iscrossed = False
        for y in cy:
            if r[1] == y:
                iscrossed = True
                break
        if not iscrossed:
            return  False
    return True

            
ans = 0
Xs = list(Xs)
Ys = list(Ys)

for nx in range(1,4): # nx: x와 평행한 직선 개수
    ny = 3 -  nx      # ny: y와 평행한 직선 개수
    cxss = select(Xs, nx)
    cyss = select(Ys, ny)
    if solve(cxss, cyss):
        ans = 1 
        break
    
print(ans)
        
    
        
    


        



