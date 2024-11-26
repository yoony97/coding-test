n, m = map(int, input().split())

# 두 사람의 이동을 기록하는 함수
def move(commands):
    current_t = 0
    current_p = 0
    positions = []
    for cmd in commands:
        d, t = cmd.split()
        t = int(t)
        if d == 'R':
            for _ in range(t):
                current_p += 1
                positions.append(current_p)
        else:
            for _ in range(t):
                current_p -= 1
                positions.append(current_p)
    return positions

# 입력 받기
commands_a = [input() for _ in range(n)]
commands_b = [input() for _ in range(m)]

# 두 사람의 이동 경로
A = move(commands_a)
B = move(commands_b)

# 두 사람이 만나는 시간 찾기
meet_time = -1
for i in range(min(len(A), len(B))):
    if A[i] == B[i]:
        meet_time = i
        break

print(meet_time)
