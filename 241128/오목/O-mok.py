import sys
inputs = sys.stdin.read().strip().split("\n")
N = 19
maps = []
for i in inputs:
    maps.append(list(map(int, i.split())))
#print(maps)

def solve():
    for i in range(N):
        for j in range(N):
            if maps[i][j] != 0:
                iswin = True
                current = maps[i][j]
                for k in range(j, j+5):
                    if 0 <= i < N and 0 <= k < N:
                        if current != maps[i][k]:
                            iswin = False
                            break
                    else:
                        iswin = False
                        break
                
                if iswin:
                    #print("ㅡ")
                    return i, (j+k)//2, current
                
                iswin = True    
                #2. 세로
                for k in range(i, i+5):
                    if 0 <= k < N and 0 <= j < N:
                        if current != maps[k][j]:
                            iswin = False
                            break
                    else:
                        iswin = False
                        break
                    
                if iswin:
                    return (i+k)//2, j, current
                
                iswin = True
                for k in range(1,5):
                    if 0<= i+k < N and 0 <= j+k < N:
                        if current != maps[i+k][j+k]:
                            iswin = False
                            break
                    else:
                        iswin = False
                        break
                        
                if iswin:
                    return (i+k+2)//2, (j+k+2)//2, current
                
                # / 각선
                
                iswin = True
                for k in range(1, 5):
                    #범위에 벗어나고 current
                    if not(0 <= i+k < N and 0 <= j-k < N) or current != maps[i+k][j-k]:
                        
                        iswin = False
                        break

                if iswin:
                    #print("/")
                    return (i+(i+5))//2, (j+(j-4))//2, current
                

    return 0, 0, 0

i, j, k = solve()
if k == 0:
    print(0)
else:
    print(k)
    print(i+1, j+1)
#print(solve())