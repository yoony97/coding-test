n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
row, col = map(int, input().split())    
def boom(i,j, arr):
    rnge = arr[i][j]-1
    for k in range(i-rnge, i+rnge+1):
        if 0 <= k < n:
            arr[k][j] = 0
        
    
    for k in range(j-rnge, j+rnge+1):
        if 0 <= k < n:
            arr[i][k] = 0
    return arr

def drop(arr):
    for i in range(n):
        temp =  []
        cnt = 0
        for j in range(n):
            if arr[j][i] != 0:
                temp.append(arr[j][i])
                arr[j][i] = 0
            else:
                cnt += 1
        idx = 0
        for k in range(cnt,n):
            arr[k][i] = temp[idx]
            idx += 1
    return arr

arr = boom(row-1, col-1, arr)
arr = drop(arr)


for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()
#print(arr)
