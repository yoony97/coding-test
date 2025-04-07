from collections import deque

L, Q = map(int, input().split())

rotation_offset = 0
prev_t = 0

# 초밥 리스트 (고정 크기)
sushi = [deque() for _ in range(L)]

# 손님 이름 정보 (의자 위치 기준)
m2p = {}
# 손님이 먹어야 할 초밥 수
people = [0] * L


rotation_offset = 0
prev_t = 0

belt = [deque() for _ in range(L)]
seat_to_guest = {}  # 실제 의자 번호 x → 이름
guest_sushi_goal = [0] * L  # 실제 의자 번호 x → 남은 초밥 수

def belt_pos_at_seat(x):
    """의자 x 앞에 있는 벨트 위치"""
    return (x - rotation_offset + L) % L

def eat(x):
    """의자 x에 앉은 손님이 먹기 시도"""
    if guest_sushi_goal[x] == 0:
        return
    name = seat_to_guest[x]
    belt_pos = belt_pos_at_seat(x)
    temp = deque()
    while belt[belt_pos]:
        sushi = belt[belt_pos].popleft()
        if sushi == name:
            guest_sushi_goal[x] -= 1
            if guest_sushi_goal[x] == 0:
                del seat_to_guest[x]
                break
        else:
            temp.append(sushi)
    belt[belt_pos] = temp

result = []

for i in range(Q):
    op = list(input().split())
    t = int(op[1])
    diff = t - prev_t

    # 매초 회전 + 먹기
    for _ in range(diff):
        rotation_offset = (rotation_offset + 1) % L
        for x in list(seat_to_guest.keys()):
            eat(x)

    prev_t = t

    if op[0] == "100":  # 초밥 추가
        x, name = int(op[2]), op[3]
        belt_pos = belt_pos_at_seat(x)
        belt[belt_pos].append(name)
        if guest_sushi_goal[x] > 0:
            eat(x)

    elif op[0] == "200":  # 손님 입장
        x, name, n = int(op[2]), op[3], int(op[4])
        seat_to_guest[x] = name
        guest_sushi_goal[x] = n
        eat(x)

    elif op[0] == "300":  # 촬영
        n_people = sum(1 for p in guest_sushi_goal if p > 0)
        n_sushi = sum(len(q) for q in belt)
        result.append((n_people, n_sushi))
    

for x,y in result:
    print(x,y)