arr = []
for _ in range(4):
    arr.append(list(map(int, input().split())))
op = input()



#Right
def left(li):
    temp = []
    answer = []
    for i in range(4):
        if li[i] != 0:
            temp.append(li[i])
        
    for i in range(1, len(temp)):
        if temp[i-1] == temp[i]:
            answer.append(temp[i-1]*2)
            temp[i] = 0
        else:
            answer.append(temp[i-1])
    if len(temp) > 1:
        if temp[-1] == temp[-2]:
            answer.append(temp[-2]*2)
            temp[-1] = 0
        else:
            answer.append(temp[-1])


    while 0 in answer:
        idx = answer.index(0)
        del answer[idx]

    for _ in range(4-len(answer)):
        answer.append(0)
    
    return answer

def right(li):
    temp = []
    answer = []
    for i in range(4):
        if li[i] != 0:
            temp.append(li[i])
    
    for i in range(len(temp)-1, 0, -1):
        if temp[i-1] == temp[i]:
            answer.insert(0, temp[i]*2)
            temp[i-1] = 0
        else:
            answer.insert(0, temp[i])
    if len(temp) > 1:
        if temp[0] == temp[1]:
            answer.insert(0, temp[0]*2)
            temp[i-1] = 0
        else:
            answer.insert(0, temp[0])

    while 0 in answer:
        idx = answer.index(0)
        del answer[idx]

    for _ in range(4-len(answer)):
        answer.insert(0, 0)
    
    return answer



if op == 'L':
    for i in range(4):
        temp = left(arr[i])
        for j in range(4):
            arr[i][j] = temp[j]

if op == 'R':
    for i in range(4):
        temp = right(arr[i])
        for j in range(4):
            arr[i][j] = temp[j]

if op == 'U':
    for j in range(4):
        temp = []
        for i in range(4):
            temp.append(arr[i][j])
        temp = left(temp)
        
        for i in range(4):
            arr[i][j] = temp[i]

if op == 'D':
    for j in range(4):
        temp = []
        for i in range(4):
            temp.append(arr[i][j])
        temp = right(temp)
        
        for i in range(4):
            arr[i][j] = temp[i]






for i in range(4):
    for j in range(4):
        print(arr[i][j], end= ' ')
    print()
    


