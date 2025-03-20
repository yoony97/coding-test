n = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(n)]
li = []
for s, e in intervals:
    li.append((s,+1))
    li.append((e,-1))

li.sort(key=lambda x: x[0])


answer = 0
temp = 0
for i in range(len(li)):
    temp += li[i][1]
    answer = max(temp, answer)

print(answer)