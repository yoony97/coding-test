#흥미로운 숫자 = 모든 자릿수에 있는 숫자는 같음, 한자리만 다른 숫자
X, Y = map(int, input().split())

def check(num):
    cnt = 0
    s = list(map(int, str(num)))
    temp = set(s)
    for i in range(1, len(s)):
        if s[i-1] != s[i]:
            cnt += 1
        if cnt > 2:
            return False
    #print(num, cnt, temp)
    if cnt <=2 and len(temp) == 2:
        return True
    
    return False        
            
ans = 0
for i in range(X,Y+1):
    if check(i):
        ans += 1
print(ans)