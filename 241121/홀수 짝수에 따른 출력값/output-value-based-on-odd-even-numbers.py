n = int(input())

def f(n):
    if n < 0:
        return 0
        
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    return f(n-2) + n


print(f(n))