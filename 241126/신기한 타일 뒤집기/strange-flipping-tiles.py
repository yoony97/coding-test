#L 흰, R 검

OFFSET = 100000
current = OFFSET
maps = [0]*(2*OFFSET + 1)
li = []
n = int(input())
current = OFFSET
for _ in range(n):
    x, d = input().split()
    x = int(x)
    if d == 'L':
        right = current
        left = current - x
        current -= x
        value = 1
    else:
        right = current + x
        left = current
        value = 2
        current += x
    li.append((left, right, value))

for (left, right, value) in li:
    for i in range(left, right):
        maps[i] = value
    
white, black = 0, 0
for i in range(2*OFFSET + 1):
    if maps[i] == 1:
        white += 1
    elif maps[i] == 2:
        black += 1 

print(white, black)