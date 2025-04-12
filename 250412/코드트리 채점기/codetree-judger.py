import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

Q = int(input())

# --- 전역 자료구조 ---
# 각 도메인의 상태: 'processing' (채점 중 여부), 'next_available_time', 'waiting'
domain_info = {}  # key: 도메인 문자열, value: dict
def get_domain(dm):
    if dm not in domain_info:
        domain_info[dm] = {
            'processing': False,
            'next_available_time': 0,
            'waiting': False  # 도메인이 waiting 힙에 들어가 있는지 여부
        }
    return domain_info[dm]

# 도메인별 작업 큐 (도메인별 힙)
# 각 작업은 (p, arrival_time, tie, url)
domain_tasks = defaultdict(list)

# 도메인 waiting 힙: (available_time, domain)
# 도메인이 채점이 가능해지는 시점에 넣어두어, 사용가능 시점에 도메인별 작업을 전역 작업 힙으로 이동시킴.
domain_waiting = []

# 전역 작업 힙: (p, arrival_time, tie, domain, url)
tasks_global = []

# 채점기 관련 자료구조
judge_tasks = {}  # judge_id -> (start_time, p, arrival_time, domain, url)
free_judges = []  # 사용 가능한 채점기 id (0-indexed)

# URL 중복 체크
hash_url = {}

# 전체 대기 작업 수
total_pending_tasks = 0

# tie-break를 위한 전역 카운터
tie_counter = 0

debug = False

# --- 함수들 ---
def push_domain_waiting(avail_time, dm):
    """도메인을 waiting 힙에 넣고, waiting 플래그를 세팅"""
    di = get_domain(dm)
    if not di['waiting']:
        heapq.heappush(domain_waiting, (avail_time, dm))
        di['waiting'] = True

def activate_domain_if_ready(current_time):
    """
    waiting 힙에서 available_time <= current_time 인 도메인을 꺼내,
    해당 도메인의 작업 큐(domain_tasks)에서 최우선 작업을 전역 작업 힙(tasks_global)으로 옮깁니다.
    꺼낸 후 waiting 플래그는 False로 전환.
    """
    while domain_waiting and domain_waiting[0][0] <= current_time:
        avail_time, dm = heapq.heappop(domain_waiting)
        di = get_domain(dm)
        di['waiting'] = False
        if (not di['processing']) and domain_tasks[dm]:
            # 도메인 작업 큐에서 우선순위가 가장 높은 작업을 꺼냄
            p, arrival, tie_val, url = heapq.heappop(domain_tasks[dm])
            heapq.heappush(tasks_global, (p, arrival, tie_val, dm, url))

def sync_time(current_time):
    """
    현재 시간 current_time로 갱신 시, 
    (1) 전체 도메인을 순회하여 아직 waiting 상태가 아니면서 처리 가능하면 waiting 힙에 넣고,
    (2) waiting 힙에 있는 도메인을 처리해 전역 작업 힙에 반영합니다.
    (전체 도메인 수는 최대 300이므로 O(300)은 부담되지 않음)
    """
    for dm, di in domain_info.items():
        if (not di['processing']) and (not di['waiting']) and domain_tasks[dm] and (current_time >= di['next_available_time']):
            push_domain_waiting(di['next_available_time'], dm)
    activate_domain_if_ready(current_time)

def init_judges(N):
    """채점기 초기화"""
    global free_judges, judge_tasks
    free_judges = list(range(N))
    heapq.heapify(free_judges)
    judge_tasks.clear()

