#흥미로운 숫자 = 모든 자릿수에 있는 숫자는 같음, 한자리만 다른 숫자
X, Y = map(int, input().split())

def check(num):
    s = list(map(int, str(num)))
    temp = set(s)
    for i in temp:
        cnt = 0
        for k in s:
            if k  == i:
                cnt += 1 
        
        if (cnt == 1 or cnt == len(s) - 1) and len(temp) == 2:
            return True
    return False
    
            
ans = 0
for i in range(X,Y+1):
    if check(i):

        ans += 1
print(ans)