def f(n):
    if n <=2:
        return n
    else:
        return f(n//3) + f(n-1)

n = int(input())

print(f(n))