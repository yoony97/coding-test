import heapq
import sys

input =  sys.stdin.readline
Q = int(input())
N = None
pq = [] # 채점 대기 큐
hash_dm = {} # 도메인 - 대기큐에 들어갈 수 있는지 없는지 판단하는 곳
hash_url = {}
isjudge = [False]
judge_el = []
debug = False

class Domain:
    def __init__(self, domain, processing):
        self.domain = domain
        self.processing = processing
        self.start = -1
        self.end = -1

    def update_start(self,t):
        self.start = t

    def update_end(self, t):
        self.end = t

    def get_time(self, t):
        #채점이 시작되지 않았다
        if self.start == -1 and not self.processing:
            return True
        
        #채점이 진행 중이다.
        if self.end == -1 and self.processing:
            return False
        
        if t < self.start + 3*(self.end -  self.start): #부적절한 채점이다.
            return False
        return True
        
    def __repr__(self):
        return f"domain = {self.domain}, start = {self.start}, end = {self.end}"

def request_judge(t, p, u):
    #t초에 우선순위가 p 이면서 url이 u인 문제에 대한 채점 요청이 들어옴
    #채점 Task는 채점 대기 큐에 들어감
    #u가 중복되면 불가능
    
    dm, pid = u.split('/')
    if u not in hash_url:
        hash_url[u] = False
    
    if not hash_url[u]: #대기 중인 url이 없을 떄
        hash_url[u] = True #url이 존재합니다. 체크
        if dm not in hash_dm:
            hash_dm[dm] = Domain(dm, False) #도메인 체크
        heapq.heappush(pq, (p, t, pid, dm, u)) #값 넣어주기
        if debug:
            print(f"[채점 요청] {u}가 들어왔지만 대기중인 u가 {hash_url[u]}라서 추가합니다.")
            print(f"[채점 요청] 추가 후 대기큐 상황: {pq}")
    else:
        if debug:
            print(f"[채점 요청] {u}가 들어왔지만 대기중인 u가 {hash_url[u]}라서 무시합니다.")

def find_judgement():
    for i in range(N):
        if not isjudge[i]:
            return i
    return -1

def try_judge(t):
    impossible = []
    while pq:
        p, st, pid, dm, u = pq[0]
        if debug: print(f"[채점 시작] {t}초에 {dm}과 같은 도메인의 채점 여부가 {hash_dm[dm].processing} 입니다.")
        if not hash_dm[dm].processing: #같은 도메인이 채점 중인가?
            if debug: print(f"[채점 시작] {t}초에 {dm}과 같은 채점 가능 시각 여부가 {hash_dm[dm].get_time(t)} 입니다.")
            if hash_dm[dm].get_time(t): #채점이 가능한가?
                idx = find_judgement() #쉬고있는 채점기가 있는가?
                if debug: print(f"[채점 시작] {t}초에 쉬고있는 채점기가 {idx} 입니다.")
                if idx != -1: #쉬고있는 채점기가 있네
                    if debug: print(f"[채점 시작] {t}초에 채점 가능한 url {u} 입니다. 채점큐에 넣겠습니다.")
                    heapq.heappop(pq)
                    isjudge[idx] = True
                    hash_dm[dm].processing = True
                    hash_url[u] = False #채점 대기큐에서 해당 u가 벗어났어요
                    hash_dm[dm].update_start(t)
                    judge_el[idx] = (t, p, st, pid, dm, u)
                break
                    
        e = heapq.heappop(pq)
        impossible.append(e)

    if impossible:
        for i in impossible:
            heapq.heappush(pq, i)
    if debug: print(f"[채점 시작] 채점기로 옮긴 뒤 대기 큐 상황{pq}")

def end_judge(t, jid):
    #t초에 jid 채점기에서 진행한 채점을 종료함
    #J_id 채점기는 다시 쉼
    #진행된 채점이 없다면 무시
    
    if isjudge[jid]: # 진행중인 채점이 있으면
        if debug: print(f"[채점 종료] {jid}번재 채점기가 {isjudge[jid]} 라서 채점을 종료합니다.")
        judge_start_t, p, input_t,  pid, dm, u = judge_el[jid]
        isjudge[jid] = False #채점 끝 알림
        hash_dm[dm].update_end(t)
        hash_dm[dm].processing = False
        judge_el[jid] = [] #진행 중인 채점 제거
    else:
        if debug: print(f"[채점 종료] {jid}번재 채점기가 {isjudge[jid]} 라서 해당 요청을 무시합니다.")
        
    
def print_judge(t):
    return len(pq)

for i in range(Q):
    cmd = input().split()
    if debug: print(' '.join(cmd))
    op = int(cmd[0])
    if op == 100:
        N = int(cmd[1])
        url = cmd[2]
        dm, pid = url.split("/")
        hash_dm[dm] = Domain(dm, False)
        heapq.heappush(pq, (1, 0, pid, dm, url)) # 우선순위, 시간, 문제아이디, 도메인, url)
        isjudge = [False]*N
        judge_el = [[] for _ in range(N)]

    if op == 200:
        t, p, u = int(cmd[1]), int(cmd[2]), cmd[3] 
        request_judge(t,p,u)
    if op == 300:
        t =  int(cmd[1])
        try_judge(t)
    
    if op == 400:
        t, jid =  int(cmd[1]), int(cmd[2])
        end_judge(t, jid-1)

    if op == 500:
        t = int(cmd[1])
        print(print_judge(t))
    if debug: print()