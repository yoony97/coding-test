a, b = map(int, input().split())
answer = 0
for i in range(a,b+1):
    if not (i%2 == 0) and not (str(i)[-1] == '5') and not(i%3 == 0 and i%9 != 0):
        answer+=1
    
print(answer)