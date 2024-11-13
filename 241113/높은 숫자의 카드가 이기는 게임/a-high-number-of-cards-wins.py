import sys

inputs = sys.stdin.read().strip().split("\n")
n = int(inputs[0])
cards = set([i for i in range(1,2*n+1)])
B_cards = list(map(int, inputs[1:]))

A_cards= cards - set(B_cards)
A_cards = list(A_cards)

A_cards.sort()
B_cards.sort()
idx = 0
answer = 0
for i in B_cards:
    fail = False
    while i > A_cards[idx]:
        if idx+1 < n:
            idx+=1
        else:
            fail = True
            break
    if fail:
        break
    else:
        answer+=1
        if idx+1 < n:    
            idx+=1
        else:
            break
print(answer)


    