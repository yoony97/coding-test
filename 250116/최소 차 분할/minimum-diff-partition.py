n = int(input())
arr = list(map(int, input().split()))

TOTAL = sum(arr)
dp = [0]*(TOTAL+1)

def backtrack(cur_n, A, hist):
    if cur_n == n:
        if not A:
            dp[0] = TOTAL
        else:
            dp[sum(A)] = abs(TOTAL-sum(A))
        return

    for i in range(n):
        if not i in hist:
            A.append(arr[i])
            hist.append(i)
            backtrack(cur_n+1, A, hist)
            A.pop()
            hist.pop()

#DP 테이블을 뭘 줘야할까?
#DP[i]는 A의 합이 i 일 때, |A-B|의 값이라 하면 좀 이상한가?

# Write your code here!

backtrack(0, [], [])
print(dp)