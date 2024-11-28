def calculate(s):
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
    CN = [i for i in N]
    if CN[i] == '1':
        CN[i] = '0'
    if CN[i] == '0':
        CN[i] = '1'
    ans = max(ans, calculate(CN))

print(ans)