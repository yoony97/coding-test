#아침 점심이 뭔데
# 업무간의 상성
# 아침에 n//2 개, 저녁에 n//2개 하면 된다.
# 1,2 일을 한다 -> 12/21 일을 한다


n = int(input())
answer = float('inf')
job_list = [i for i in range(n)]
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))



def combination(arr, k):
    result =  []
    def _back(start,temp):
        if len(temp) == k:
            result.append(tuple(temp))
        
        for i in range(start, len(arr)):
            temp.append(arr[i])
            _back(i+1,temp)
            temp.pop()
    _back(0, [])
    return result



def back(idx, morning):
    global answer, job_list

    if len(morning) == n//2:
        mscore = 0
        ascore = 0
        afternoon = list(set(job_list) - set(morning))
        for x, y in combination(morning,2):
            mscore += arr[x][y]
            mscore += arr[y][x]
        
        for x, y in combination(afternoon,2):
            ascore += arr[x][y]
            ascore += arr[y][x]
        
        answer = min(answer, abs(mscore-ascore))
        return
    
    for i in range(idx+1, n):
        #if i not in morning:
        morning.append(i)
        back(i, morning)
        morning.pop()

# #print(list(combinations([1,2,3],2)))
back(0, [])
print(answer)


#print(result)