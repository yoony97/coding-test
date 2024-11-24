a, b = map(int,input().split())
n = [int(i) for i in input()]

li = []

origin = 0
cns = 1

for i in n[::-1]:
    origin += i*cns
    cns *= a

while True:
    if origin < b:
        li.append(origin)
        break
    else:
        li.append(origin%b)
        origin = origin//b

for i in li[::-1]:
    print(i, end='')