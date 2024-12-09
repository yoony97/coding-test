N = int(input())
li = []
for i in range(N):
    height, weight = map(int, input().split())
    li.append((height, weight, i+1))

li.sort(key = lambda x: (x[0], -x[1]))

for i in li:
    print(' '.join([str(k) for k in i]))