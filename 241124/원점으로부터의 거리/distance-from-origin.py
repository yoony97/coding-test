n = int(input())
li = []
for idx in range(n):
    a, b = map(int, input().split())
    li.append((a,b,idx+1))

li.sort(key = lambda x: abs(x[0])+abs(x[1]))

for i in li:
    print(i[2])