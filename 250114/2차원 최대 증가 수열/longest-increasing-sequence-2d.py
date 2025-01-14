n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
#점프 # nx > x  and  ny > y and grid[nx][ny] > grid[x][y] 점프 조건ㄴ 
# Write your code here!
dp = [[-float('inf')]*n for i in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        for nx in range(i+1, n):
            for ny in range(j+1, n):
                if grid[nx][ny] > grid[i][j]:
                    dp[nx][ny] = max(dp[nx][ny], dp[i][j]+1)

answer = 0
for i in range(n):
    answer = max(max(dp[i]), answer)

#print(dp)
print(answer)
