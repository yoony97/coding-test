yellow = [[0]*4 for _ in range(6)]
red =  [[0]*6 for _ in range(4)]


def input_block(t,x,y, arr):
    depth = 0
    if t == 2:
        for row in range(6):
            if arr[row][y] != 0 or arr[row][y+1] != 0:
                break
            depth += 1
        
        arr[depth-1][y] = 1
        arr[depth-1][y+1] = 1

    elif t == 3: 
        for row in range(5):
            if arr[row][y] != 0 or arr[row+1][y] !=0:
                break
            depth += 1

        arr[depth-1][y] = 1
        arr[depth][y] =1
    else:
        for row in range(6):
            if arr[row][y] != 0:
                break
            depth += 1
        arr[depth-1][y] = 1


def down(arr, start_row):
    for row in range(start_row, 0,-1):
        for col in range(4):
            arr[row][col] = arr[row-1][col]
    
    arr[0] = [0,0,0,0]

def check(arr):
    count = 0
    for row in range(2): #0,1 행만 관리함
        if sum(arr[row]) >= 1:
            count += 1
    
    for i in range(count):
        down(arr, 5)



def calculate(arr):
    score = 0
    for row in range(5,-1,-1):
        if sum(arr[row]) == 4:
            score+= 1
            down(arr, row)
    return score


def transpose(arr):
    return list([list(i) for i in zip(*arr)])

#red = transpose(red)
K = int(input())
blocks = []
score = 0
red_type = {2:3, 3:2, 1:1}
for _ in range(K):
    red = transpose(red)
    t, x, y = map(int, input().split())
    input_block(t,x,y,yellow)
    input_block(red_type[t],y,x,red)
    score += calculate(yellow)
    score += calculate(red)
    check(yellow)
    check(red)
    red = transpose(red)


block_sum = 0
for i in yellow:
    block_sum += sum(i)
for i in red:
    block_sum += sum(i)

print(score)
print(block_sum)