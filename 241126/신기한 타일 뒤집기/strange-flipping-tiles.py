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
        left = current - x + 1
        right = current
        current = current - x + 1
        value = 1

    else:
        left = current
        right = current + x - 1
        value = 2
        current = current + x - 1

    li.append((left, right, value))

for (left, right, value) in li:
    for i in range(left, right+1):
        maps[i] = value
    
white, black = 0, 0
for i in range(2*OFFSET + 1):
    if maps[i] == 1:
        white += 1
    elif maps[i] == 2:
        black += 1 

print(white, black)