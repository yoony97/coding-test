n = int(input())
li = []
for _ in range(n):
    name, height, weight = input().split()
    li.append((name, int(height), int(weight)))

li.sort(key = lambda x: (x[1], -x[2]))

for i in li:
    print(' '.join([str(s) for s in i ]))