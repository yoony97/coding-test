def solve1(n):
    if n == 0:
        return
    solve1(n-1)
    print(n, end=' ')
    


def solve2(n):
    if n == 0:
        return
    print(n, end=' ')
    solve2(n-1)

n = int(input())

solve1(n)
print()
solve2(n)