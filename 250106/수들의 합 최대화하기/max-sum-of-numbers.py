n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
rows = [False]*n
cols = [False]*n
answer = 0
ele = []
def solve(cnt):
    global answer
    if cnt == 3:
        answer = max(answer, sum(ele))
        return
    
    for i in range(n):
        for j in range(n):
            if not rows[i] and not cols[i]:
                ele.append(grid[i][j])
                rows[i] = True
                cols[i] = True
                solve(cnt+1)
                rows[i] = False
                cols[i] = False
                ele.pop()

solve(1)
print(answer)
# Write your code here!
