def calculate(s):
    if len(s) == 1 and s[0] == '0':
        return 0

    result = 0
    n = 1
    for i in s[::-1]:
        i = int(i)
        result += i*n
        n *= 2 
    return result

N = [str(i) for i in input()]
ans = 0

for i in range(len(N)):
    CN = [j for j in N]
    if CN[i] == '1':
        CN[i] = '0'
    elif CN[i] == '0':
        CN[i] = '1'
    #print(CN)
    ans = max(ans, calculate(CN))

print(ans)