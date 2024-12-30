N  = int(input())
lines = []
selected = [0]*N
answer = 0

for _ in range(N):
    x, y = map(int, input().split())
    lines.append((x,y))

def duplicate(point1, point2):
    x1, x2 = point1
    x3, x4 = point2

    
    if x1 > x2:
        x1, x2 = x2, x1
    if x3 > x4:
        x3, x4 = x4, x3

    return max(x1, x3) <= min(x2, x4)

def solve(target):
    global answer 
    if target == N: 
        for i in range(N):
            if selected[i]:
                cur = lines[i]
                for j in range(N):
                    if i == j or not selected[j]:
                        continue
                    if duplicate(lines[i], lines[j]):
                        return 
        answer  = max(sum(selected), answer)
        return
    
    selected[target] = 1
    solve(target+1)
    selected[target] = 0

solve(0)
print(answer)