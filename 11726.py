n = int(input())

dp = [0]*1001
dp[0] = 1
dp[1] = 2

def solution(n):
    for i in range(2,n):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n-1]


if __name__ == '__main__':
    print(solution(n)%10007)

