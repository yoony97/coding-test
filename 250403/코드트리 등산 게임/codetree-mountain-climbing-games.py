"""
등산가
 1. 현재보다 오른쪽에 위치한 산으로 이동 가능
 2. 항상 현재 산의 높이보다 더 높은 산으로 이동가능

케이블카
 케이블카는 특정 산만 이동 가능
 산 높이 상관 x

- 시뮬레이션 400
  - 오른쪽에 위치한 높은 산으로 이동할때마다 1,000,000점 획득
  - 케이블카를 탈 수 있는 산에 도착시 케이블 카 이용, 1,000,000점 획득
  - 최종적으로 위치한 산의 높이만큼 점수를 얻음

- 빅뱅 : 초기에 산 정의
- 우공이산: 오른쪽 끝에 H 산 APPEND
- 지진: 가장 오른쪽 산 제거
- 등산: 케이블카를 이용할 수 있는 산는 산이 M_INDEX
"""

def can_go(start, heigh, mountains):
    for i in range(start, len(mountains)):
        if heigh < mountains[i]:
            return True
    return False


def simulate(mountains, heigh, start, m_index, use_cable, score):
    global answer
    if not can_go:
        answer = max(answer, score+heigh)
        return

    for i in range(start, len(mountains)):
        if i == m_index and not use_cable:
            simulate(mountains, mountains[0], 0, m_index, True, score + 1000000)
        
        if heigh < mountains[i]:
            simulate(mountains, mountains[i], start+1, m_index, use_cable, score + 1000000)

    



k = int(input())
mountains = []

for _ in range(k):
    temp = list(map(int, input().split()))
    if temp[0] == 100:
        mountains = temp[1:]
    if temp[0] == 200:
        mountains.append(temp[1])
    if temp[0] == 300:
        mountains.pop()
    if temp[0] == 400:
        answer = 0 
        cable_car = temp[1]
        simulate(mountains, 0, 0, cable_car, False, 0):
        print(answer)



