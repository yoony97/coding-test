ops = [i for i in input()]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
current = (0, 0)
dir_num = 3

for op in ops:
    if op == "L":
        dir_num -= 1
        if dir_num == -1:
            dir_num = 3

    if op == "R":
        dir_num = (dir_num+1)%4
    if op == "F":
        cx, cy = current
        cx+=dx[dir_num]
        cy+=dy[dir_num]
        current = (cx, cy)
print(current[0], current[1])