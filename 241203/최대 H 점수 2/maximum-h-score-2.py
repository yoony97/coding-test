#중간 값을 이용해볼까?

def H_score(li):
    max_H = 0
    for i in range(0, max(li)+1):
        cnt = 0
        for l in li:
            if l >= i:
                cnt +=1
        
        if cnt >= i:
            max_H = max(i, max_H)    
    return max_H

N, L = map(int, input().split())
numbers = list(map(int, input().split()))
mid = sorted(numbers)[N//2]
visited = [False]*N

for i in range(L):
    best_idx = -1
    min_diff = float('inf')
    #중간값으로 부터 가까운 것 부터 + 1 해주자.
    for a in range(N):
        if numbers[a] == mid or visited[a]:
            continue
        if min_dff > abs(mid - numbers[a]):
            best_idx = a
            min_dff = abs(mid - numbers[a])

    # L이 N이랑 같으면, 미드값도 더할 생각해야함
    if best_idx == -1:
        best_idx = N//2
    
    numbers[best_idx] += 1
    visited[best_idx] = True

print(H_score(numbers))