n = int(input())
arr = list(map(int, input().split()))
dp = [-float('inf')]*n
dp[0] = arr[0]
#dp[i]는 i번째 원소를 마지막원소라고 가정했을 떄의 조건에 맞는 합
for i in range(1,n):
    dp[i] = max(dp[i-1]+arr[i], arr[i])
# Write your code here!

print(max(dp))
