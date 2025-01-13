N = int(input())
memo = [-1]*(N+1)
def fibonnach(n):
    if memo[n] != -1:
        return memo[n]
    if n == 1:
        memo[n] = 1
        return 1
    if n == 2:
        memo[n] = 1
        return 1
    else:
        return fibonnach(n-1) + fibonnach(n-2)

print(fibonnach(N))

# Write your code here!
