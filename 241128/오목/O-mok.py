import sys
inputs = sys.stdin.read().strip().split("\n")
N = 19
maps = []
for i in inputs:
    maps.append(list(map(int, i.split())))
#print(maps)

def solve():
    for i in range(N-5):
        for j in range(N-5):
            if maps[i][j] != 0:
                iswin = True
                current = maps[i][j]
                for k in range(j, j+5):
                    if current != maps[i][k]:
                        iswin = False
                        break
                if iswin:
                    return i, (j+k)//2, current
                
                iswin = True    
                #2. 세로
                for k in range(i, i+5):
                    if current != maps[k][j]:
                        iswin = False
                        break
                if iswin:
                    return (i+k)//2, j, current
                
                iswin = True
                
                for k in range(1,5):
                    if current != maps[i+k][j+k]:
                        iswin = False
                        break
                if iswin:
                    #print(i+k, j+k)
                    return (i+k+2)//2, (j+k+2)//2, current
                
                # / 각선
                
                iswin = True
                for k in range(1, 5):
                    if not(0 <= i+k < N and 0 <= j-k < N) and current != maps[i+k][j-k]:
                        #print("!",i+k, j-k, current, maps[i+k][j-k])
                        iswin = False
                        break
                if iswin:
                    return (i+(i+5))//2, (j+(j-4))//2, current
                

    return 0, 0, 0

i, j, k = solve()
if k == 0:
    print(0)
else:
    print(k)
    print(i+1, j+1)
#print(solve())