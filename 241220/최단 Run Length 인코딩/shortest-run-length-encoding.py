s = list(map(str, input()))
n = len(s)
ans = float('inf')

def rshift(s):
    temp = s[-1]
    for i in range(n-1, -1, -1):
        s[i] = s[i-1]
    s[0] = temp

def cal(s):
    encoded = ''
    char = s[0]
    cnt = 1
    for i in range(1, n):
        if char == s[i]:
            cnt += 1
        else:
            encoded += f"{char}{cnt}"
            char = s[i]
            cnt = 1
    encoded += f"{char}{cnt}"
    return encoded

for i in range(n):
    rshift(s)
    ans = min(ans, len(cal(s)))

print(ans)
# print(''.join(answer))
# print(cal(s))
# print(ans)



