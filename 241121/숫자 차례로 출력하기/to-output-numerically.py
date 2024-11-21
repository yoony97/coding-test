def solve1(c, n):
    if c == n+1:
        return
    print(c, end=' ')
    solve1(c+1, n)
    


def solve2(n):
    if n == 0:
        return
    print(n, end=' ')
    solve2(n-1)

n = int(input())

solve1(1, n)
print()
solve2(n)