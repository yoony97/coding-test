#바이러스 실험
"""
#섭취
바이러스는 자기 칸에 있는 양분을 나이만큼 섭취
같은 칸에 여러 개 바이러스 있으면, 나이 어린 바이러스부터 섭취

#죽음
모든 바이러스가 섭취가 끝나면, 죽은 바이러스가 나이//2 값의 양분으로 변함

#번식
5의 배수의 나이를 가진 바이러스는 번식함
8개의 칸에 나이가 1인 바이러스가 생김

#풀기 쉬웠음
#나오는 설명 그대로 구현하면됨
#여기서 sort 하는 방식이 좀 더 괜찮은 게 없을까?
   -> 자료구조를 적극 활용하자. 우선순위 큐를 고려해야한다.

"""
import heapq

#init
n, m, k = map(int, input().split())
food = [[5]*n for _ in range(n)]
new_food = []
virus = []
dx = [1,0,-1,0,-1,1,-1,1]
dy = [0,1,0,-1,-1,1,1,-1]



for i in range(n):
    row =list(map(int, input().split()))
    new_food.append(row)

for _ in range(m):
    r, c, age = map(int, input().split())
    heapq.heappush(virus,(age, r-1, c-1))

def eat(virus):
    dead_virus = []
    new_virus = []
    while virus:
        age, r, c = heapq.heappop(virus)
        if food[r][c] >= age:
            food[r][c] -= age
            heapq.heappush(new_virus, (age+1, r, c))
        else:
            dead_virus.append((age, r, c))
    
    return new_virus, dead_virus

def die(dead_virus):
    for age, r, c in dead_virus:
        food[r][c] += age//2
    

def divide(virus):
    new_virus = []
    while virus:
        age, r, c = heapq.heappop(virus)  # heap에서 하나씩 꺼냄
        heapq.heappush(new_virus, (age, r, c))  # 다시 heap에 넣음 (heap 유지)
        if age % 5 == 0:
            for i in range(8):
                nr = r + dx[i]
                nc = c + dy[i]
                if 0 <= nr < n and 0 <= nc < n:
                    heapq.heappush(new_virus, (1, nr, nc))
    return new_virus

def injection():
    for i in range(n):
        for j in range(n):
            food[i][j] += new_food[i][j]

for _ in range(k):
    virus, dead_virus = eat(virus) # 1번
    die(dead_virus) #2번
    virus = divide(virus) #3번
    injection() #4번
    #print(food)
    #print(virus)
    #print(food)

print(len(virus))


