import sys 
inputs = sys.stdin.read().strip().split("\n")
N, M = map(int, inputs[0].split())
arr = list(map(int, inputs[1:]))
answer = [i for i in arr]


def boom(arr, N):
    answer = [i for i in arr]
    result=  []
    ischange = False
    cnt = 1
    for i in range(1, N):
        if arr[i-1] == arr[i]:
            cnt += 1 
        else:
            if cnt >= M:
                #boom
                ischange = True
                for j in range(N):
                    #
                    if i-cnt<= j < i:
                        answer[j] = 0
            cnt = 1
        
    if cnt >= M:
        ischange = True
        for j in range(N):
            #
            if N-cnt<= j < N:
                answer[j] = 0
            
    for i in range(N):
        if answer[i] != 0:
            result.append(answer[i])
    
    return result, ischange
    
flag = True
for i in range(N):
    arr, flag = boom(arr, len(arr))
    #print(arr, flag)

if len(arr) == 0:
    print(0)
else:
    print(len(arr))
    print('\n'.join([str(i) for i in arr]))
    