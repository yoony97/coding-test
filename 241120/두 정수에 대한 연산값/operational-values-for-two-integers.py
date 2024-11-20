n, m = map(int, input().split())

def f(n,m):
    if n > m:
        n += 25
        m = m*2
    else:
        m+= 25
        n = n*2
    return n, m

n, m = f(n,m)
print(n,m)