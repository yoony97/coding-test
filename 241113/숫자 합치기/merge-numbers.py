n = int(input())
li = list(map(int, input().split()))
li.sort()
#두 개 뽑아서
answer = 0
while li:
    if len(li) > 2:
        a = li.pop(0)
        b = li.pop(0)
        li.append(a+b)
        answer += (a+b)
    else:
        answer += li[0] + li[1]
        print(answer)
        break
    
#print(answer)