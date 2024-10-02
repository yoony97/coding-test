import sys
import numpy as np

data = sys.stdin.read().strip().split("\n")
N, B = map(int, data[0].split(" "))
matrix = [list(map(int, i.split(" "))) for i in data[1:]]
answer = [matrix[i].copy() for i in range(N)]



def calcuate(arr1, arr2, i, j):
    result = 0
    for k in range(N):
        result += arr1[i][k] * arr2[k][j]
    return result
    

    


# a[i][j] = a[i][0] * a[0][j] + ... + a[i][n]*a[n][j]
# a[0][0] = a[0][0]* a[0][0] + a[0][1]* a[1][0] + a[0][2]*a[2][0] + ... a[0][n] * a[n][0]
# a[0][1] = a[0][0]* a[0][1] + a[0][1]* a[1][1] + a[0][2]*a[2][1] + ... a[0][n] * a[n][1]

np.ling

for _ in range(B-1):
    temp = [[0]*N for i in range(N)]
    for i in range(N):
        for j in range(N):
            temp[i][j] = calcuate(answer, matrix, i, j)
    answer = temp

for i in answer:
    print(" ".join([str(j%1000) for j in i]))