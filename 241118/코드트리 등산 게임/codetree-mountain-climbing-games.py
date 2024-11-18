import bisect
from functools import lru_cache

# LIS를 구하는 함수 (캐싱 활용)
@lru_cache(None)
def find_lis_cached(li):
    sub = []
    for num in li:
        pos = bisect.bisect_left(sub, num)
        if pos == len(sub):
            sub.append(num)
        else:
            sub[pos] = num
    return sub

# 특정 위치에서 타겟을 포함한 LIS를 구하는 함수
def find_lis_with_target(li, target_index):
    sub = []
    parent = [-1] * len(li)
    target = li[target_index]
    lis_end_index = -1

    for i, num in enumerate(li):
        if num > target:
            continue  # 타겟 이후의 LIS는 제외
        pos = bisect.bisect_left(sub, num)
        if pos == len(sub):
            sub.append(num)
            lis_end_index = i
        else:
            sub[pos] = num
        if pos > 0:
            parent[i] = lis_end_index

    # LIS 복원
    lis = []
    current = lis_end_index
    while current != -1:
        lis.append(li[current])
        current = parent[current]
    return lis[::-1]

# 시뮬레이션 수행
def simulation(m, m_index):
    answer = 0
    cable = m_index - 1  # 케이블카 위치
    pre_cable = find_lis_with_target(tuple(m[:cable + 1]), cable)  # 타겟 포함 LIS
    post_cable = find_lis_cached(tuple(m[cable:]))  # 이후 LIS
    test = pre_cable[:-1] + post_cable  # 타겟 제외
    answer += (len(test) - 1) * 1000000
    answer += post_cable[-1]
    return answer

# 메인 로직
import sys
inputs = sys.stdin.read().strip().split("\n")
m = []
n = int(inputs[0])

for i in range(n):
    ops = list(map(int, inputs[i + 1].split()))
    if ops[0] == 100:  # 초기화
        m = ops[2:]
    elif ops[0] == 200:  # 우공이산
        m.append(ops[1])
    elif ops[0] == 300:  # 지진
        m.pop()
    elif ops[0] == 400:  # 시뮬레이션
        answer = simulation(m, ops[1])
        print(answer)
