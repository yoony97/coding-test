action = list(map(int, input().split()))

score = {
    0: 0, 1: 2, 2: 4, 3: 6, 4: 8, 5: 10,
    6: 12, 7: 14, 8: 16, 9: 18, 10: 20,
    11: 22, 12: 24, 13: 26, 14: 28, 15: 30,
    16: 32, 17: 34, 18: 36, 19: 38, 20: 40,
    21: 13, 22: 16, 23: 19, 24: 25,
    25: 22, 26: 24,
    27: 28, 28: 27, 29: 26,
    30: 30, 31: 35,
    32: 0  # 도착점
}

next_map = {}
for i in range(0, 20):
    next_map[i] = i + 1
next_map[20] = 32  # 도착점

# 분기 경로
next_map[5] = 6
next_map[21] = 22
next_map[22] = 23
next_map[23] = 24
next_map[24] = 30
next_map[30] = 31
next_map[31] = 20

next_map[25] = 26
next_map[26] = 24  # 합류

next_map[27] = 28
next_map[28] = 29
next_map[29] = 24  # 합류

next_map[32] = 32  # 도착점 고정

def move(pos, steps):
    if pos == 32:
        return 32

    for s in range(steps):
        if s == 0:
            # 첫 칸 이동 시에만 분기 고려
            if pos == 5:
                pos = 21
                continue
            elif pos == 10:
                pos = 25
                continue
            elif pos == 15:
                pos = 27
                continue
        pos = next_map[pos]
    return pos


pawn = [0, 0, 0, 0]
answer = 0

def btk(cur_num, total):
    global answer

    if cur_num == 10:
        answer = max(answer, total)
        return

    move_len = action[cur_num]
    for i in range(4):
        if pawn[i] == 32:
            continue

        now = pawn[i]
        new_pos = move(now, move_len)

        # 다른 말과 겹치는지 확인 (도착한 말은 예외)
        if new_pos != 32 and new_pos in pawn:
            continue

        pawn[i] = new_pos
        btk(cur_num + 1, total + score[new_pos])
        pawn[i] = now  # 복구

btk(0, 0)
print(answer)