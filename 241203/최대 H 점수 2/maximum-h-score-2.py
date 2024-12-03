#최대 L개의 서로 다른 원소의 값을 1씩 올려 H 점수를 최대로 만드는 프로그램을 작성해 보세요.
#H 점수: 특정 수열이 주어졌을 때, H 이상인 숫자의 수가 H개 이상인 것을 만족하는 H 중 최댓값을 의미합니다.
from itertools import combinations

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
ans = 0
for i in combinations(range(N), L):
    copy = [n for n in numbers]
    for c in i:
        copy[c] += 1
    ans = max(ans, H_score(copy))
    #numbers 중에 L개를 뽑는 방법
print(ans)