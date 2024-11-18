#시뮬레이션마다 이동 가능
#등산가 - 현재 위치보다 (높은)오른쪽 산에 이동 가능
#케이블카 - 특정 산에서만 가능
#       - 현재 위치를 포함한 임의의 산으로 이동할 수 있음 (산의 높낮이 상관)

#시뮬레이션
#1. 시작할 산 선택 가능
#2. 등산 성공 시 1,000,000 점 얻음
# 케이블 카 이용 가능시 무조건 이용(이용 성공 시, 1,000,000점)
#또한 최종적으로 도착한 산의 높이만큼 점수를 얻음
import bisect
import bisect

def find_lis(li):
    # LIS 추적용 리스트와 위치 정보
    sub = []  # LIS를 저장 (길이만 관리)
    indices = []  # LIS 원소가 어디에서 왔는지 저장
    parent = [-1] * len(li)  # 각 원소의 이전 위치를 저장
    
    for i, num in enumerate(li):
        pos = bisect.bisect_left(sub, num)  # 삽입 위치 탐색
        if pos == len(sub):
            sub.append(num)
        else:
            sub[pos] = num  # 대체하여 LIS 유지
        
        indices.append(pos)  # 현재 위치를 저장
        
        if pos > 0:
            parent[i] = indices.index(pos - 1)  # 이전 위치를 parent에 저장

    # LIS 복원
    lis_length = len(sub)
    lis = []
    current = indices.index(lis_length - 1)
    while current != -1:
        lis.append(li[current])
        current = parent[current]
    
    return lis[::-1]  # LIS 출력


import bisect

def find_lis_with_target(li, target_index):
    # LIS를 저장할 배열과 관련 정보
    sub = []  # LIS를 점진적으로 유지
    indices = []  # 각 원소의 LIS 위치를 저장
    parent = [-1] * len(li)  # 각 원소의 이전 위치를 저장
    target_index 
    
    for i, num in enumerate(li):
        pos = bisect.bisect_left(sub, num)  # num이 들어갈 위치
        if pos == len(sub):
            sub.append(num)
        else:
            sub[pos] = num  # LIS 유지하기 위해 대체
        
        indices.append(pos)  # 현재 위치 저장
        
        # 이전 위치를 parent에 저장
        if pos > 0:
            parent[i] = indices.index(pos - 1)
        

    # target 값에서부터 LIS 복원
    lis = []
    current = target_index
    while current != -1:
        lis.append(li[current])
        current = parent[current]
    
    return lis[::-1]  # LIS 출력


def simulation(m, m_index):
    answer = 0
    cable = m_index - 1
    root = m[cable]
    pre_cable = find_lis_with_target(m[:cable+1], cable)
    test = pre_cable + find_lis(m)
    answer += (len(test)-1)*1000000
    answer += max(test)
    return answer

import sys
from collections import deque
inputs = sys.stdin.read().strip().split("\n")
m = None
n = int(inputs[0])
for i in range(n):
    ops = list(map(int, inputs[i+1].split()))
    if ops[0] == 100:
        m = ops[2:]
    if ops[0] == 200:
        #우공이산
        m.append(ops[1])
    if ops[0] == 300:
        m.pop()
        #지진
    if ops[0] == 400:
        answer = simulation(m, ops[1])
        print(answer)
