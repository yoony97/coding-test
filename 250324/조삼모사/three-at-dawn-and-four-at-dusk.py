#아침 점심이 뭔데
# 업무간의 상성
# 아침에 n//2 개, 저녁에 n//2개 하면 된다.
# 1,2 일을 한다 -> 12/21 일을 한다

# def combination(job, ):
n = int(input())
answer = float('inf')
job_list = [i for i in range(n)]
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

def combination(job):
    result = []
    for i in job:
        for j in job:
            if i != j:
                result.append((i,j))
    return result


def back(morning):
    global answer, job_list

    if len(morning) == n//2:
        mscore = 0
        ascore = 0
        afternoon = list(set(job_list) - set(morning))
        for x, y in combination(morning):
            mscore += arr[x][y]
        
        for x, y in combination(afternoon):
            ascore += arr[x][y]
        
        answer = min(answer, abs(mscore-ascore))
        return
    
    for i in range(n):
        if i not in morning:
            morning.append(i)
            back(morning)
            morning.pop()

back([])
print(answer)