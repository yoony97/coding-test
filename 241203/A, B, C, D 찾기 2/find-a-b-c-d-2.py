clue = list(map(int, input().split()))
clue.sort() 
def solve() :
    for A in range(1,11):
        for B in range(1,11):
            for C in range(1,11):
                for D in range(1,11):
                    find = True
                    result = [A, B, C, D, A + B, B + C, C + D, D + A, A + C, B + D, A + B + C, A + B + D, A + C + D, B + C + D, A + B + C + D]
                    result.sort()
                    for r, c in zip(result, clue):
                        if r != c:
                            find = False
                    if find:
                        print(A, B, C, D)
                        return
solve()
                        

