import sys

data = sys.stdin.read().strip().split('\n')
N = int(data[0])
li = list(map(int, data[1].split()))
dp = [0]*N


dp[0] = li[0]

for i in range(1,N): 
    print(dp[i-1], li[i])
    dp[i] = max(dp[i-1]+ li[i], li[i])

print(max(dp))