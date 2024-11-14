n = int(input())
current = input()
target = input()
groups = []
temp = []
for (c, t) in zip(current, target):
    if c == t:
        if temp:
            groups.append(temp)
            temp = []
    else:
        temp.append(c)

print(len(groups))



#GHHHGHH
#HHGGGHH
