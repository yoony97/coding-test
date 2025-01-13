N = int(input())
memo = [-1]*(N+1)
def fibonnach(n):
    if memo[n] != -1:
        return memo[n]
    if n <= 2:
        memo[n] = 1
    
    else:
        memo[n] = fibonnach(n - 1) + fibonnach(n - 2) 

    return memo[n]
    
print(fibonnach(N))

# Write your code here!
