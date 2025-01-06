n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
rows = [False]*n
cols = [False]*n
answer = 0
ele = []
def solve(cnt):
    global answer
    if cnt == n:
        #print(ele)
        answer = max(answer, sum(ele))
        return
    
    for i in range(n):
        for j in range(n):
            if not rows[i] and not cols[j]:
                ele.append(grid[i][j])
                rows[i] = True
                cols[j] = True
                solve(cnt+1)
                rows[i] = False
                cols[j] = False
                ele.pop()

solve(0)
# if n  == 1:
#     print(grid[0][0])
# else:
print(answer)
# Write your code here!
