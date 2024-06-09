import sys
input = sys.stdin.read

def max_score(n, scores):
    if n == 1:
        return scores[0]
    elif n == 2:
        return scores[0] + scores[1]
    
    dp = [0] * n
    dp[0] = scores[0]
    dp[1] = scores[0] + scores[1]
    dp[2] = max(scores[0] + scores[2], scores[1] + scores[2])
    
    for i in range(3, n):
        dp[i] = max(dp[i-2] + scores[i], dp[i-3] + scores[i-1] + scores[i])
    
    return dp[-1]

data = input().strip().split("\n")

N = int(data[0])
scores = [int(i) for i in data[1:]]

# 결과 출력
print(max_score(N, scores))
