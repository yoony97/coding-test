n = int(input())
li = []

for i in range(n):
    name, path, area = input().split()
    li.append((name, path, area))

li.sort(key= lambda x : x[0])
print('name',li[-1][0])
print('addr',li[-1][1])
print('city',li[-1][2])

