clue = list(map(int, input().split()))
def solve() :
    for A in range(1,41):
        for B in range(1,41):
            for C in range(1,41):
                for D in range(1,41):
                    condition = A in clue and B in clue and C in clue and D in clue
                    condition2 =  A+B in clue and B + C in clue and C + D in clue and A+D in clue and B+D in clue and A+C in clue
                    condition3 =  A + B + C in clue and A + B + D in clue and A + C + D in clue and B + C + D in clue
                    condition4 =  A + B + C + D in clue
                    if condition and condition2 and condition3 and condition4:
                        print(A,B,C,D)
                        return

solve()
                        

