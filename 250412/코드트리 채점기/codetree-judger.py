import heapq
import sys

input = sys.stdin.readline

Q = int(input())
N = None

# PQ에 저장할 작업(task)은 리스트 형태로 저장합니다.
# 각 task = [priority, arrival_time, counter, domain, url, valid]
pq = []
task_counter = 0  # 작업 순서 보조 변수

# 도메인 및 URL 관리
hash_dm = {}   # domain 문자열 -> Domain 객체
hash_url = {}  # url 문자열 -> 해당 url이 이미 대기중인지 여부

# 채점기 관리: 채점기 배정 상태는 judge_tasks에 저장하고,
# 사용 가능한 채점기는 free_judges 힙(0-indexed)로 관리합니다.
judge_tasks = {}      # { judge_id: (start_time, priority, arrival_time, domain, url) }
free_judges = []      # 사용 가능한 채점기 id들을 최소 힙으로 관리

debug = False

class Domain:
    def __init__(self, domain):
        self.domain = domain
        self.processing = False
        # 도메인이 아직 처리한 적이 없으면 바로 사용 가능하므로
        # 초기 next_available_time은 0으로 설정합니다.
        self.next_available_time = 0
        self.last_start = -1

    def is_available(self, t):
        # 도메인이 처리 중이 아니고, t가 다음 사용 가능 시각보다 크거나 같다면 사용 가능
        return (not self.processing) and (t >= self.next_available_time)

    def start_judging(self, t):
        self.processing = True
        self.last_start = t

    def end_judging(self, t):
        self.processing = False
        # 다음 사용 가능 시간 = 채점 시작 시각 + 3 * (채점 소요시간)
        self.next_available_time = self.last_start + 3 * (t - self.last_start)

    def __repr__(self):
        return f"Domain({self.domain}, next_available_time={self.next_available_time}, processing={self.processing})"

def request_judge(t, p, u):
    global task_counter
    dm, _ = u.split('/')
    # 같은 URL이 대기큐에 없을 때만 추가 (중복 요청 방지)
    if u not in hash_url or not hash_url[u]:
        hash_url[u] = True
        if dm not in hash_dm:
            hash_dm[dm] = Domain(dm)
        task = [p, t, task_counter, dm, u, True]
        task_counter += 1
        heapq.heappush(pq, task)
        if debug:
            print(f"[채점 요청] {u} 추가: {task}")
    else:
        if debug:
            print(f"[채점 요청] {u} 중복되어 무시됨.")

def try_judge(t):
    global pq
    # 할당 가능한 채점기가 없으면 아무 작업도 진행할 수 없음
    if not free_judges:
        return

    selected_index = -1
    # PQ 전체를 선형 탐색하면서 유효한(task[5] == True) 작업 중 도메인이 사용 가능한 작업을 찾음
    for i, task in enumerate(pq):
        p, arrival, count, dm, u, valid = task
        if not valid:
            continue
        domain = hash_dm[dm]
        if domain.is_available(t):
            selected_index = i
            break

    if selected_index == -1:
        return  # 할당할 수 있는 작업이 없는 경우

    # 찾은 작업은 PQ에서 제거합니다.
    task = pq[selected_index]
    last = pq.pop()  # 마지막 요소와 교체 후 pop
    if selected_index < len(pq):
        pq[selected_index] = last
        heapq.heapify(pq)  # 전체 힙 구조 재정렬
    p, arrival, count, dm, u, valid = task

    # 해당 URL은 대기 상태에서 제거
    hash_url[u] = False
    # 도메인에 채점 시작 처리: 채점기를 할당하기 전 도메인이 사용 중임을 표시
    domain = hash_dm[dm]
    domain.start_judging(t)

    # 사용 가능한 채점기 중 가장 작은 id(0-indexed)를 할당합니다.
    jid = heapq.heappop(free_judges)
    judge_tasks[jid] = (t, p, arrival, dm, u)
    if debug:
        print(f"[채점 시작] 시간 {t}에 채점기 {jid+1}에서 {u} 채점 시작. 작업: {task}")

def end_judge(t, jid):
    # 입력으로 받는 채점기 번호는 1-indexed입니다.
    jid_index = jid - 1
    if jid_index in judge_tasks:
        start_t, p, arrival, dm, u = judge_tasks[jid_index]
        domain = hash_dm[dm]
        domain.end_judging(t)
        del judge_tasks[jid_index]
        # 채점 종료 후, 해당 채점기를 다시 사용 가능한 free_judges 힙에 추가합니다.
        heapq.heappush(free_judges, jid_index)
        if debug:
            print(f"[채점 종료] 시간 {t}에 채점기 {jid}에서 {u} 채점 종료.")
    else:
        if debug:
            print(f"[채점 종료] 시간 {t}에 채점기 {jid}에서 진행 중인 채점이 없어 무시됨.")

def print_judge(t):
    # lazy deletion 기법을 사용하므로, 유효한 작업의 개수를 세서 출력합니다.
    return sum(1 for task in pq if task[5])

# 메인 처리 루프
for _ in range(Q):
    cmd = input().split()
    if not cmd:
        continue
    op = int(cmd[0])
    if op == 100:
        # 100 N url : 초기화 명령
        N = int(cmd[1])
        url = cmd[2]
        dm, _ = url.split("/")
        if dm not in hash_dm:
            hash_dm[dm] = Domain(dm)
        # 초기 작업 추가: 우선순위 1, 시간 0
        hash_url[url] = True
        task = [1, 0, task_counter, dm, url, True]
        task_counter += 1
        heapq.heappush(pq, task)
        # 채점기 초기화 (0부터 N-1까지 사용)
        free_judges = list(range(N))
        heapq.heapify(free_judges)
        judge_tasks = {}
    elif op == 200:
        # 200 t p url : 채점 요청
        t, p, u = int(cmd[1]), int(cmd[2]), cmd[3]
        request_judge(t, p, u)
    elif op == 300:
        # 300 t : 채점기를 이용하여 할당 시도
        t = int(cmd[1])
        try_judge(t)
    elif op == 400:
        # 400 t judge_id : 채점기에서 현재 채점 중인 작업 종료
        t, jid = int(cmd[1]), int(cmd[2])
        end_judge(t, jid)
    elif op == 500:
        # 500 t : 대기 큐에 남은 작업의 개수를 출력
        t = int(cmd[1])
        print(print_judge(t))
