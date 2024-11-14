N = int(input())
current = [i for i in input()]
target = [i for i in input()]

mismatch = False
groups = []
temp = []
for i in range(N):
    if current[i] != target[i]:
        temp.append(current[i])
        if len(temp) == 4:
            groups.append(temp)
            temp = []
    else:
        if temp:
            groups.append(temp)
            temp = []

if temp:
    groups.append(temp)
    

print(len(groups))