class Node:
    def __init__(self):
        self.id = 0
        self.pid = -1
        self.child_IDS = []
        self.auth = 0
        self.alram = 1
    def __repr__(self):
        return f"Node(pid={self.pid}, mid={self.id}, child={self.child_IDS}, auth={self.auth}, alram={self.alram})"

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
        Nodes[i+1].id = i+1
        Nodes[i+1].auth = authority[i]
        if pid != -1:
            Nodes[pid].child_IDS.append(i+1)

def change_parent(c1, c2):
    p1 = Nodes[c1].pid
    p2 = Nodes[c2].pid


    if p1 != -1 and c1 in Nodes[p1].child_IDS:
        Nodes[p1].child_IDS.remove(c1)
    if p2 != -1 and c2 in Nodes[p2].child_IDS:
        Nodes[p2].child_IDS.remove(c2)

    Nodes[c1].pid, Nodes[c2].pid = p2, p1

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
    def dfs(node_idx, depth):
        nonlocal count
        for child in Nodes[node_idx].child_IDS:
            if Nodes[child].alram == 1:
                if Nodes[child].auth >= depth + 1:
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
        #print(f"{cmd[1]} 변경 전 : {Nodes[cmd[1]]}")
        #print(f"{cmd[2]} 변경 전 : {Nodes[cmd[2]]}")
        #print('부모를 변경합니다')
        change_parent(cmd[1], cmd[2])
        #print(f"{cmd[1]} 변경 후 : {Nodes[cmd[1]]}")
        #print(f"{cmd[2]} 변경 후 : {Nodes[cmd[2]]}")
    elif cmd[0] == 500:
        count_reachable(cmd[1])
