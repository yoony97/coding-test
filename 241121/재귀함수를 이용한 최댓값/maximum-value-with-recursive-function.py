n = int(input())
li = list(map(int, input().split()))

def f(n):
    if n == 0:
        return li[n]
    if f(n-1) > li[n]:
        return f(n-1)
    else:
        return li[n]

print(f(n-1))