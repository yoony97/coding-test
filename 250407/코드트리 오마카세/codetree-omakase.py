from collections import defaultdict, deque

L, Q = map(int, input().split())


rotation_offset = 0
prev_t = 0

belt = defaultdict(deque)  # key: belt position, value: deque of sushi names
seat_to_guest = {}         # key: seat position, value: guest name
guest_sushi_goal = {}      # key: seat position, value: number of sushi to eat

def belt_pos_at_seat(x):
    """의자 x 앞에 있는 벨트 위치 계산"""
    return (x - rotation_offset + L) % L

def eat(x):
    """손님이 자기 앞에 있는 초밥 먹기 시도"""
    if guest_sushi_goal.get(x, 0) == 0:
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
                del guest_sushi_goal[x]
                break
        else:
            temp.append(sushi)
    belt[belt_pos] = temp

result = []

for i in range(Q):
    op = list(input().split())
    t = int(op[1])
    diff = t - prev_t

    # 회전 및 먹기 처리
    for _ in range(diff):
        rotation_offset = (rotation_offset + 1) % L
        for x in list(seat_to_guest.keys()):
            eat(x)

    prev_t = t

    if op[0] == "100":
        x, name = int(op[2]), op[3]
        belt[belt_pos_at_seat(x)].append(name)
        if guest_sushi_goal.get(x, 0) > 0:
            eat(x)

    elif op[0] == "200":
        x, name, n = int(op[2]), op[3], int(op[4])
        seat_to_guest[x] = name
        guest_sushi_goal[x] = n
        eat(x)

    elif op[0] == "300":
        n_people = len(guest_sushi_goal)
        n_sushi = sum(len(q) for q in belt.values())
        result.append((n_people, n_sushi))

for x,y in result:
    print(x,y)