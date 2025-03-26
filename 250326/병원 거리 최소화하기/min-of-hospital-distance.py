
#dist = abs(x2-x1) + abs(y2-y1)
n, m = map(int, input().split())
person = []
target = []

answer = float('inf')

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 1:
            person.append((i,j))
        if row[j] == 2:
            target.append((i,j))

def back(start, hist):
    global answer
    if len(hist) == m:
        temp = 0
        for px, py in person:
            min_temp = float('inf')
            for tx,ty in hist:
                dist = abs(px-tx) + abs(ty-py)
                min_temp = min(min_temp, dist)
            temp += min_temp
        answer = min(answer, temp)
        #print(hist, temp)
        return

    for i in range(start,len(target)):
        hist.append(target[i])
        back(i+1, hist)
        hist.pop()

back(0, [])
print(answer)
