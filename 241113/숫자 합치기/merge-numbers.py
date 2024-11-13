n = int(input())
li = list(map(int, input().split()))
li.sort()

answer = 0
while li:
    if len(li) > 1:
        a = li.pop(0)
        b = li.pop(0)
        li.append(a+b)
        answer += a+b
    else:
        answer += li.pop(0)

print(answer)