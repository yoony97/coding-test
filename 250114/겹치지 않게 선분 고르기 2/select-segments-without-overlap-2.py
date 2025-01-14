n = int(input())
segments= []
for _ in range(n):
    a, b = map(int, input().split())
    segments.append((a,b))
    
segments.sort(key = lambda x : x[1])

dp = [0]*n

def iscross(i, j):
    a, b = segments[i]
    x, y = segments[j]
    return not (b < x or y < a)
    # if a <= x <=  b or a <= y <= b or x <= a <= y  or  x<=  b  <= y:
    #     return True
    # return False
    
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if not iscross(i,j):
            dp[i] = max(dp[i], dp[j]+1)
        
        
print(max(dp))
    
# Write your code here!
