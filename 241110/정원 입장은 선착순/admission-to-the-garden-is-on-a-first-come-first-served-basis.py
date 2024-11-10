# 1 ~ N 번호표 N 명
# idx   사람(번호표)
# a_idx 도착 시간
# t_idx 시간 동안 정원에 머무름
# 1번에 1명
# 모든 사람이 정원을 한 번씩 들려서 머물렀다 갈 때, 이들 중 가장 오래 기다려야 하는 사람이 기다리는 시간을 구하는 프로그램을 작성해보세요.
import heapq
import sys

starts = []
times = []
inputs = sys.stdin.read().strip().split("\n")
N = int(inputs[0])
answers = [0 for i in range(N)]
#init
for i in range(N):
    start, t = map(int, inputs[i+1].split())
    heapq.heappush(starts, (start, i))
    times.append(t)

#처음 사람 초기화
num, idx = heapq.heappop(starts)
current_time = num + times[idx]
answers[idx] = 0 # 처음사람은 안기다려도 되잖아.
waiting = []
while starts:
    #print('wating 인원:', waiting)
    #print('아직 도착하지 않은 인원:', starts)
    #print('현재 시간:', current_time)
    #print('기다린 시간:',answers)
    #대기 인원 큐 저장(현재 시간이 도착시간보다 클 떄 )
    while starts[0][0] <= current_time:
        num, idx = heapq.heappop(starts)
        #print(f"{idx} 님은 {num} 시간에 도착하여 대기합니다.")
        heapq.heappush(waiting,(idx, num)) # 번호표 우선
    
    if waiting:
        idx, num = heapq.heappop(waiting)
    else:
        num, idx = heapq.heappop(starts)

    answers[idx]= current_time - num   # 대기 시간
    current_time += times[idx] # 

#전부다 도착하면 waiting queue만 따로 처리 해줘야함
while waiting:
    idx, num = heapq.heappop(waiting)
    answers[idx]= current_time - num # 대기 시간
    current_time += times[idx] # 

print(max(answers))