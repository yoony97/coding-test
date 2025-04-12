import heapq
import sys

class PriorityQueue:
    def __init__(self):          # 빈 Priority Queue 하나를 생성합니다.
        self.items = []
                
    def push(self, item):        # 우선순위 큐에 데이터를 추가합니다.
        heapq.heappush(self.items, item)
                
    def empty(self):             # 우선순위 큐가 비어있으면 True를 반환합니다.
        return not self.items
                
    def size(self):              # 우선순위 큐에 있는 데이터 수를 반환합니다.
        return len(self.items)
        
    def pop(self):               # 우선순위 큐의 최솟값 데이터를 반환하고 제거합니다.
        if self.empty():
            raise Exception("PriorityQueue is empty")
        return heapq.heappop(self.items)
                
    def top(self):               # 우선순위 큐의 최솟값 데이터를 제거하지 않고 반환합니다.
        if self.empty():
            raise Exception("PriorityQueue is empty")
        return self.items[0]


MAX_D = 300
MAX_N = 50000
INF = sys.maxsize

# 해당 도메인에서 해당 문제ID가 레디큐에 있는지 관리합니다.
# SortedSet 대신 set 사용
is_in_readyq = [set() for _ in range(MAX_D + 1)]

# 현재 쉬고 있는 채점기들을 관리합니다.
rest_judger = PriorityQueue()

# 각 채점기가 채점할 때, 도메인의 인덱스를 저장합니다.
judging_domain = [0 for _ in range(MAX_N + 1)]

# 각 도메인별 start, gap, end(채점이 가능한 최소 시간)을 관리합니다.
s = [0 for _ in range(MAX_D + 1)]
g = [0 for _ in range(MAX_D + 1)]
e = [0 for _ in range(MAX_D + 1)]

# 도메인 문자열을 정수 인덱스로 매핑하기 위한 dict (SortedDict → dict)
domainToIdx = {}
global cnt
cnt = 0

# 현재 채점 대기 큐에 있는 task의 개수를 관리합니다.
global ans
ans = 0

# 각 도메인별로 우선순위 큐를 만들어, 우선순위가 가장 높은 URL을 뽑아줍니다.
url_pq = [PriorityQueue() for _ in range(MAX_D + 1)]


# 채점기를 준비합니다.
def Init(query):
    global n, cnt, ans
    (empty, n, url) = query
    n = int(n)

    for i in range(1, n + 1):
        rest_judger.push(i)

    # URL에서 도메인 부분과 숫자 부분을 분리합니다.
    idx = url.find('/')
    domain = url[:idx]
    num = int(url[idx+1:])

    # 만약 도메인이 처음 나온 도메인이라면 domainToIdx에 등록합니다.
    if domain not in domainToIdx:
        cnt += 1
        domainToIdx[domain] = cnt
    domain_idx = domainToIdx[domain]

    # 도메인 번호에 맞는 레디큐에 숫자 부분을 넣습니다.
    is_in_readyq[domain_idx].add(num)

    # 새 URL을 도메인에 맞춰 url_pq에 넣습니다.
    # (id, tme, num)
    newUrl = (1, 0, num)
    url_pq[domain_idx].push(newUrl)

    # 채점 대기 큐에 값이 추가됐으므로 개수를 1 증가합니다.
    ans += 1


# 새로운 URL을 입력받아 레디큐에 추가합니다.
def NewUrl(query):
    global cnt, ans
    (empty, tme, id, url) = query
    tme = int(tme)
    id = int(id)

    # URL에서 도메인 부분과 숫자 부분 분리 (첫 슬래시 기준)
    idx = url.find('/')
    domain = url[:idx]
    num = int(url[idx+1:])

    # 도메인이 처음 나오면 등록
    if domain not in domainToIdx:
        cnt += 1
        domainToIdx[domain] = cnt

    domain_idx = domainToIdx[domain]

    # 이미 레디큐에 있으면 중복이므로 넘어감
    if num in is_in_readyq[domain_idx]:
        return

    # 도메인 번호에 맞는 레디큐에 숫자 추가
    is_in_readyq[domain_idx].add(num)

    # URL을 도메인에 맞춰 url_pq에 넣습니다. (id, tme, num)
    newUrl = (id, tme, num)
    url_pq[domain_idx].push(newUrl)

    # 채점 대기 큐에 값 추가 → 개수 증가
    ans += 1


# 다음 도메인을 찾아 할당합니다.
def Assign(query):
    global ans
    (empty, tme) = query
    tme = int(tme)

    # 쉬고 있는 채점기가 없다면 넘어감
    if rest_judger.empty():
        return

    # 가장 우선순위가 높은 URL을 찾습니다.
    min_domain = 0
    minUrl = (INF, 0, 0)

    for i in range(1, cnt + 1):
        # 현재 채점 중이거나, 현재 시간에 이용할 수 없으면 넘어감
        if e[i] > tme:
            continue

        # i번 도메인에 해당하는 URL이 있다면
        if not url_pq[i].empty():
            curUrl = url_pq[i].top()
            if minUrl > curUrl:
                minUrl = curUrl
                min_domain = i

    # 가장 우선순위가 높은 URL이 존재하면,
    # 해당 도메인과 쉬고 있는 가장 낮은 번호의 채점기를 연결합니다.
    if min_domain:
        judger_idx = rest_judger.top()
        rest_judger.pop()

        # 해당 도메인의 가장 우선순위가 높은 URL을 제거합니다.
        url_pq[min_domain].pop()

        # 도메인의 start, end를 갱신합니다.
        s[min_domain] = tme
        e[min_domain] = INF

        # judger_idx번 채점기가 채점 중인 도메인 번호를 갱신합니다.
        judging_domain[judger_idx] = min_domain

        # 레디큐에서 해당 URL의 숫자를 제거합니다.
        is_in_readyq[min_domain].remove(minUrl[2])

        # 채점 대기 큐에 값이 제거됐으므로 개수 1 감소
        ans -= 1


# 채점 하나를 마무리합니다.
def Finish(query):
    (empty, tme, id) = query
    tme = int(tme)
    id = int(id)

    # 만약 id번 채점기가 채점 중이 아니라면 스킵
    if judging_domain[id] == 0:
        return

    # id번 채점기를 마무리합니다.
    rest_judger.push(id)
    domain_idx = judging_domain[id]
    judging_domain[id] = 0

    # 해당 도메인의 gap, end 값을 갱신합니다.
    g[domain_idx] = tme - s[domain_idx]
    e[domain_idx] = s[domain_idx] + 3 * g[domain_idx]


# 현재 채점 대기 큐에 있는 URL의 개수를 출력합니다.
def Check(query):
    global ans
    (empty, tme) = query
    tme = int(tme)
    print(ans)


q = int(sys.stdin.readline())

for _ in range(q):
    query = sys.stdin.readline().split()

    if int(query[0]) == 100:
        Init(query)
    if int(query[0]) == 200:
        NewUrl(query)
    if int(query[0]) == 300:
        Assign(query)
    if int(query[0]) == 400:
        Finish(query)
    if int(query[0]) == 500:
        Check(query)
