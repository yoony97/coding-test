from itertools import permutations

N = int(input())
li = list(map(int, input().split())) #[a+b, b+c, c+d, d+e]

def solve():
    for i in permutations(range(1, N+1)):
        isfind = True
        for p in range(1, N-1):
            if not(i[p] + i[p-1] == li[p-1]):
                isfind = False
                break
        if isfind:
            print(' '.join([str(a) for a in i]))
            return 

solve()