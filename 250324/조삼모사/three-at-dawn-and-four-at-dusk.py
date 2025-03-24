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



def calc_score(team):
    score = 0
    length = len(team)
    for i in range(length):
        for j in range(i+1, length):
            score += arr[team[i]][team[j]] + arr[team[j]][team[i]]
    return score

def back(start, morning):
    global answer
    if len(morning) == n // 2:
        # 나머지 작업은 저녁(또는 다른 팀)
        afternoon = [i for i in range(n) if i not in morning]
        m_score = calc_score(morning)
        a_score = calc_score(afternoon)
        answer = min(answer, abs(m_score - a_score))
        return
    for i in range(start, n):
        morning.append(i)
        back(i+1, morning)
        morning.pop()


# #print(list(combinations([1,2,3],2)))
back(0, [])
print(answer)


#print(result)