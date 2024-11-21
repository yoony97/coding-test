N = int(input())

def p(n):
    if n == 0: 
        return
    print("* "*n)
    p(n-1)
    print("* "*n)

p(N)