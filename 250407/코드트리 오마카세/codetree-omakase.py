L, Q = 0, 0

class Query:
    def __init__(self, cmd, t, x, name, n):
        self.cmd = cmd
        self.t = t
        self.x = x
        self.name = name
        self.n = n

queries = []
names = set()

p_queries = {} # 각 사람마다 주어진 초밥 명령만 관리
entry_time = {} # 각 사람마다 입장 시간 관리합니다.
position = {} #  각 손님 위치
exit_time = {} # 퇴장 시간 

def cmp(q1, q2):
    if q1.t != q2.t: 
        return q1.t < q2.t
    return q1.cmd < q2.cmd

L, Q = map(int, input().split())
for _ in range(Q):
    command = input().split()
    cmd, t, x, n = -1, -1, -1, -1
    name = ''
    cmd = int(command[0])
    if cmd == 100:
        t, x, name = command[1:]
        t, x = map(int, [t,x])
    elif cmd == 200:
        t, x, name, n = command[1:]
        t, x, n = map(int, [t, x, n])
    else:
        t = int(command[1])
    queries.append(Query(cmd, t, x, name, n))

    if cmd == 100:
        if name not in p_queries:
            p_queries[name] = []
        p_queries[name].append(Query(cmd, t, x, name, n))
    
    elif cmd == 200:
        names.add(name)
        entry_time[name] = t
        position[name] = x

for name in names:
    exit_time[name] = 0
    for q in p_queries[name]: #초밥 cmd 
        time_to_remove = 0
        if q.t < entry_time[name]:
            #초밥이 사람이 들어온 시간 전보다 빨리 놓여졌을 경우
            
            t_sushi_x = (q.x + (entry_time[name] - q.t))%L  #entry_time 때 초밥 위치
            #몇 초 더 지나야 만나?
            additional_time = (position[name] - t_sushi_x + L)%L
            time_to_removed = entry_time[name] + additional_time
        else: #이후에 만날 경우
            additional_time = (position[name] - q.x + L)%L
            time_to_removed = q.t + additional_time
        # 초밥이 사라지는 시간 중 가장 늦은 시간을 업데이트 합니다.
        exit_time[name] = max(exit_time[name], time_to_removed)
        # 초밥이 사라지는 111번 쿼리를 추가합니다.
        queries.append(Query(111, time_to_removed, -1, name, -1))

for name in names:
    queries.append(Query(222, exit_time[name], -1, name, -1))

queries.sort(key=lambda q: (q.t, q.cmd))

people_num, sushi_num = 0, 0
for i in range(len(queries)):
    if queries[i].cmd == 100:  # 초밥 추가
        sushi_num += 1
    elif queries[i].cmd == 111:  # 초밥 제거
        sushi_num -= 1
    elif queries[i].cmd == 200:  # 사람 추가
        people_num += 1
    elif queries[i].cmd == 222:  # 사람 제거
        people_num -= 1
    else:  # 사진 촬영시 답을 출력하면 됩니다.
        print(people_num, sushi_num)