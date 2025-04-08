class Node:
    def __init__(self):
        self.id = 0
        self.pid = -1
        self.child_IDS = []
        self.auth = 0
        self.alram = 1

MAX_DEPTH = 20
MAX_NODE = 100000
N, Q = map(int, input().split())
Nodes = [Node() for _ in range(N+1)]

def init(cmd):
    parents = cmd[:N]
    authority = cmd[N:]
    for i in range(N):
        pid = parents[i]
        Nodes[i+1].pid = pid
        Nodes[i+1].auth = authority[i]
        if pid != -1:
            Nodes[pid].child_IDS.append(i+1)

def change_parent(c1, c2):
    p1 = Nodes[c1].pid
    p2 = Nodes[c2].pid

    # 부모의 자식 리스트에서 제거
    if p1 != -1:
        Nodes[p1].child_IDS.remove(c1)
    if p2 != -1:
        Nodes[p2].child_IDS.remove(c2)

    # pid 스왑
    Nodes[c1].pid, Nodes[c2].pid = p2, p1

    # 새 부모에게 등록
    if p2 != -1:
        Nodes[p2].child_IDS.append(c1)
    if p1 != -1:
        Nodes[p1].child_IDS.append(c2)

def change_alram(c):
    Nodes[c].alram *= -1

def change_auth(c, power):
    Nodes[c].auth = power

def count_reachable(c):
    count = 0
    print(f"{c}에 도달할 수 있는 알람 방은")
    def dfs(node_idx, depth):
        nonlocal count
        for child in Nodes[node_idx].child_IDS:
            if Nodes[child].auth >= depth + 1 and Nodes[child].alram == 1:
                print(f"{child}가 가능합니다")
                count += 1
                dfs(child, depth + 1)
    dfs(c, 0)
    print(count)


for _ in range(Q):
    cmd = list(map(int, input().split()))
    if cmd[0] == 100:
        init(cmd[1:])
    elif cmd[0] == 200:
        change_alram(cmd[1])
    elif cmd[0] == 300:
        change_auth(cmd[1], cmd[2])
    elif cmd[0] == 400:
        change_parent(cmd[1], cmd[2])
    elif cmd[0] == 500:
        count_reachable(cmd[1])
