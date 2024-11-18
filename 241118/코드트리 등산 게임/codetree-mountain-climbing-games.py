import bisect

def find_lis_length(li):
    sub = []
    for num in li:
        pos = bisect.bisect_left(sub, num)
        if pos == len(sub):
            sub.append(num)
        else:
            sub[pos] = num
    return len(sub), sub[-1]  # LIS 길이와 마지막 값만 반환

def simulation(m, m_index):
    cable = m_index - 1  # 케이블카 위치
    pre_cable = m[:cable + 1]  # 케이블카 전 구간
    post_cable = m[cable:]  # 케이블카 후 구간

    # 케이블카 이전 LIS 계산
    pre_len, pre_last = find_lis_length(pre_cable)

    # 케이블카 이후 LIS 계산
    post_len, post_last = find_lis_length(post_cable)

    # 점수 계산
    answer = (pre_len + post_len - 1) * 1_000_000  # 중복된 케이블카 위치 제외
    answer += post_last  # 마지막 산의 높이 추가
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
