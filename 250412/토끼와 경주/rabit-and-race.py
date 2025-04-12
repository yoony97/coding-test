import sys
import heapq
input = sys.stdin.readline

# 전역(또는 클래스 멤버) 변수들
N = M = P = 0
PID = []         # 각 토끼의 고유 ID
D   = []         # 각 토끼의 이동 거리
R   = []         # 각 토끼의 행 좌표 (1-based)
C   = []         # 각 토끼의 열 좌표 (1-based)
jumpCount = []   # 각 토끼의 점프 횟수
score = []       # 각 토끼의 점수
PID2IDX = {}     # pid -> index
min_pq = []      # 우선순위 큐 (토끼 선택용, lazy deletion) # (점프가 가장 적은 토끼, 행 번호+열번호가 작은 토끼, 행 작은 토끼, 열 작은 토끼, 고유번호 작은 토끼)
max_pq = []      # 우선순위 큐 (추가 점수용, lazy deletion) # (현재 서있는 행 + 열 큰 토끼, 행번호가 큰 토끼, 열번호가 큰 토끼, 고유번호가 큰 토끼) 
valid_state = [] # 각 토끼의 "현재 유효한 (jumpCount, row, col)" 기록
isdebug = False
def init_command(parts):
    """
    예) 100 3 5 2  10 2  20 5
       N=3, M=5, P=2
       토끼 #0: pid=10, d=2
       토끼 #1: pid=20, d=5
    """
    global N, M, P, PID, D, R, C, jumpCount, score, PID2IDX, min_pq, max_pq, valid_state
    N = int(parts[1])
    M = int(parts[2])
    P = int(parts[3])
    data = list(map(int, parts[4:]))  # pid1, d1, pid2, d2, ...
    PID = [0]*P
    D   = [0]*P
    R   = [1]*P   # 모든 토끼 (1,1) 시작
    C   = [1]*P
    jumpCount = [0]*P
    score = [0]*P
    PID2IDX = {}
    min_pq = []
    valid_state = [(0,1,1)] * P  # (jumpCount, row, col) 현재 유효 상태
    
    idx = 0
    for i in range(P):
        pid_val = data[2*i]
        d_val   = data[2*i + 1]
        PID[i]  = pid_val
        D[i]    = d_val
        PID2IDX[pid_val] = i
        # 초기 우선순위 큐에 삽입
        # 우선순위: (jumpCount, row+col, row, col, pid) 오름차순
        # => jumpCount 작을수록, row+col 작을수록, row 작을수록, col 작을수록, pid 작을수록
        heapq.heappush(min_pq, (0, 2, 1, 1, pid_val))
        heapq.heappush(max_pq,(-2,-1, -1, -pid_val, 0))
        valid_state[i] = (0, 1, 1)

def final_pos(p, d, L, direction):
    """
    p: 현재 좌표 (1-based)
    d: 이동해야 할 칸 수
    L: 격자 최대값 (행이면 N, 열이면 M)
    direction: +1이면 증가하는 방향 (아래 혹은 오른쪽), -1이면 감소하는 방향 (위 혹은 왼쪽)
    
    1차원 반사 운동을 주기를 이용해 계산.
    """
    # 특수 케이스: 만약 L == 1 (격자가 한 줄이면 어차피 무조건 1)
    if L == 1:
        return 1

    # 먼저 0-based 좌표로 변환
    if direction == +1:
        start = p - 1
        period = 2 * (L - 1)
        r = (start + d) % period
        if r > L - 1:
            r = period - r
        return r + 1
    else:  # direction == -1, 즉, 위쪽 또는 왼쪽으로 이동
        # 위쪽(또는 왼쪽) 방향은 반대로 계산: 좌표를 뒤집어서 처리
        start = L - p  # 0-based에서의 '역순' 위치
        period = 2 * (L - 1)
        r = (start + d) % period
        if r > L - 1:
            r = period - r
        return L - r  # 다시 반대로 복원

def move_rabbit(rabbit_idx):
    """
    rabbit_idx 토끼를 1회 이동시킨다.
    - 4방향 후보 중 (r+c, r, c)가 가장 큰 곳으로 이동
    - 점프 횟수 += 1, 나머지 토끼의 점수 += (이동 후 r+c)
    - 우선순위 큐에 갱신된 상태를 push (lazy deletion)
    """
    x, y = R[rabbit_idx], C[rabbit_idx]
    dist = D[rabbit_idx]
    cand = []  # (r+c, r, c) 후보
    

    # 4방향
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in dirs:
        if dx != 0:
            # 수직 이동: 행만 변하고 열은 그대로
            if dx == 1:   # 아래 방향
                nx = final_pos(x, dist, N, +1)
            else:         # 위 방향 (dx == -1)
                nx = final_pos(x, dist, N, -1)
            ny = y
        else:
            # 수평 이동: 열만 변하고 행은 그대로
            nx = x
            if dy == 1:   # 오른쪽
                ny = final_pos(y, dist, M, +1)
            else:         # 왼쪽 (dy == -1)
                ny = final_pos(y, dist, M, -1)
        heapq.heappush(cand, (-1*(nx+ny), -nx, -ny))
        
    
    
    best = cand[0]
    new_r = -best[1]
    new_c = -best[2]
    
    jumpCount[rabbit_idx] += 1
    R[rabbit_idx] = new_r
    C[rabbit_idx] = new_c
    
    # 나머지 토끼에게 점수 += new_r + new_c
    gain = new_r + new_c
    for i in range(P):
        if i != rabbit_idx:
            score[i] += gain
    
    # 우선순위 큐에 새 상태 push
    jc = jumpCount[rabbit_idx]
    heapq.heappush(min_pq, (jc, new_r+new_c, new_r, new_c, PID[rabbit_idx]))
    heapq.heappush(max_pq, ( -1*(new_r+new_c), -new_r, -new_c, -PID[rabbit_idx], jc)) #(현재 서있는 행 + 열 큰 토끼, 행번호가 큰 토끼, 열번호가 큰 토끼, 고유번호가 큰 토끼) 
    # valid_state 갱신
    valid_state[rabbit_idx] = (jc, new_r, new_c)

