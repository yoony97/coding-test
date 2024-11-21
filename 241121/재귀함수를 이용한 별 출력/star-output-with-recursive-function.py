def p(n):
    if n == 0:
        return
    p(n-1)
    print("*"*n)

n = int(input())
p(n)