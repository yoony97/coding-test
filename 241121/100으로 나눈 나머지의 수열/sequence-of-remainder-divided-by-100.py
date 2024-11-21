n = int(input())

def f(n):
    if n == 1:
        return 2
    elif n == 2:
        return 4
    else:
        return (f(n-1)*f(n-2))%100

print(f(n))