def pick_rabbit():
    """
    우선순위 큐에서 '현재 상태'와 일치하는 토끼를 pop.
    (lazy deletion 기법)
    """
    while True:
        jc, sumrc, rr, cc, pid_val = heapq.heappop(min_pq)
        idx = PID2IDX[pid_val]
        # 지금 토끼의 실제 상태와 일치하는가?
        if (jc, rr, cc) == valid_state[idx] and sumrc == rr+cc:
            return idx
        # 아니면 무효화된 상태 => 계속 pop

def do_k_moves(k):
    """
    K번 반복:
      - 우선순위가 가장 높은 토끼를 pick → 이동
      - '이번 K번 중 한 번이라도 뽑힌' 집합에 기록
    """
    chosen_set = set()
    for t in range(k):
        
        idx = pick_rabbit()
        chosen_set.add(idx)
        if isdebug: print(f"[{t} 이동 전] idx:{idx}, PID:{PID[idx]} 인 토끼가 뽑혔습니다.")
        if isdebug: print(f"[{t} 이동 전] PID:{PID[idx]} 토끼의 위치는 {R[idx]}, {C[idx]}입니다.")
        if isdebug: print(f"[{t} 이동 전] 이동 거리는 {D}입니다.")
        if isdebug: print(f"[{t} 이동 전] 점수는 {score} 입니다.")
        move_rabbit(idx)
        if isdebug: print(f"[{t} 이동 후] PID:{PID[idx]} 토끼의 위치는 {R[idx]}, {C[idx]} 입니다.")
        if isdebug: print(f"[{t} 이동 후] 점수는 {score} 입니다.")
        if isdebug: print()
    
    return chosen_set

def pick_rabbit4S(chosen_set):
    while max_pq:
        sumrc, rr, cc, pid_val, jc = heapq.heappop(max_pq)
        sumrc, rr, cc, pid_val = -sumrc, -rr, -cc, -pid_val
        idx = PID2IDX[pid_val]
        # 지금 토끼의 실제 상태와 일치하는가?
        if (jc, rr, cc) == valid_state[idx] and sumrc == rr+cc and idx in chosen_set:
            return idx
        
def final_scoring(chosen_set, S):
    """
    chosen_set 안의 토끼 중 (r+c, r, c, pid)가 가장 큰 토끼에 S점 부여
    """
    if not chosen_set:
        return
        # 아니면 무효화된 상태 => 계속 pop
    best_idx = pick_rabbit4S(chosen_set)
    if isdebug: print(f"움직인 토끼 중 idx: {best_idx}, pid : {PID[best_idx]} 인 토끼가 제일 높습니다.")
    if isdebug: print(f"부여 전 점수: {score}")
    score[best_idx] += S
    if isdebug: print(f"부여 후 점수: {score}")
def command_200(parts):
    """
    200 K S
    -> K번 이동 후, 그중 한번이라도 뽑힌 토끼에 대해
       (r+c, r, c, pid)가 가장 큰 한 마리에 S점 부여
    """
    K = int(parts[1])
    S = int(parts[2])
    chosen_set = do_k_moves(K)
    final_scoring(chosen_set, S)

def command_300(parts):
    """
    300 pid L
    -> pid 토끼의 이동 거리를 d * L로 변경
    """
    pid_val = int(parts[1])
    L = int(parts[2])
    idx = PID2IDX[pid_val]
    D[idx] *= L

def command_400():
    """
    문제에 따라:
    - 여기서는 '현재 점수가 가장 높은 토끼의 점수를 출력' 예시
      (동률이면 아무나, 혹은 문제에 맞춰 결정)
    """
    print(max(score))

# 메인 예시
Q = int(input().strip())
for _ in range(Q):
    parts = input().split()
    if not parts:
        continue
    op = int(parts[0])
    if op == 100:
        init_command(parts)
    elif op == 200:
        command_200(parts)
    elif op == 300:
        command_300(parts)
    elif op == 400:
        command_400()
