N, M, Q = map(int, input().split())
arr = []
op = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

for _ in range(Q):
    op.append(input().split())

def rshift(i):
    temp = arr[i][-1]
    for j in range(M-1, 0, -1):
        arr[i][j] = arr[i][j-1]
    arr[i][0]  = temp


def lshift(i):
    temp = arr[i][0]
    for j in range(M-1):
        arr[i][j] = arr[i][j+1]
    arr[i][-1] = temp

def check(i, target_row):
    for j in range(M):
        if arr[target_row][j] == arr[i][j]:
            return True
    return False


for (row, direct) in op:
    row = int(row) - 1
    if direct == 'L':
        rshift(row)
        target = 'R'
        current_row = row
        for offset in range(1, row+1):
            nr = row - offset
            if check(current_row, nr):
                if target == 'R':
                    lshift(nr)
                    target = 'L'
                else:
                    rshift(nr)
                    target = 'R'
                current_row = nr
            else:
                break
        
        target = 'R'
        current_row = row
        for offset in range(1, N-row):
            nr = row + offset        
            #print(nr, target)
            if check(current_row, nr):
                if target == 'R':
                    lshift(nr)
                    target = 'L'
                else:
                    rshift(nr)
                    target = 'R'
                current_row = nr
            else:
                break

    if direct == 'R':
        lshift(row)
        target = 'L'
        current_row = row
        for offset in range(1, row+1):
            nr = row - offset
            if check(current_row, nr):
                if target == 'R':
                    lshift(nr)
                    target = 'L'
                else:
                    rshift(nr)
                    target = 'R'
                current_row = nr
            else:
                break
        
        target = 'L'
        current_row = row
        for offset in range(1, N-row):
            nr = row + offset        
            #print(nr, target)
            if check(current_row, nr):
                if target == 'R':
                    lshift(nr)
                    target = 'L'
                else:
                    rshift(nr)
                    target = 'R'
                current_row = nr
            else:
                break



for i in range(N):
    for j in range(M):
        print(arr[i][j], end =' ')
    print()
