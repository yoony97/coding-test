from collections import deque
COLOR_MAX = 5
MAX_DEPTH = 100
depths = [-1]*(100_001)
max_depth = [-1]*(100_001)
update_time = [0]*(100_001)
colors = [-1]*(100_001)
pids = [-9]*(100_001)
childs = [[] for  i in range(100_001)]
ischanged = [False]*(100_001) #자식이 추가되었는 지 관리
candiate = set()

time = 1

class ColorCount:
    def __init__(self):
        self.cnt = [0] * (COLOR_MAX + 1)

    def __add__(self, obj):
        res = ColorCount()
        for i in range(1, COLOR_MAX + 1):
            res.cnt[i] = self.cnt[i] + obj.cnt[i]
        return res

    # 서로다른 색의 개수의 제곱을 반환합니다
    def score(self):
        result = 0
        for i in range(1, COLOR_MAX + 1):
            result += 1 if self.cnt[i] else 0
        return result * result

def canMakeChild(curr, needDepth):
    if max_depth[curr] == -1:
        return True
    if max_depth[curr] <= needDepth:
        return False
    return canMakeChild(pids[curr], needDepth + 1)

def add_node(body):
    global time
    m_id, p_id, color, depth = body
    if p_id == -1 or canMakeChild(p_id, 1):
        pids[m_id] = p_id
        colors[m_id] = color
        max_depth[m_id] = depth
        childs[p_id].append(m_id)
        update_time[m_id] = time
        time += 1

def change_color(body):
    m_id, color = body
    q = deque([m_id])
    while q:
        curr = q.popleft()
        colors[curr] = color
        for curr in childs[curr]:
            q.append(curr)

def print_color(m_id):
    if pids[m_id] == -9:
        return 0, 0
    info = print_color(pids[m_id])
    if info[1] >  update_time[m_id]:
        return info
    else:
        return colors[m_id], update_time[m_id]    

    
def getBeauty(curr, color, lastUpdate):
    # root에서부터 내려온 색 정보보다 현재 노드의 색정보가 최신이라면 갱신합니다
    if lastUpdate < update_time[curr]:
        lastUpdate = update_time[curr]
        color = colors[curr]
    result = [0, ColorCount()]
    result[1].cnt[color] = 1
    for childId in childs[curr]:
        # 각 자식이 이루는 SubTree에서의 점수와 color count 값을 가져옵니다
        subResult = getBeauty(childId, color, lastUpdate)
        result[1] = result[1] + subResult[1]
        result[0] += subResult[0]
    result[0] += result[1].score()
    return result


Q = int(input())
for i in range(Q):
    cmd = list(map(int, input().split()))
    op, *body = cmd
    if op == 100:
        add_node(body)
    if op == 200:
        change_color(body)
    if op == 300:
        print(print_color(body[0])[0])
    if op == 400:
        beauty = 0
        for i in range(1, 100_001):
            # root 노드들에 대해 점수를 계산합니다
            if pids[i] == -1 :
                beauty += getBeauty(i, colors[i], update_time[i])[0]
        print(beauty)
