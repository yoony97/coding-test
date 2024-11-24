n = int(input())
li = []
for _ in range(n):
    name, kor, eng, ma = input().split()
    li.append((name, int(kor), int(eng), int(ma)))

li.sort(key = lambda x: (x[1], x[2]))

for i in li[::-1]:
    print(' '.join([str(s) for s in i]))