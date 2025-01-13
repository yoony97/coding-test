N = int(input())

def fibonnach(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonnach(n-1) + fibonnach(n-2)

print(fibonnach(N))

# Write your code here!
