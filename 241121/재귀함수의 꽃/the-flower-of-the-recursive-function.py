N = int(input())

def p(n):
    if n == 0: 
        return
    print(n, end=' ')
    p(n-1)
    print(n, end=' ')

p(N)