def f(n):
    if 0< n <= 2:
        return 1
    else:
        return f(n-1) + f(n-2)

n = int(input())

print(f(n))