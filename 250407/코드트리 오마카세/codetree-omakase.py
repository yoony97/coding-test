#원형 벨트에 l개의 의자가 있음
## 의자 위치 x[x_1, x_2, ..., x_{L-1}라고 했을 때, x = 0을 기점으로 시게 방향으로 위치함
# 의자 앞에 초밥 여러개 가능
# 초밥은 1초에 한칸씩 회전 
# 처음에는 벨트위에 초밥이 없음, 의자에 사람도 없음
def make_sushi():
    """
        t초에 회전 한번 일어난 이후, 시각 t에 위치 x앞에 있는 벨트 위에 name 이름을 부착한 회전초밥을 올림
        이름이 적혀 있는 초밥이 같은 위치에 여러개 놓여 잇을 수 잇음
    """
    pass

def enter_guest():
    """
        t초에 회전 한번 일어난 이후, 이름이 name인 사람이 시각 t에 x 의자에 앉음
        이때부터 위치 x 앞으로 오는 초밥들 중 자신의 이름이 적혀 있는 초밥을 정확히 n개 먹고 자리를 떠남
        만약 시각 t에 위치 x에 자신의 이름이 적혀있는 초밥이 놓여있다면 바로 먹음
        동시에 여러개 있다면 여러개 먹을 수 있음
        시간 소요 안됨
    """
    pass
def take_picture():
    """
        초밥 회전 발생 후, 손님이 앉아있는 자리에서 자신의 이름이 적힌 초밥을 먹은 뒤 시간 t에 오마카세 집 촬영함, 
        현재 남아있는 사람 수와 초밥 수를 출력함
    """
    pass
from collections import deque

L, Q = map(int, input().split())
m2p = {}
people = [0]*L
sushi = [deque([]) for _ in range(L)]
prev_t = 0

def rotate(sushi):
    new_sushi = [sushi[-1]]
    for i in range(L-1):
        new_sushi.append(sushi[i])

    return new_sushi

def eat(sushi):
    for i in range(L):
        if people[i] > 0:
            name = m2p[i]
            temp = deque([])
            while sushi[i]:
                if people[i] == 0: #다먹은 경우
                    del m2p[i]
                    break
                s_name = sushi[i].popleft()
                if name == s_name:
                    people[i] -= 1
                else:
                    temp.append(s_name)
        
            while sushi[i]:
                s_name = sushi[i].popleft()
                temp.append(s_name)
            sushi[i] = temp
    return sushi


    

for i in range(Q):
    op = list(input().split())
    cur_t = int(op[1])
    differ = cur_t - prev_t
    
    for _ in range(differ):
        sushi = rotate(sushi)
        sushi = eat(sushi)

    
    #회전은 계속하며 밥도 계속 먹는다.
    #여기서 회전 시켜야함
    
    if op[0] == '100': #초밥 추가
        x, name = int(op[2]), op[3]
        sushi[x].append(name)
        sushi = eat(sushi)

    
    elif op[0] == '200':
        x, name, n = int(op[2]), op[3], int(op[4])
        m2p[x] = name
        people[x] = n
        
        #여기서 즉시 먹는 경우가 존재한다
        sushi = eat(sushi) 


    elif op[0] == '300':
        n_sushi = 0
        n_people = 0
        for i in range(L):
            n_sushi += len(sushi[i])
            if people[i] > 0:
                n_people += 1
        print(n_people, n_sushi)
    
    # print(cur_t, sushi)
    # print(people)

    prev_t = cur_t