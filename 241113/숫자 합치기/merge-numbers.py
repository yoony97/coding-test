from sortedcontainers import SortedList

n = int(input())
li = SortedList(list(map(int, input().split())))

answer = 0
while li:
    if len(li) > 2:
        a = li.pop(0)
        b = li.pop(0)
        li.add(a+b)
        answer += (a+b)
    else:
        answer += li[0] + li[1]
        print(answer)
        break
    