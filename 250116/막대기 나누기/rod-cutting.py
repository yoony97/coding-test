n = int(input())
profit = list(map(int, input().split()))
dp = [0]*(n+1)
#dp[1] = profit[0]
#길이가 i일 때, 최대 가격 dp[i]
#dp[i]에서 현재 단위 j 를 빼고,  가격으로 채울 경우와 현재 가격 중  최대 값을 넣으면 되지
# Write your code here!

for j in range(1,n+1):
    for i in range(n+1):
        if i - j >=0:
            dp[i] = max(dp[i-j]+ profit[j-1], dp[i])
print(dp[n])
