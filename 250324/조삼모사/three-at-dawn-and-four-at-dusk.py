#아침 점심이 뭔데
# 업무간의 상성
# 아침에 n//2 개, 저녁에 n//2개 하면 된다.
# 1,2 일을 한다 -> 12/21 일을 한다

from itertools import combinations
n = int(input())
answer = float('inf')
job_list = [i for i in range(n)]
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

# def combination(job):
#     result = []
#     for i in job:
#         for j in job:
#             if i != j:
#                 result.append((i,j))
#     return result


def back(idx, morning):
    global answer, job_list

    if len(morning) == n//2:
        mscore = 0
        ascore = 0
        afternoon = list(set(job_list) - set(morning))
        for x, y in combinations(morning,2):
            mscore += arr[x][y]
            mscore += arr[y][x]
        
        for x, y in combinations(afternoon,2):
            ascore += arr[x][y]
            ascore += arr[y][x]
        
        answer = min(answer, abs(mscore-ascore))
        return
    
    for i in range(idx+1, n):
        #if i not in morning:
        morning.append(i)
        back(i, morning)
        morning.pop()

#print(list(combinations([1,2,3],2)))
back(0, [])
print(answer)