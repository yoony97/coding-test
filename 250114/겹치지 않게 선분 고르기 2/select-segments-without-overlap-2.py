n = int(input())
start, end = [], []
for _ in range(n):
    a, b = map(int, input().split())
    start.append(a)
    end.append(b)

dp = [1]*n


def iscross(i, j):
    a, b = start[i], end[i]  
    x, y = start[j], end[j]

    if a <= x <=  b or a <= y <= b or x <=a <= y  or  x<=  b  <= y:
        return True
    return False
    


for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if not iscross(i,j):
            dp[i] = max(dp[i-1], dp[j]+1)
        
        
print(max(dp))
    
# Write your code here!
