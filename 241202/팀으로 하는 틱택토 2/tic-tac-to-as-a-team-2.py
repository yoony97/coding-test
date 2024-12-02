import sys
inputs = sys.stdin.read().strip().split("\n")
lines = []
for i in inputs:
    line = tuple(map(int, i))
    lines.append(line)

#팀이 이긴다 == 컬럼 또는 로우 또는 대각선 한줄이 2개의 숫자로만 이루어져있다.
#가로
winner = []
for i in range(3):
    s = tuple(set(lines[i]))
    if len(s) == 2:
        winner.append(s)
#세로

for i in range(3):
    vertical = []
    for j in range(3):
        vertical.append(lines[i][j])
    s = tuple(set(vertical))
    if len(s) == 2:
        winner.append(s)

#대각선
type1 = [(0,0), (1,1), (2,2)]
type2 = [(0,2), (1,1), (2,0)] 
for ty in [type1, type2]:
    line = []
    for t in ty:
        i, j = t
        line.append(lines[i][j])
    
    s = tuple(set(line))
    if len(s) == 2:
        winner.append(s)

print(len(set(winner)))
