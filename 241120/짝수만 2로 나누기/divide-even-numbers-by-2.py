n = int(input())
li = list(map(int, input().split()))

def solve(li,n):
    for i in range(n):
        if li[i]%2 == 0:
            li[i] = li[i]//2

solve(li,n)
print(' '.join([str(i) for i in li]))
