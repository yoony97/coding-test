n = int(input())
li = []
for idx in range(n):
    height, weight = map(int, input().split())
    li.append((height, weight, idx+1))

li.sort(key = lambda x: (-x[0], -x[1], x[2]))
for i in li:
    print(" ".join([str(s) for s in i]))
    