def request_judge(t, p, u):
    """op=200: t초에 우선순위 p, url=u 로 채점 요청"""
    global total_pending_tasks, tie_counter
    if u not in hash_url or not hash_url[u]:
        hash_url[u] = True
        dm, _ = u.split('/')
        di = get_domain(dm)
        tie_counter += 1
        heapq.heappush(domain_tasks[dm], (p, t, tie_counter, u))
        total_pending_tasks += 1
        if debug:
            print(f"[request_judge] t={t} p={p} url={u}, total_pending={total_pending_tasks}")
        # 도메인이 사용 가능하면 waiting 힙에 등록
        if (not di['processing']) and (t >= di['next_available_time']) and (not di['waiting']):
            push_domain_waiting(di['next_available_time'], dm)
    else:
        if debug:
            print(f"[request_judge] t={t} url={u} duplicate, ignored.")

def try_judge(t):
    """op=300: t초에 가능한 작업을 채점기에 할당 (한 번 할당 후 break)"""
    sync_time(t)
    while free_judges and tasks_global:
        p, arrival, tie_val, dm, url = heapq.heappop(tasks_global)
        di = get_domain(dm)
        if di['processing'] or (not hash_url.get(url, False)):
            continue
        if t < di['next_available_time']:
            continue
        jid = heapq.heappop(free_judges)
        di['processing'] = True
        hash_url[url] = False
        global total_pending_tasks
        total_pending_tasks -= 1
        judge_tasks[jid] = (t, p, arrival, dm, url)
        if debug:
            print(f"[try_judge] t={t} assigned {url} to judge {jid+1}")
        # 문제 해석에 따라 op=300 당 1건만 할당할 경우 break
        break

def end_judge(t, jid_1_based):
    """op=400: t초에 채점기 jid 종료 (1-indexed). 종료 시 도메인의 다음 사용 가능 시각을 계산하고, 대기 상태로 전환"""
    jid = jid_1_based - 1
    if jid not in judge_tasks:
        if debug:
            print(f"[end_judge] t={t} judge {jid_1_based} no task, ignored")
        return
    start_time, p, arrival, dm, url = judge_tasks[jid]
    del judge_tasks[jid]
    di = get_domain(dm)
    di['processing'] = False
    next_time = start_time + 3 * (t - start_time)
    di['next_available_time'] = next_time
    heapq.heappush(free_judges, jid)
    # 종료 후, 도메인의 작업이 남아있다면 waiting 힙에 등록
    if domain_tasks[dm]:
        push_domain_waiting(next_time, dm)
    if debug:
        print(f"[end_judge] t={t} judge {jid+1} finished {url}, {dm} available at {next_time}")

def print_judge(t):
    """op=500: t초에 대기 중인 작업의 총 개수를 출력"""
    print(total_pending_tasks)

# --- 메인 루프 ---
for _ in range(Q):
    cmd = input().split()
    if not cmd:
        continue
    op = int(cmd[0])
    if op == 100:
        #global total_pending_tasks, tie_counter
        total_pending_tasks = 0
        tie_counter = 0
        N = int(cmd[1])
        url = cmd[2]
        domain_info.clear()
        domain_tasks.clear()
        domain_waiting.clear()
        tasks_global.clear()
        judge_tasks.clear()
        free_judges.clear()
        hash_url.clear()
        init_judges(N)
        dm, _ = url.split('/')
        di = get_domain(dm)
        hash_url[url] = True
        tie_counter += 1
        heapq.heappush(domain_tasks[dm], (1, 0, tie_counter, url))
        total_pending_tasks += 1
        # 초기 작업이 있다면 도메인이 사용 가능하므로 waiting 힙에 추가
        if not di['processing'] and (0 >= di['next_available_time']) and (not di['waiting']):
            push_domain_waiting(di['next_available_time'], dm)
        if debug:
            print(f"[init] N={N}, url={url}")
    elif op == 200:
        t, p, u = int(cmd[1]), int(cmd[2]), cmd[3]
        sync_time(t)
        request_judge(t, p, u)
    elif op == 300:
        t = int(cmd[1])
        try_judge(t)
    elif op == 400:
        t = int(cmd[1])
        jid = int(cmd[2])
        sync_time(t)
        end_judge(t, jid)
    elif op == 500:
        t = int(cmd[1])
        sync_time(t)
        print_judge(t)
