n, m, k = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
target_row = 0

for i in range(n):
    ispossible = True
    for j in range(k-1, k+m-1):
        if arr[i][j] != 0:
            ispossible = False
    
    if not ispossible:
        break
    target_row = i

for j in range(k-1, k+m-1):
    arr[target_row][j] = 1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end= " ")
    print()



        