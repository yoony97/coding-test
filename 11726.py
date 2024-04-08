n = int(input())


# 2xn 타일 존재
# 1x2, 2x1 타일로 채우는 방법의 수

# n = 1 -> 1
# n = 2 -> 2
# n = 3 -> 3
# n = 4 -> 5
# n = 5 -> 8
dp = [0]*1001
dp[0] = 1
dp[1] = 2

def solution(n):
    for i in range(2,n):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n-1]


if __name__ == '__main__':
    print(solution(n)%10007)

