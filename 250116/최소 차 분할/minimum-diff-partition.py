n = int(input())
arr = list(map(int, input().split()))

TOTAL = sum(arr)
dp = [float('inf')]*(TOTAL+1)
A = []
hist = []

def backtrack(cur_n):
    global dp, A, hist
    if cur_n == n:
        dp[sum(A)] = min(dp[sum(A)], abs(TOTAL-sum(A)-sum(A)))
        return

    for i in range(n):
        if not i in hist:
            A.append(arr[i])
            hist.append(i)
            backtrack(cur_n+1)
            A.pop()
            hist.pop()
            backtrack(cur_n+1)

backtrack(0)
print(min(dp))