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
"""


#init
n, m, k = map(int, input().split())
food = [[5]*n for _ in range(n)]
virus = []
dx = [1,0,-1,0,-1,1,-1,1]
dy = [0,1,0,-1,-1,1,1,-1]


for i in range(n):
    row =list(map(int, input().split()))
    for j in range(n):
        food[i][j] += row[j]

for _ in range(m):
    r, c, age = map(int, input().split())
    virus.append((age, r-1, c-1)) #0-based index

def age_sort(arr):
    return sorted(arr, key = lambda x: x[0])

def eat(virus):
    virus = age_sort(virus)
    dead_virus = []
    new_virus = []
    for age, r, c in virus:
        if food[r][c] >= age:
            food[r][c] -= age
            new_virus.append((age+1, r, c))
        else:
            dead_virus.append((age, r, c))
    return new_virus, dead_virus

def die(dead_virus):
    for age, r, c in dead_virus:
        food[r][c] += age//2
    

def divide(virus):
    new_virus = [i for i in virus]
    for age, r, c in virus:
        if age%5 == 0:
            for i in range(8):
                nr = r + dx[i]
                nc = c + dy[i]
                if 0 <= nr < n and 0 <= nc < n:
                    new_virus.append((1, nr, nc))
    
    return new_virus

for _ in range(k):
    virus, dead_virus = eat(virus)
    die(dead_virus)
    virus = divide(virus)
    # print(virus)
    # print(food)

print(len(virus))