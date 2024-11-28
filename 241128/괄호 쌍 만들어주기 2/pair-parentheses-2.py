N = [i for i in input()]
L = len(N)
cnt = 0
#a = set()
for i in range(L-1):
    if N[i] == '(' and N[i+1] == '(':
        for j in range(i+2, L-1):
            if N[j] == ')' and N[j+1] == ')':
                cnt += 1

print(cnt)