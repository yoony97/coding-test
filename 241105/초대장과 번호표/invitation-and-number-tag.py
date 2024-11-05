import sys
input = sys.stdin.readline

n, g = map(int,input().split())
groups = [list(map(int,input().split())) for _ in range(g)]

# 계산
invite_set = set()
invite_set.add(1)

pre_len = len(invite_set)
while True:
    # 2-1: 최대한 초대 처리
    for group in groups:

        # 1: 초대 사람 수
        cnt = 0
        for i in range(1, group[0]+1):
            if group[i] in invite_set:
                cnt += 1

        # 2: k-1개 판단 후 초대
        if cnt == (group[0] - 1):
            for i in range(1, group[0]+1):
                invite_set.add(group[i])

    # 2-2: 기저조건
    if pre_len == len(invite_set):
        break

    # 2-3: 기저조건 처리
    pre_len = len(invite_set)

# 출력
print(len(invite_set))