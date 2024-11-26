#L: 흰색, R: 검은색
#마지막으로 칠한 타일 위에 위치
#흰색 + 검은색 = 회색

n = int(input())
OFFSET = 100000
current = OFFSET
MAX_LEN = 200000
li = []
maps = [0]*(MAX_LEN+1)
counts = [[0,0] for _ in range((MAX_LEN+1))]
for i in range(n):
    x, direction = input().split()
    x = int(x)
    if direction == 'L':
        left_section = current - x
        right_section = current 
        current = current - x
        value = 1
    else:
        left_section = current
        right_section = current + x
        value = 2
        current = current + x

    li.append((left_section, right_section, value))


for (left, right, value) in li:
    for i in range(left, right):
        maps[i] = value
        if value == 1:
            counts[i][0] += 1
        elif value == 2:
            counts[i][1] += 1
        

white, black, gray = 0, 0, 0 

for i in range(MAX_LEN+1):
    if counts[i][0] >= 2 and counts[i][1] >= 2:
        gray += 1
    else: 
        if maps[i] == 1:
            white += 1
        elif maps[i] == 2:
            black += 1
            

print(white, black, gray)
