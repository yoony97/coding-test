from itertools import combinations

N = int(input())
points = []
ranges = [i for i in range(0, 11)]
ans = 0

def check(xs, ys): 
    valid = [False]*N
    for x in xs:
        for i in range(N):
            if x == points[i][0]:
                valid[i] = True
    
    for y in ys:
        for i in range(N):
            if y == points[i][1]:
                valid[i] = True
    
    for i in valid:
        if not i:
            return False
    return True

def solve(nx, ny):
    for xs in combinations(ranges,nx):
        for ys in combinations(ranges,ny):
            if check(xs,ys):
                return True
    return False


for i in range(N):
    a, b = map(int,input().split())
    points.append((a,b))


for nx in range(0, 4):
    ny = 3 - nx
    #print(nx, ny)
    if solve(nx, ny):
        ans = 1
        break

print(ans)