n = [i for i in input()]
LEN = len(n)
cnt = 0
for i in range(LEN):
    if n[i] == '(':
        for j in range(i,LEN):
            if n[j] == ')':
                cnt += 1

print(cnt)